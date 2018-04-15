import os

import cv2
import numpy as np

path = os.getcwd() + os.sep
# path += '../db_aulas/Imagens/obama.jpeg'
path += '../db_images/jpeg/captcha.jpeg'
# path += '../db_images/png/captcha.png'

img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detector = cv2.FastFeatureDetector_create()
kps = detector.detect(gray, None)

img2 = cv2.drawKeypoints(img, kps, None, color=(255,0,0))

cv2.imshow("image", np.hstack([img, img2]))
cv2.waitKey(0)
