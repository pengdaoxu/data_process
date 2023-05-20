import os
# ###################### training/images###########################
# # PATH = 'D:/lab资料/数据集/IDRiD/Segmentation/IDRID/test/masks/'  # 照片所在的路径
# PATH = 'C:/Users/14532/Desktop/images/'  # 照片所在的路径
#
# # 获取该目录下所有文件，存入列表中
# image = os.listdir(PATH)
#
# n = int(1)
# for i in image:
#     if (i == 'IDRiD_' + '%02d' % n + '.tif'):
#         old_name = PATH + i    # 旧文件名（就是路径+文件名）
#         new_name = PATH + '%02d' % n + '_training' + '.tif'  # 新文件名（就是路径+文件名）
#         os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名
#
#     n += 1
#     print('Done')
# ##################################################################


# ###################### training/1st_manual###########################
# # PATH = 'D:/lab资料/数据集/IDRiD/Segmentation/IDRID/test/masks/'  # 照片所在的路径
# PATH = 'C:/Users/14532/Desktop/IDRID_unet_文件名更改/training/1st_manual/'  # 照片所在的路径
#
# # 获取该目录下所有文件，存入列表中
# image = os.listdir(PATH)
#
# n = int(1)
# for i in image:
#     if (i == 'IDRiD_' + '%02d' % n + '_EX' + '.gif'):
#         old_name = PATH + i    # 旧文件名（就是路径+文件名）
#         new_name = PATH + '%02d' % n + '_manual' + '.gif'  # 新文件名（就是路径+文件名）
#         os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名
#
#     n += 1
#     print('Done')
# #################################################################


###################### test/images ###########################
# # PATH = 'D:/lab资料/数据集/IDRiD/Segmentation/IDRID/test/masks/'  # 照片所在的路径
# PATH = 'C:/Users/14532/Desktop/images/'  # 照片所在的路径
#
# # 获取该目录下所有文件，存入列表中
# image = os.listdir(PATH)
#
# n = int(55)
# for i in image:
#     if (i == 'IDRiD_' + '%02d' % n + '.tif'):
#         old_name = PATH + i    # 旧文件名（就是路径+文件名）
#         new_name = PATH + '%02d' % n + '_test' + '.tif'  # 新文件名（就是路径+文件名）
#         os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名
#
#     n += 1
#     print('Done')
# ##################################################################




# ###################### test/1st_manual ###########################
# # PATH = 'D:/lab资料/数据集/IDRiD/Segmentation/IDRID/test/masks/'  # 照片所在的路径
# PATH = 'C:/Users/14532/Desktop/1st_manual/'  # 照片所在的路径
#
# # 获取该目录下所有文件，存入列表中
# image = os.listdir(PATH)
#
# n = int(55)
# for i in image:
#     if (i == 'IDRiD_' + '%02d' % n + '_EX' + '.gif'):
#         old_name = PATH + i    # 旧文件名（就是路径+文件名）
#         new_name = PATH + '%02d' % n + '_manual' + '.gif'  # 新文件名（就是路径+文件名）
#         os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名
#
#     n += 1
#     print('Done')
# ##################################################################


################################################################################################
################################################################################################

###################### training/1st_manual###########################
# PATH = 'D:/lab资料/数据集/IDRiD/Segmentation/IDRID/test/masks/'  # 照片所在的路径
PATH = 'C:/Users/14532/Desktop/IDRID_unet_文件名更改/test/1st_manual/'  # 照片所在的路径

# 获取该目录下所有文件，存入列表中
image = os.listdir(PATH)

n = int(55)
for i in image:
    if (i == '%02d' % n + '_manual' + '.gif'):
        old_name = PATH + i    # 旧文件名（就是路径+文件名）
        new_name = PATH + '%02d' % n + '_manual1' + '.gif'  # 新文件名（就是路径+文件名）
        os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名

    n += 1
    print('Done')
##################################################################
