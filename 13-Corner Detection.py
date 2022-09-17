# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:40:12 2022

@author: Johan Lee
"""

import cv2
import numpy as np





img = cv2.imread('geometric_figures.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,(255,0,255),-1)
    
cv2.imshow('Result',img)




cv2.waitKey(0)
cv2.destroyAllWindows()