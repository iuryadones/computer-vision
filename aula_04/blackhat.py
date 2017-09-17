import cv2
import pylab as plt
import numpy as np

gray = cv2.imread('../db_aulas/images/license_plate.png', 0)

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13,5))

blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

cv2.imshow("Original", gray)
cv2.waitKey(0)

cv2.imshow("Blackhat", blackhat)
cv2.waitKey(0)

cv2.imshow("Tophat", tophat)
cv2.waitKey(0)
