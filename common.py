#coding:utf-8

from skimage import io
import  os
"""
    img: numpy数组；
"""
def showimage(img):
    io.imshow(img)
    io.show()


def isFileExist(path):
    """
    检测文件是否存在；
    :param path:
    :return:
    """
    if os.path.isfile(path) and os.path.exists(path):
        return True
    else:
        return False

def isDirExist(path):
    """
    检测路径是否存在；
    :param path:
    :return:
    """
    if os.path.exists(path) and os.path.isdir(path):
        return True
    else:
        return False