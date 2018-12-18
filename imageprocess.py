#coding:utf-8
import numpy as np
import common
from skimage import io,filters
import os

"""
   图像处理类；
"""
class  ImageProcess(object):
    def __init__(self, imgpath):
        self.imgpath = imgpath
        self.img = np.array([])

    def getBinaryImg(self):
        """
        提取出轮廓； 去除背景;
        :return:
        """


    def read(self):
        """
        读取图像；
        :return:
        """
        if common.isFileExist(self.imgpath):
            self.img = io.imread(self.imgpath)
        return self.img

    def write(self, savePath):
        """
        保存数据到本地；
        :param savePath:
        :param savename:
        :return:
        """
        if common.isFileExist(savePath) and not self.img.size:
            io.imsave(savePath, self.img)
        elif not self.img.size:
            if os.mknod(savePath):
                io.imsave(savePath, self.img)

    def show(self):
        if self.img.size:
            io.imshow(self.img)
            io.show()


