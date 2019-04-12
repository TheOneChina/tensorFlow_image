"""

    图像二值化处理

"""

import cv2
from PIL import Image
from collections import defaultdict

'''
  自适应阀值二值化
'''
def _get_dynamic_binary_image(image_path):

  im = cv2.imread(image_path)
  im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
  th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
  return th1



'''
  手动二值化 , threshold：像素阀值
  '''
def _get_static_binary_image(img_path, threshold):

  img = Image.open(img_path)
  img = img.convert('L')
  pixdata = img.load()
  w, h = img.size
  for y in range(h):
    for x in range(w):
      if pixdata[x, y] < threshold:
        pixdata[x, y] = 0
      else:
        pixdata[x, y] = 255

  return img

# 获取图片中像素点数量最多的像素：像素阀值
def get_threshold(image):
    pixel_dict = defaultdict(int)

    # 像素及该像素出现次数的字典
    rows, cols = image.size
    for i in range(rows):
        for j in range(cols):
            pixel = image.getpixel((i, j))
            pixel_dict[pixel] += 1

    count_max = max(pixel_dict.values()) # 获取像素出现出多的次数
    pixel_dict_reverse = {v:k for k,v in pixel_dict.items()}
    threshold = pixel_dict_reverse[count_max] # 获取出现次数最多的像素点

    return threshold

def binarizst_handle(image_path):
    # 1- 获取图片中的出现次数最多的像素，即为该图片的背景
    # 2-将图片进行二值化处理
    return _get_dynamic_binary_image(image_path)

"""
使用手动二值化eg:
    image = Image.open(img_path) # 打开图片文件
    imgry = image.convert('L')  # 转化为灰度图
    # 获取图片中的出现次数最多的像素，即为该图片的背景
    max_pixel = get_threshold(imgry)
    _get_static_binary_image(img_path,max_pixel)
"""
