import os
import numpy as np
import cv2
import json
import random

# dataPath = 'D:\Files\Dataset\FSCount\Other\jhu_crowd_v2.0'
dataPath = 'D:\Files\Dataset\FSCount\Other\jhu_crowd_v2.0_processed'
# denPath = r'D:\Programs\Git Repo\LearningToCountEverything\test\Sample\den'
# samplePath = r'D:\Programs\Git Repo\LearningToCountEverything\test\apple_multicolor.jpg'
# sampleBoxPath = r'D:\Programs\Git Repo\LearningToCountEverything\test\apple_multicolor_box.txt'
sampleDataset = r'D:\Programs\Git Repo\LearningToCountEverything\test\Sample'
train = 'train'
test = 'test'
den = 'den'
val = 'val'
gt = 'gt'
image = 'images'
img = 'img'


## Check empty annotation file
# trainPath = os.path.join(dataPath, train)
# gtTrainPath = os.path.join(trainPath, gt)
#
# valPath = os.path.join(dataPath, val)
# gtValPath = os.path.join(valPath, gt)
#
# testPath = os.path.join(dataPath, test)
# gtTestPath = os.path.join(testPath, gt)
#
# for file in os.listdir(gtTestPath):
#     # if os.stat(file).st_size == 0:
#     #     print(file)
#     # else:
#     with open(os.path.join(gtTestPath, file), 'r') as f:
#         text = f.read()
#         if text.strip() == '':
#             print(file)

## Check missing gt filePath
# testPath = os.path.join(dataPath, test)
# imgTestPath = os.path.join(testPath, img)
# gtTestPath = os.path.join(testPath, gt)
# for file in os.listdir(imgTestPath):
#     name = file.split('.')[0]
#     missingFilePath = os.path.join(gtTestPath, name+'.txt')
#     if os.path.isfile(missingFilePath):
#         continue
#     print(missingFilePath)

## Conver npy file to csv
# list = os.listdir(denPath)
# filePath = os.path.join(denPath, list[1])
# print(filePath)
# data = np.load(filePath)
# print(data.shape)
# print(len(data))
# with open('1053.csv', 'w') as f:
#     for col in range(data.shape[0]):
#         for row in range(data.shape[1]):
#             f.write(str(data[col, row]))
#             if row < data.shape[1]-1:
#                 f.write(',')
#             elif col < data.shape[0]-1:
#                 f.write('\n')

## Convert csv to npy file
# denSamplePath = r'D:\Files\Dataset\FSCount\Other\SampleDataset\den'
#
# # trainPath = os.path.join(dataPath, train)
# # gtTrainPath = os.path.join(trainPath, gt)
# # denTrainPath = os.path.join(trainPath, den)
# for file in os.listdir(denSamplePath):
#     filename = file.split('.')[0]
#     filePath = os.path.join(denSamplePath, file)
#     list = []
#
#     with open(filePath, 'r') as f:
#         for line in f:
#             temp = []
#             for val in line.split(','):
#                 temp.append(float(val))
#             list.append(temp)
#     npy_file = np.array(list)
#     print(npy_file.shape)
#     savePath = os.path.join(denPath, filename)
#     np.save(savePath+'.npy', npy_file)

## Reformat
sampleDataset += '\\'
anno_file = sampleDataset + 'annotation_FSC147_384.json'
data_split_file = sampleDataset + 'Train_Test_Val_FSC_147.json'
im_dir = sampleDataset + 'images_384_VarV2'
den_dir = sampleDataset + 'den'
anno_dir = sampleDataset + 'anno'
# box_dir = sampleDataset + 'box'

# with open(anno_file, 'w') as file:
#     dict = {}
#     for img in os.listdir(im_dir):
#         print(img)
#         img_path = os.path.join(im_dir, img)
#         filename  = img.split('.')[0]
#         den_path = os.path.join(den_dir, filename+'.npy')
#         anno_path = os.path.join(anno_dir, filename+'.txt')
#         # box_path = os.path.join(box_dir, filename+'_box.txt')
#         image = cv2.imread(img_path, 0)
#         h, w = image.shape
#
#         subDict = {}
#         subDict["H"] = h
#         subDict["W"] = w
#         subDict["density_path"] = den_path
#         subDict["img_path"] = img_path
#
#         with open(anno_path, 'r') as anno:
#             # Get points
#             lines = anno.readlines()
#             p_list  = [v.split()[:2] for v in lines]
#             subDict["points"] = p_list
#
#             # Get 3 random boxes
#             b_list = []
#             box1 = random.randrange(len(lines))
#             box2 = random.randrange(len(lines))
#             box3 = random.randrange(len(lines))
#             lines = [lines[box1], lines[box2], lines[box3]]
#
#             li  = [v.split()[:4] for v in lines]
#             for col in li:
#                 col = [float(val) for val in col]
#                 x, y, w, h = tuple(col)
#                 p1 = [x-w/2, y-h/2]
#
#                 p3 = [x+w/2, y+h/2]
#
#                 p2 = [p1[0], p3[1]]
#
#                 p4 = [p3[0], p1[1]]
#                 b_list.append([p1, p2, p3, p4])
#             subDict["box_examples_coordinates"] = b_list
#
#
#         # with open(box_path, 'r') as box:
#         #     b_list = []
#         #     lines = box.readlines()
#         #     li  = [v.split() for v in lines]
#         #     for col in li:
#         #         p1 = col[:2]
#         #         p1 = [p1[1], p1[0]]
#         #
#         #         p3 = col[2:]
#         #         p3 = [p3[1], p3[0]]
#         #
#         #         p2 = [p1[0], p3[1]]
#         #
#         #         p4 = [p3[0], p1[1]]
#         #         b_list.append([p1, p2, p3, p4])
#         #     subDict["box_examples_coordinates"] = b_list
#
#         dict[img] = subDict
#     json.dump(dict, file)

# with open(data_split_file, 'w') as file:
#     dict = {}
#     list = []
#     for img in os.listdir(im_dir):
#         list.append(img)
#     dict["test"] = list
#     dict["train"] = []
#     dict["val"] = []
#     json.dump(dict, file)

## Remove file
# with open(anno_file, 'r+') as file:
#      anno_json = json.load(file)
#      del anno_json["0071.jpg"]
#      file.seek(0)
#      file.truncate()
#      json.dump(anno_json, file)
#
# with open(data_split_file, 'r+') as file:
#     data_split_json = json.load(file)
#     data_split_json["test"].remove("0071.jpg")
#     file.seek(0)
#     file.truncate()
#     json.dump(data_split_json, file)

# with open(anno_file, 'r') as file:
#     # c = file.read()
#     # print(c[11996655-5:11996655+8])
#     anno_json = json.load(file)
#     print(len(anno_json))

import logging

logging.basicConfig(filename="logfilename.log", level=logging.INFO)
logging.error('your text goes here')
