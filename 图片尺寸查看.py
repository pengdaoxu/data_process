from PIL import Image
file_path = 'D:/lab资料/数据集/渗出物分割/IDRID_unet_文件名更改/test/1st_manual/55_manual1.gif'
img = Image.open(file_path)
imgSize = img.size  # 大小/尺寸
w = img.width  # 图片的宽
h = img.height  # 图片的高
f = img.format  # 图像格式

print(imgSize)
print(w, h, f)