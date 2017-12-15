import os

import cv2
import numpy as np

path = os.getcwd() + os.sep
png = path + '../db_images/png/captcha.png'
jpeg = path + '../db_images/jpeg/captcha.jpeg'
test = path + '../db_aulas/Imagens/elephant.jpg'

img = cv2.imread(jpeg)
cv2.imshow('Original', img)
cv2.waitKey(0)

Z = img.reshape((-1, 3))
Z = np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

K = 2

ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2', res2)
cv2.waitKey(0)
