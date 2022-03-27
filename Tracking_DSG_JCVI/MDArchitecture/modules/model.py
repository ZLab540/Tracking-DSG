import os
import scipy.io
import numpy as np
from collections import OrderedDict

import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch


def append_params(params, module, prefix):
    for child in module.children():
        for k, p in child._parameters.iteritems():
            if p is None: continue

            if isinstance(child, nn.BatchNorm2d):
                name = prefix + '_bn_' + k
            else:
                name = prefix + '_' + k

            if name not in params:
                params[name] = p
            else:
                raise RuntimeError("Duplicated param name: %s" % (name))


class LRN(nn.Module):
    def __init__(self):
        super(LRN, self).__init__()

    def forward(self, x):
        #
        # x: N x C x H x W
        pad = Variable(x.data.new(x.size(0), 1, 1, x.size(2), x.size(3)).zero_())
        x_sq = (x ** 2).unsqueeze(dim=1)
        x_tile = torch.cat((torch.cat((x_sq, pad, pad, pad, pad), 2),
                            torch.cat((pad, x_sq, pad, pad, pad), 2),
                            torch.cat((pad, pad, x_sq, pad, pad), 2),
                            torch.cat((pad, pad, pad, x_sq, pad), 2),
                            torch.cat((pad, pad, pad, pad, x_sq), 2)), 1)
        x_sumsq = x_tile.sum(dim=1).squeeze(dim=1)[:, 2:-2, :, :]
        x = x / ((2. + 0.0001 * x_sumsq) ** 0.75)
        return x



class MDNet_new(nn.Module):
    def __init__(self, model_path=None, K=1):
        super(MDNet_new, self).__init__()
        self.K = K
        '''
        self.conv1_1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU()
        )
        self.conv1_2 = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU()
        )
        self.conv1_3 = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.conv2_1 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU()
        )
        self.conv2_2 = nn.Sequential(
            nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.conv3_1 = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.conv4_1 = nn.Sequential(
            nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.conv5_1 = nn.Sequential(
            nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        '''
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 96, kernel_size=7, stride=2),
            nn.ReLU(),
            LRN(),
            nn.MaxPool2d(kernel_size=3, stride=2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(96, 256, kernel_size=5, stride=2),
            nn.ReLU(),
            LRN(),
            nn.MaxPool2d(kernel_size=3, stride=2)
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(256, 512, kernel_size=3, stride=1),
            nn.ReLU()
        )


        '''
        self.conv4 = nn.Sequential(
            nn.Conv2d(512, 512, kernel_size=3, stride=1),
            nn.ReLU()
        )
        '''
        self.fc4 = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(512 * 3 * 3, 512),
            nn.ReLU()
        )
        self.fc5 = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(512, 512),
            nn.ReLU()
        )
        self.branches = nn.ModuleList([nn.Sequential(nn.Dropout(0.5),
                                                     nn.Linear(512, 2)) for _ in range(K)])

        if model_path is not None:
            if os.path.splitext(model_path)[1] == '.pth':
                self.load_model(model_path)
            elif os.path.splitext(model_path)[1] == '.mat':
                self.load_mat_model(model_path)
            else:
                raise RuntimeError("Unkown model format: %s" % (model_path))
        self.build_param_dict()

    def build_param_dict(self):
        self.params = OrderedDict()
        for name, module in self.named_children():
            if name is not 'branches':
                append_params(self.params, module, name)
        for k, module in enumerate(self.branches):
            append_params(self.params, module, 'fc6_%d' % (k))

    def set_learnable_params(self, layers):
        for k, p in self.params.iteritems():
            if any([k.startswith(l) for l in layers]):
                p.requires_grad = True
            else:
                p.requires_grad = False

    def set_stn_learnable_params(self, layers):
        for k, p in self.params.iteritems():
            if any([k.startswith(l) for l in layers]):
                p.requires_grad = True
            else:
                p.requires_grad = False

    def get_learnable_params(self):
        params = OrderedDict()
        for k, p in self.params.iteritems():
            if p.requires_grad:
                params[k] = p
        return params

    def forward(self, x, k=0, in_layer='conv1', out_layer='fc6'):

        #
        # forward model from in_layer to out_layer

        run = False

        for name, module in self.named_children():
            if name == in_layer:
                run = True
            if run:
                if name is not 'branches':
                    x = module(x)
                if name == 'conv3':
                    x = x.view(x.size(0), -1)
                if name == out_layer:
                    return x
        x = self.branches[k](x)
        if out_layer == 'fc6':
            return x
        elif out_layer == 'fc6_softmax':
            return F.softmax(x)

        '''
        x1 = self.conv1(x)
        x2 = self.conv2(x1)
        x3 = self.conv3(x2)
        x4 = self.conv4(x3)
        x5 = x4.view(x4.size(0), -1)
        out5 = self.fc4(x5)
        out6 = self.fc5(out5)
        out7 = self.branches[k](out6)
        if out_layer == 'fc6':
            return out7
        elif out_layer == 'fc6_softmax':
            return F.softmax(out7)  # import torch.nn.functional as  F
        '''

    def load_model(self, model_path):
        states = torch.load(model_path)
        shared_layers = states['shared_layers']
        # self.load_state_dict(shared_layers)
        '''

        self.conv1_1[0].weight.data = shared_layers['conv1_1.0.weight']
        self.conv1_1[0].bias.data = shared_layers['conv1_1.0.bias']

        self.conv1_2[0].weight.data = shared_layers['conv1_2.0.weight']
        self.conv1_2[0].bias.data = shared_layers['conv1_2.0.bias']

        self.conv1_3[0].weight.data = shared_layers['conv1_3.0.weight']
        self.conv1_3[0].bias.data = shared_layers['conv1_3.0.bias']

        self.conv2_1[0].weight.data = shared_layers['conv2_1.0.weight']
        self.conv2_1[0].bias.data = shared_layers['conv2_1.0.bias']

        self.conv2_2[0].weight.data = shared_layers['conv2_2.0.weight']
        self.conv2_2[0].bias.data = shared_layers['conv2_2.0.bias']

        self.conv3_1[0].weight.data = shared_layers['conv3_1.0.weight']
        self.conv3_1[0].bias.data = shared_layers['conv3_1.0.bias']

        #self.conv3_2[0].weight.data = shared_layers['conv3_2.0.weight']
        #self.conv3_2[0].bias.data = shared_layers['conv3_2.0.bias']

        #self.conv3_3[0].weight.data = shared_layers['conv3_3.0.weight']
        #self.conv3_3[0].bias.data = shared_layers['conv3_3.0.bias']

        self.conv4_1[0].weight.data = shared_layers['conv4_1.0.weight']
        self.conv4_1[0].bias.data = shared_layers['conv4_1.0.bias']

        #self.conv4_2[0].weight.data = shared_layers['conv4_2.0.weight']
        #self.conv4_2[0].bias.data = shared_layers['conv4_2.0.bias']

        #self.conv4_3[0].weight.data = shared_layers['conv4_3.0.weight']
        #self.conv4_3[0].bias.data = shared_layers['conv4_3.0.bias']

        self.conv5_1[0].weight.data = shared_layers['conv5_1.0.weight']
        self.conv5_1[0].bias.data = shared_layers['conv5_1.0.bias']

        #self.conv5_2[0].weight.data = shared_layers['conv5_2.0.weight']
        #self.conv5_2[0].bias.data = shared_layers['conv5_2.0.bias']

        #self.conv5_3[0].weight.data = shared_layers['conv5_3.0.weight']
        #self.conv5_3[0].bias.data = shared_layers['conv5_3.0.bias']
        '''




        # print "shared_layers = ", shared_layers[OrderedDict[0]]
        self.conv1[0].weight.data = shared_layers['conv1.0.weight']
        self.conv1[0].bias.data = shared_layers['conv1.0.bias']

        self.conv2[0].weight.data = shared_layers['conv2.0.weight']
        self.conv2[0].bias.data = shared_layers['conv2.0.bias']

        self.conv3[0].weight.data = shared_layers['conv3.0.weight']
        self.conv3[0].bias.data = shared_layers['conv3.0.bias']


        '''

        self.conv4[0].weight.data = shared_layers['conv4.0.weight']
        self.conv4[0].bias.data = shared_layers['conv4.0.bias']
        
        '''

        self.fc4[1].weight.data = shared_layers['fc4.1.weight']
        self.fc4[1].bias.data = shared_layers['fc4.1.bias']

        self.fc5[1].weight.data = shared_layers['fc5.1.weight']
        self.fc5[1].bias.data = shared_layers['fc5.1.bias']

        # for i in range(k):
        # self.branches[k] = shared_layers[k+10]

    def load_mat_model(self, matfile):
        mat = scipy.io.loadmat(matfile)
        mat_layers = list(mat['layers'])[0]

        print "self.conv1[0] = ", self.conv1[0]

        weight, bias = mat_layers[0 * 4]['weights'].item()[0]
        self.conv1[0].weight.data = torch.from_numpy(np.transpose(weight, (3, 2, 0, 1)))
        self.conv1[0].bias.data = torch.from_numpy(bias[:, 0])

        weight, bias = mat_layers[1 * 4]['weights'].item()[0]
        self.conv2[0].weight.data = torch.from_numpy(np.transpose(weight, (3, 2, 0, 1)))
        self.conv2[0].bias.data = torch.from_numpy(bias[:, 0])

        weight, bias = mat_layers[2 * 4]['weights'].item()[0]
        self.conv3[0].weight.data = torch.from_numpy(np.transpose(weight, (3, 2, 0, 1)))
        self.conv3[0].bias.data = torch.from_numpy(bias[:, 0])



class BinaryLoss(nn.Module):
    def __init__(self):
        super(BinaryLoss, self).__init__()

    def forward(self, pos_score, neg_score):
        pos_loss = -F.log_softmax(pos_score)[:, 1]
        neg_loss = -F.log_softmax(neg_score)[:, 0]

        loss = pos_loss.sum() + neg_loss.sum()
        return loss


class Accuracy():
    def __call__(self, pos_score, neg_score):
        pos_correct = (pos_score[:, 1] > pos_score[:, 0]).sum().float()
        neg_correct = (neg_score[:, 1] < neg_score[:, 0]).sum().float()

        pos_acc = pos_correct / (pos_score.size(0) + 1e-8)
        neg_acc = neg_correct / (neg_score.size(0) + 1e-8)

        return pos_acc.data[0], neg_acc.data[0]


class Precision():
    def __call__(self, pos_score, neg_score):
        scores = torch.cat((pos_score[:, 1], neg_score[:, 1]), 0)
        topk = torch.topk(scores, pos_score.size(0))[1]
        prec = (topk < pos_score.size(0)).float().sum() / (pos_score.size(0) + 1e-8)

        return prec.data[0]
