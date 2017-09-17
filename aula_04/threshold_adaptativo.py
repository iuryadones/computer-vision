import cv2
import pylab as plt

image = cv2.imread('../db_aulas/images/license_plate.png', 0)
thresh = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15
)
cv2.imshow("OpenCV Mean Thresh", thresh)
cv2.waitKey(0)
