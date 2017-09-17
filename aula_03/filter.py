import cv2
import numpy as np

image = cv2.imread('../db_images/png/captcha.png')
cv2.imshow('RGB', image)
cv2.waitKey(0)

blur = cv2.blur(image,(3,3))
cv2.imshow('blur', blur)
cv2.waitKey(0)

gaussian = cv2.GaussianBlur(image,(3,3), 0)
cv2.imshow('Gaussian', gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(image, 5)
cv2.imshow('Median blur', median)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow('blilateral', bilateral)
cv2.waitKey(0)

kernel = np.ones([3,3])
filter2d = cv2.filter2D(image, -1, kernel)
cv2.imshow('filter2d', filter2d)
cv2.waitKey(0)

kernel = np.array([[-1,-1,-1],[-1, 9,-1],[-1,-1,-1]])
filter2d = cv2.filter2D(image, -1, kernel)
cv2.imshow('filter2d', filter2d)
cv2.waitKey(0)
