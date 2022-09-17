# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:59:07 2022

@author: Johan Lee
"""


import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

img[100:155,100:155] = [0,255,255]

copy = img[37:111,107:194]
img[0:74,0:87] = copy


cv2.imshow('The watch',img)
cv2.waitKey(0)
cv2.destroyAllWindows()