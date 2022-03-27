# coding=utf-8

import os
import json
import numpy as np

def gen_config(args):
    if args.seq != '':
        # generate config from a sequence name
        seq_home = '../vot2019/'
        save_home = '../result_vot2019/'
        result_home = '../result_vot2019/'
        
        seq_name = args.seq
        print(args.seq)
        img_dir = os.path.join(seq_home, seq_name)#, 'img')
        gt_path = os.path.join(seq_home, seq_name, 'groundtruth.txt')

        img_list0 = os.listdir(img_dir)
        img_list = []
        for imname in img_list0:
            if imname.endswith('.jpg'):
                img_list.append(imname)
        img_list.sort()
        img_list = [os.path.join(img_dir,x) for x in img_list]

        gt_8p = np.loadtxt(gt_path, delimiter=',')
        gt = []
        for g8p in gt_8p:
            x1, y1, x2, y2, x3, y3, x4, y4 = g8p
            center_x = (x1+x2+x3+x4)/4
            center_y = (y1+y2+y3+y4)/4
            width = max([x1, x2, x3, x4])-min([x1, x2, x3, x4])
            height = max([y1, y2, y3, y4])-min([y1, y2, y3, y4])
            gt.append(np.array([center_x, center_y, width, height]))
        gt = np.array(gt)
        init_bbox = gt[0]
        
        savefig_dir = os.path.join(save_home,seq_name)
        result_dir = os.path.join(result_home,seq_name)
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
        result_path = os.path.join(result_dir, 'result.json')

    elif args.json != '':
        # load config from a json file

        param = json.load(open(args.json,'r'))
        seq_name = param['seq_name']
        img_list = param['img_list']
        init_bbox = param['init_bbox']
        savefig_dir = param['savefig_dir']
        result_path = param['result_path']
        gt = None
        
    if args.savefig:
        if not os.path.exists(args.savefig):
            savefig_dir = args.savefig
            os.makedirs(savefig_dir)
    else:
        savefig_dir = ''

    return img_list, init_bbox, gt, savefig_dir, args.display, result_path
