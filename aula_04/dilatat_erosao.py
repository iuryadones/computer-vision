import cv2
import pylab as plt
import numpy as np

kernel = np.ones((5,5), np.uint8)

image = cv2.imread('../db_aulas/images/license_plate.png', 0)

erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)

dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow('Dilation', dilation)
cv2.waitKey(0)

openig = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Openig', openig)
cv2.waitKey(0)

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
