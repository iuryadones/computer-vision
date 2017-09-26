import os
import cv2
import numpy as np

path = os.getcwd()
sobel_x = cv2.Sobel(image, 0)
cv2.imshow("image", sobel_x)
cv2.waitkey(0)

