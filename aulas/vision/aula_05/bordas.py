import os
import cv2
import numpy as np

path = os.getcwd()
image = cv2.imread(path+"/db_images/png/captcha.png")
cv2.imshow("image", image)
cv2.waitKey(0)

sobel_x = cv2.Sobel(image)
cv2.imshow("image", sobel_x)
cv2.waitkey(0)
