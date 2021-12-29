import os
import numpy as np
import cv2
import json
import random
import argparse

parser = argparse.ArgumentParser(description="Get boxes from data")
parser.add_argument("-dp", "--data_path", type=str, default='../test/Sample/', help="Path to the dataset")
parser.add_argument("-op", "--out_path", type=str, default='../test/demo/', help="Path to the output dir")
parser.add_argument("-im", "--im_name", type=str, default='131.jpg', help="Sample image")
args = parser.parse_args()

data_path = args.data_path
output_dir = args.out_path
anno_file = data_path + 'annotation_FSC147_384.json'
data_split_file = data_path + 'Train_Test_Val_FSC_147.json'
im_dir = data_path + 'images_384_VarV2'
den_dir = data_path + 'den'
anno_dir = data_path + 'anno'


file_name = args.im_name
with open(output_dir+file_name.split('.')[0]+'_box.txt', 'w+') as f:
    with open(anno_file, 'r') as file:
        anno_json = json.load(file)
        box_list = anno_json[file_name]["box_examples_coordinates"]
        for box in box_list:
            top_left = box[0]
            bottom_right = box[2]
            f.write('{} {} {} {}\n'.format(int(top_left[1]), int(top_left[0]), \
                int(bottom_right[1]), int(bottom_right[0])))
