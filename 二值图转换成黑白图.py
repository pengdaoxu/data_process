import os
import glob
from PIL import Image
import numpy as np

# 指定原始 PNG 图像所在的文件夹
img_folder = "./test/maskspng"

# 枚举文件夹中的所有 PNG 图像
png_files = glob.glob(os.path.join(img_folder, "*.png"))

# 处理每个 PNG 图像
for png_file in png_files:
    # 打开 PNG 图像，并将其转换成灰度图
    with Image.open(png_file) as img:
        # 将图像转换成灰度图
        img = img.convert("L")
        # 将图像转换成 numpy 数组
        img_array = np.array(img)

    # 将灰度图中非零值改为 255
    img_array[img_array != 0] = 255

    # 创建新的 Image 对象，并保存为新的 PNG 图片
    new_img = Image.fromarray(img_array.astype(np.uint8))
    new_img.save(os.path.join(img_folder, os.path.basename(png_file)))