import cv2
import numpy as np

sobel_x = cv2.Sobel(image, cv2)
cv2.imshow("image",sobel_x)
