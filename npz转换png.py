

#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import os
from skimage.transform import resize
from glob import glob
import SimpleITK as sitk
file_dir = r"D:\lab资料\数据集\Synapse\train_npz\*"  # npy文件路径
dest_dir = r"D:\lab资料\数据集\Snapse转换\train_npz"  # 文件存储的路径


def npy_png(file_dir, dest_dir):
    # 如果不存在对应文件，则创建对应文件
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    path = glob(file_dir)
    k=0
    for file in path:
        arr = np.load(file)
        z = arr.shape[0] # 获取Z轴大小
        k += 1
        for i in range(z-1):  # 因为是npy是三维的，但是png二维显示，所以我按照Z轴切片进行保存展示
            arr1 = arr[i:i+1,...] #每次增长1 slice
            arr2 = arr1[0, ...] # 将其转换为两维，因为Z轴当前为1，可以省略。
            disp_to_img = resize(arr2, [128, 128])
            plt.imsave(os.path.join(dest_dir, "{}_{}_disp.png".format(k,i)), disp_to_img, cmap='plasma')  # 定义命名规则，保存图片为彩色模式
        ## npy文件转换为nii文件
        # sitk_img = sitk.GetImageFromArray(arr, isVector=False)
        # sitk.WriteImage(sitk_img, os.path.join(dest_dir, str(i) + ".nii"))
        # print('file_name:{}'.format(file))


if __name__ == "__main__":
    npy_png(file_dir, dest_dir)

