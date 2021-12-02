import os
import numpy as np
import cv2
import json

box_path = r'D:\Programs\Git Repo\LearningToCountEverything\test\Sample\box\0001_box.txt'
p_list = []
with open(box_path, 'r') as box:
    lines = box.readlines()
    li  = [v.split() for v in lines]
    for col in li:
        p1 = col[:2]
        p1 = [p1[1], p1[0]]

        p3 = col[2:]
        p3 = [p3[1], p3[0]]

        p2 = [p1[0], p3[1]]

        p4 = [p3[0], p1[1]]
        p_list.append([p1, p2, p3, p4])
print(p_list)
