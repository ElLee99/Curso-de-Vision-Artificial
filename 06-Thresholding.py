# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:50:05 2022

@author: Johan Lee
"""

import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retval, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
retval2, threshold1 = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval3,threshold3 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original',img)
cv2.imshow('threshold1',threshold1)
cv2.imshow('threshold2',threshold2)
cv2.imshow('Adaptive threshold',th)
cv2.imshow('Otsu threshold',threshold3)
cv2.waitKey(0)
cv2.destroyAllWindows()