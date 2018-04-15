import os

import cv2
import dlib
import numpy as np
import imutils

path = os.getcwd() + os.sep
path += '../db_aulas/Imagens/obama.jpeg'

img = cv2.imread(path)

sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(img, None)

path2 = os.getcwd() + os.sep
path2 += '../db_aulas/Imagens/obama_knn.jpg'

img2 = cv2.imread(path)
# img2 = imutils.resize(img2, width=500)

sift2 = cv2.xfeatures2d.SIFT_create()
kp2, des2 = sift2.detectAndCompute(img2, None)

im_with_keypoists = cv2.drawKeypoints(img, kp, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", im_with_keypoists)
cv2.waitKey(0)

#kp = sorted(kp, key=lambda x: x.response)[-5::]
#print(kp)

im_with_keypoists = cv2.drawKeypoints(img, kp, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", im_with_keypoists)
cv2.waitKey(0)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des, des2, k=2)

good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
        print(m.distance)

img3 = cv2.drawMatchesKnn(img, kp, img2, kp2, good, None, flags=2)
cv2.imshow("Matches Knn", img3)
cv2.waitKey(0)

