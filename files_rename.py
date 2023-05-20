import os

PATH = 'C:\\Users\\14532\Desktop\\IDRiD_P\\'  # 照片所在的路径
# PATH = './IDRID/test/maskspng/'  # 照片所在的路径

num = int(130)    # 81  54
my_list = []
for i in range(1, num + 1):    # 55 1
    a = 'image' + '%03d' % i
    my_list.append(a)

# 获取该目录下所有文件，存入列表中

image = os.listdir(PATH)

n = 0
for i in image:
    # 旧文件名（就是路径+文件名）
    old_name = PATH + image[n]
    # 新文件名（就是路径+文件名）
    new_name = PATH + 'IDRiD_' + '%02d' % (n+55) + '_0' + '.jpg'  # 可以按照自己的需求改后缀   # 55 1

    # 用os模块中的rename方法对文件改名
    os.rename(old_name, new_name)

    n += 1
    print('Done')