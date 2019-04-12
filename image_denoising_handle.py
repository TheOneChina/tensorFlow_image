"""
    图片降噪处理

"""

import sys, os
from PIL import Image, ImageDraw
import cv2

"""
    对图片进行干扰线降噪
"""
def interference_line(img):
    h, w = img.shape[:2]
    # ！！！opencv矩阵点是反的
    # img[1,2] 1:图片的高度，2：图片的宽度
    for y in range(1, w - 1):
        for x in range(1, h - 1):
            count = 0
            if img[x, y - 1] > 245:
                count = count + 1
            if img[x, y + 1] > 245:
                count = count + 1
            if img[x - 1, y] > 245:
                count = count + 1
            if img[x + 1, y] > 245:
                count = count + 1
            if count > 2:
                img[x, y] = 255
    return img




"""
    对图片进行点降噪
"""
def interference_point(image_path,img_name):
     img = Image.open(image_path)
    # # 将图片转换成灰度图片
     img = img.convert("L")
    # # 去噪,G = 50,N = 4,Z = 4
     clearNoise(img, 50, 4, 4)
     handle_out_path = "./handle_img_point"+"/"+img_name
     #保存处理好的图片
     img.save(handle_out_path)
     print(" handle done file :" + img_name)



"""
 二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换
 该函数也可以改成RGB判断的,具体看需求如何
"""
def getPixel(image, x, y, G, N):
    L = image.getpixel((x, y))
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0
    if L == (image.getpixel((x - 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x, y - 1))
    else:
        return None

    # 降噪
    # 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
    # G: Integer 图像二值化阀值
    # N: Integer 降噪率 0 <N <8
    # Z: Integer 降噪次数
    # 输出
    #  0：降噪成功
    #  1：降噪失败


"""
    # 降噪
    # 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点 
    # G: Integer 图像二值化阀值 
    # N: Integer 降噪率 0 <N <8 
    # Z: Integer 降噪次数 
    # 输出 
    #  0：降噪成功 
    #  1：降噪失败
"""
def clearNoise(image, G, N, Z):
    draw = ImageDraw.Draw(image)
    for i in range(0, Z):
        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                color = getPixel(image, x, y, G, N)
                if color != None:
                    draw.point((x, y), color)



def handle(img,img_name):
    # 5.1-对图片进行干扰线降噪
    im =interference_line(img)
    filename = './handle_img_line/' + img_name.split('.')[0] + '.jpg'
    cv2.imwrite(filename, im)
    # 5.2- 对图片进行点降噪
    interference_point(filename,img_name)