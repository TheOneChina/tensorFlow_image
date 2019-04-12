"""
　该文件为下载验证码图片，作为训练源
"""
import numpy as np  # numpy (1.14.5)
import requests
import cv2
import random
import time


class ImageDownload:
    """
        类创建的时候进行初始化 request 操作，可理解成构造器
    """

    def __init__(self):
        # request url
        self.url = "http://jk.new.4lunzi.com/lunzi/getVerifyCode"

        # request body
        self.header = {
            "Referer": "http://jk.new.4lunzi.com/lunzi/getVerifyCode",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }

    def download(self):
        # request body
        body = {"schoolId": 15}

        # send request
        responseImage = requests.get(self.url, headers=self.header)

        # file flow
        # file.content 是读取的远程文件的字节流
        img = cv2.imdecode(np.fromstring(responseImage.content, np.uint8), 1)

        # download path
        image_name = random.randint(10000, 300000)
        image_type = ".jpg";
        download_path = "./download_img/" + str(image_name) + image_type;

        # save image
        cv2.imwrite(download_path, img)

        # success
        print(" file name :" + str(image_name) + image_type + " save success ")


if __name__ == "__main__":
    print(" download code image start")
    # init class object
    imageDownload = ImageDownload()

    for i in range(20):
        print(i)
        # use download method
        imageDownload.download()
        # thread sleep time, unit seconds
        #time.sleep(1)
