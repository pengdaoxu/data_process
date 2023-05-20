from PIL import Image
import numpy as np

# 打开 PNG 图像，并将其转换成灰度图
img_path = "./train/masks512/IDRiD_01_0.png"
with Image.open(img_path) as img:
    # 将图像转换成灰度图
    img = img.convert("L")
    # 将图像转换成 numpy 数组
    img_array = np.array(img)
    pixels = img.load()

# 输出图像的大小和数据类型
unique_pixels = set()
print("Image size: ", img.size)
print("Image dtype: ", img_array.dtype)
for x in range(img.width):
    for y in range(img.height):
        # 获取当前像素点的灰度值
        gray = pixels[x, y]
        # 将灰度值添加到集合中
        unique_pixels.add(gray)
print(unique_pixels)