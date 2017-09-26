import os
import numpy as np
import cv2
import imutils

path = os.getcwd()
image = cv2.imread(path + '/db_images/jpeg/captcha.jpeg')
#image = imutils.resize(image, width=600)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 180)
cv2.imshow('edges', edges)
cv2.waitKey(0)

lines = cv2.HoughLines(edges, 10, np.pi/180, 5)
# HoughCircles()
for lin in lines:
    for rho, theta in lin:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0+100*(-b))
        y1 = int(y0+100*(a))
        x2 = int(x0+1000*(-b))
        y2 = int(x0+1000*(a))
        cv2.line(image, (x1, y1), (x2, y2), (255,0,0), 2)

cv2.imshow("Hough Lines", image)
cv2.waitKey(0)


