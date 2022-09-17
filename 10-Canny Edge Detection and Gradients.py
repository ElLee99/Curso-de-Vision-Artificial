# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:26:44 2022

@author: Johan Lee
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame,cv2.CV_64F)

    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    edges = cv2.Canny(frame,100,150)

    cv2.imshow('Original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('Edges',edges)

    k = cv2.waitKey(5) & 0xFF #Esc to end loop
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()