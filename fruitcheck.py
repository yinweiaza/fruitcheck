#coding:utf-8
import numpy as np
from skimage import data,io
import common
import imageprocess as proc


if __name__ == '__main__':
    imgproc = proc.ImageProcess('image/orange1.jpg')
    imgproc.read()
    imgproc.show()

