import os

import cv2
import imutils
import numpy as np

path = os.getcwd() + os.sep
png = path + '../db_images/png/captcha.png'
jpeg = path + '../db_images/jpeg/captcha.jpeg'
test = path + '../db_aulas/Imagens/soduku.jpg'

img = cv2.imread(test)
cv2.imshow('Original', img)
cv2.waitKey(0)

ratio = img.shape[0]/500.0
orig = img.copy()
img = imutils.resize(img, height=500)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

print('Step 1: Edge Detection')

cv2.imshow('Image', img)
cv2.waitKey(0)

cv2.imshow('Edged', edged)
cv2.waitKey(0)

clone = edged.copy()
(_, cnts, _) = cv2.findContours(clone, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:50]

screenCnt = None

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02*peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

print('Step 2: Find contours of paper')

cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow('Outline', img)
cv2.waitKey(0)
