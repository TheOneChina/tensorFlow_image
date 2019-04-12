"""
对download 下载的图片进行处理
handle way :
    1 - 图像二值化(Image Binarization)：就是将图像上的像素点的灰度值设置为0或255，
        也就是将整个图像呈现出明显的黑白效果的过程　－－　去除图片色彩,使其呈现为黑白色。
    2 - 降噪(Image Denoising)：图片中随机分布的像素点或者干扰线

"""
import os
import image_binarization_handle
import image_clearBorder
import image_denoising_handle
import cv2
from PIL import Image, ImageDraw
from PIL import Image


def image_handle(directory):
    print("base image file path:" + "directory")
    # 1- 循环该目录下的所有文件
    for file in os.listdir(directory):
        # 2- 判断文件后缀是否为指定格式
        if file.endswith(".jpg") or file.endswith(".png"):
            image_name = file
            image_path = directory + "/" + image_name
            # 3-  自适应阈值二值化
            im = image_binarization_handle.binarizst_handle(image_path)
            # 4- 去除边框
            im = image_clearBorder.clear_border(im)
            #
            image_denoising_handle.handle(im,image_name)


if __name__ == "__main__":
    image_dir = './download_img'
    image_handle(image_dir)
