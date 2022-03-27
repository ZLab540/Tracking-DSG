import json
import scipy.io as scio
with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Basketball/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '1'


len = 725
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/basketball_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Bolt/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '2'


len = 350
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/Bolt_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Boy/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '3'


len = 602
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/boy_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Car4/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '4'


len = 659
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/car4_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/CarDark/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '5'


len = 393
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/carDark_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/CarScale/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '6'


len = 252
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/carScale_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})


with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Coke/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '7'


len = 291
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/coke_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Couple/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '8'


len = 140
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/couple_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Crossing/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '9'


len = 120
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/crossing_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/David/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '10'


len = 471
annoBegin = 300
startFrame = 300

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/david_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/David2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '11'


len = 537
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/david2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/David3/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '12'


len = 252
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/david3_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Deer/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '13'


len = 71
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/deer_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Dog1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '14'


len = 1350
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/dog1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Doll/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '15'


len = 3872
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/doll_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Dudek/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '16'


len = 1145
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/dudek_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/FaceOcc1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '17'


len = 892
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/faceOcc1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/FaceOcc2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '18'


len = 812
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/faceOcc2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})


with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Fish/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '19'


len = 476
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/fish_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/FleetFace/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '20'


len = 707
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/fleetFace_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Football/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '21'


len = 362
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/football_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Football1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '22'


len = 74
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/football1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Freeman1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '23'


len = 326
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/freeman1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Freeman3/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '24'


len = 460
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/freeman3_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Freeman4/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '25'


len = 283
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/freeman4_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Girl/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '26'


len = 500
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/girl_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Ironman/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '27'


len = 166
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/ironman_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Jogging-1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '28'


len = 307
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/jogging-1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Jogging-2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '29'


len = 307
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/jogging-2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Jumping/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '30'


len = 313
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/jumping_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Lemming/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '31'


len = 1336
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/lemming_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})


with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Liquor/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '32'


len = 1741
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/liquor_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Matrix/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '33'


len = 100
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/matrix_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Mhyang/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '34'


len = 1490
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/mhyang_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/MotorRolling/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '35'


len = 164
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/motorRolling_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/MountainBike/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '36'


len = 228
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/mountainBike_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Shaking/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '37'


len = 365
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/shaking_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Singer1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '38'


len = 351
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/singer1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Singer2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '39'


len = 366
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/Singer2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Skating1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '40'


len = 400
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/skating1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Skiing/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '41'


len = 81
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/skiing_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Soccer/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '42'


len = 392
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/soccer_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Subway/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '43'


len = 175
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/subway_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})


with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Suv/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '44'


len = 945
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/suv_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Sylvester/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '45'


len = 1345
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/sylvester_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Tiger1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '46'


len = 349
annoBegin = 1
startFrame = 6

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/tiger1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Tiger2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '47'


len = 365
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/tiger2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Trellis/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '48'


len = 569
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/trellis_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Walking/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '49'


len = 412
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/walking_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})


with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Walking2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '50'


len = 500
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/walking2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Woman/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '51'


len = 597
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/woman_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})





import json
import scipy.io as scio
with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Biker/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '52'


len = 142
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/biker_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Bird1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '53'


len = 408
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/bird1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Bird2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '54'


len = 99
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/bird2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/BlurBody/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '55'


len = 334
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/blurBody_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/BlurCar1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '56'


len = 742
annoBegin = 247
startFrame = 247

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/blurCar1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/BlurCar2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '57'


len = 585
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/blurCar2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})


with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/BlurCar3/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '58'


len = 357
annoBegin = 3
startFrame = 3

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/blurCar3_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/BlurCar4/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '59'


len = 380
annoBegin = 18
startFrame = 18

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/blurCar4_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/BlurFace/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '60'


len = 493
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/blurFace_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/BlurOwl/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '61'


len = 631
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/blurOwl_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Board/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '62'


len = 698
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/board_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Bolt2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '63'


len = 293
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/bolt2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Box/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '64'


len = 1161
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/box_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Car1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '65'


len = 1020
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/car1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Car2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '66'


len = 913
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/car2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Car24/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '67'


len = 3059
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/car24_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/ClifBar/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '68'


len = 472
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/clifBar_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Coupon/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '69'


len = 327
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/coupon_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})


with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Crowds/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '70'


len = 347
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/crowds_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Dancer/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '71'


len = 225
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/dancer_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Dancer2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '72'


len = 150
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/dancer2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Diving/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '73'


len = 215
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/diving_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Dog/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '74'


len = 127
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/dog_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/DragonBaby/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '75'


len = 113
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/dragonBaby_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Girl2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '76'


len = 1500
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/girl2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Gym/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '77'


len = 767
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/gym_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Human2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '78'


len = 1128
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/human2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Human3/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '79'


len = 1698
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/human3_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Human4/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '80'


len = 667
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/human4_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Human5/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '81'


len = 713
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/human5_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Human6/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '82'


len = 792
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/human6_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})


with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Human7/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '83'


len = 250
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/human7_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Human8/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '84'


len = 128
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/human8_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Human9/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '85'


len = 305
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/human9_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Jump/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '86'


len = 122
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/jump_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/KiteSurf/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '87'


len = 84
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/kiteSurf_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Man/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '88'


len = 134
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/man_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Panda/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '89'


len = 1000
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/panda_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/RedTeam/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '90'


len = 1918
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/redTeam_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Rubik/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '91'


len = 1997
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/rubik_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Skater/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '92'


len = 160
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/skater_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Skater2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '93'


len = 435
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/skater2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Skating2-1/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '94'


len = 473
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/skating2-1_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})


with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Skating2-2/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '95'


len = 473
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/skating2-2_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Surfer/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '96'


len = 376
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/surfer_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Toy/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '97'


len = 271
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/toy_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Trans/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '98'


len = 124
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/trans_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Twinnings/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '99'


len = 472
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/twinnings_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})



with open("/media/lab540/disk2/lizizi/py-MDNet-master/result100/Vase/result.json", 'r') as f:
  temp = json.loads(f.read())
#print(temp)
res = temp['res']
type = temp['type']
fps = temp['fps']

print '100'


len = 271
annoBegin = 1
startFrame = 1

resultnew = '/media/lab540/disk2/lizizi/py-MDNet-master/result100_mat/vase_DGNT.mat'
scio.savemat(resultnew,{'results':{'res':res,'type':type,'fps':fps,'len':len,'annoBegin':annoBegin,'startFrame':startFrame}})

