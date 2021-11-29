import os

dataPath = 'D:\Files\Dataset\FSCount\jhu_crowd_v2.0'
train = 'train'
test = 'test'
val = 'val'
gt = 'gt'
image = 'images'


trainPath = os.path.join(dataPath, train)
gtTrainPath = os.path.join(trainPath, gt)

for file in os.listdir(gtTrainPath):
    # if os.stat(file).st_size == 0:
    #     print(file)
    # else:
    with open(os.path.join(gtTrainPath, file), 'r') as f:
        text = f.read()
        if text.strip() == '':
            print(file)
