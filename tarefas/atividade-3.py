import cv2
import numpy as np

img = cv2.imread("../db_images/png/captcha.png", 0)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

threshN = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for n,thresh in enumerate(threshN):
    cv2.imshow('Thresh {}'.format(n), thresh)
    cv2.waitKey(0)
