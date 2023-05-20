
#########################################################masks############################################

import cv2
import os

# 定义输入和输出文件夹路径
input_folder = './test/maskspng'
output_folder = './test/masks512'

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的每个图片文件
for file_name in os.listdir(input_folder):
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        # 使用 OpenCV 的 imread() 函数读取图片
        img_path = os.path.join(input_folder, file_name)
        img = cv2.imread(img_path)

        # 将图片 resize 到指定大小
        img_resized = cv2.resize(img, (512, 512))
        _, thresh = cv2.threshold(img_resized, 127, 255, cv2.THRESH_BINARY)

        # 输出到指定文件夹，并保留原始图片的文件名
        output_path = os.path.join(output_folder, file_name)
        cv2.imwrite(output_path, thresh)
#########################################################################################################

##################################################images################################################
import cv2
import os
import shutil

# 定义输入和输出文件夹路径
input_folder = 'C:\\Users\\14532\\Desktop\\IDRiD_P'
output_folder = 'C:\\Users\\14532\\Desktop\\IDRiD_P'

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的每个图片文件
for file_name in os.listdir(input_folder):
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        # 使用 OpenCV 的 imread() 函数读取图片
        img_path = os.path.join(input_folder, file_name)
        img = cv2.imread(img_path)

        # 将图片 resize 到指定大小
        img_resized = cv2.resize(img, (512, 512))

        # 输出到指定文件夹，并保留原始图片的文件名
        output_path = os.path.join(output_folder, file_name)
        cv2.imwrite(output_path, img_resized)