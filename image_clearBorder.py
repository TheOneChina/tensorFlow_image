"""

    去除图像边框

"""

'''
    去除边框
'''
def clear_border(img):
    h, w = img.shape[:2]
    for y in range(0, w):
        for x in range(0, h):
            # if y ==0 or y == w -1 or y == w - 2:
            if y < 4 or y > w - 4:
                img[x, y] = 255
            # if x == 0 or x == h - 1 or x == h - 2:
            if x < 4 or x > h - 4:
                img[x, y] = 255

    return img
