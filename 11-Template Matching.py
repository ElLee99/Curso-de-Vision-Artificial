# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:46:09 2022

@author: Johan Lee
"""

import numpy as np
import cv2


img_original = cv2.imread('fruits.jpg',cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)


template = cv2.imread('orange.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.45
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_original, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

cv2.imshow('Result',img_original)
cv2.waitKey(0)
cv2.destroyAllWindows()