import os
from collections import Counter

import cv2
import numpy as np
from skimage.feature import hog
from sklearn.externals import joblib

path = os.getcwd() + os.sep
path += '../db_aulas/Imagens/numbers.jpg'

clf = joblib.load('digits_cls.pkl')

im = cv2.imread(path)
cv2.imshow('Digits Original', im)
cv2.waitKey(0)

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Gray', gray)
cv2.waitKey(0)

gray = cv2.GaussianBlur(gray, (21, 21), 0.5)
cv2.imshow('GaussianBlur Gray', gray)
cv2.waitKey(0)

ret, im_th = cv2.threshold(gray, 127, 255, 0)
im2, cnts, hierarchy = cv2.findContours(im_th, 1, 2)

rects = [cv2.boundingRect(cnt) for cnt in cnts]
for rect in rects:
    leng = int(rect[3] * 1.)
    pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
    pt2 = int(rect[0] + rect[2] // 2 - leng // 2)

    roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
    roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
    roi = cv2.dilate(roi, (3, 3))

    cv2.imshow("Roi", roi)
    cv2.waitKey(200)

    roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1))
    nbr = clf.predict(np.array([roi_hog_fd], 'float64'))

    cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
    cv2.putText(im, str(int(nbr[0])), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

cv2.imshow("Resulting Image with Rectangular ROIs", im)
cv2.waitKey(0)
