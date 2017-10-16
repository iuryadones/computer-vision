import os
import cv2
import numpy as np
from scipy.ndimage.filters import gaussian_filter

path = os.getcwd() + os.sep
#path += '../db_images/png/captcha.png'
path += '../db_images/jpeg/captcha.jpeg'

img = cv2.imread(path)
cv2.imshow('Original image', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=1)
cv2.imshow('sobel x', sobel_x)
cv2.waitKey(0)

sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=1)
cv2.imshow('sobel y', sobel_y)
cv2.waitKey(0)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
cv2.imshow('sobel x', sobel_x)
cv2.waitKey(0)

sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
cv2.imshow('sobel y', sobel_y)
cv2.waitKey(0)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
cv2.imshow('sobel x', sobel_x)
cv2.waitKey(0)

sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow('sobel y', sobel_y)
cv2.waitKey(0)

edges = cv2.Canny(gray, 100, 255)
cv2.imshow('edges', edges)
cv2.waitKey(0)

edges = cv2.Canny(gray, 135, 255)
cv2.imshow('edges', edges)
cv2.waitKey(0)

edges = cv2.Canny(gray, 71, 255)
cv2.imshow('edges', edges)
cv2.waitKey(0)

edges = cv2.Canny(gray, 100, 200)
cv2.imshow('edges', edges)
cv2.waitKey(0)

gaussian_blur5 = cv2.GaussianBlur(gray, (5, 5), 0.)
gaussian_blur3 = cv2.GaussianBlur(gray, (3, 3), 0.)
dog = gaussian_blur5 - gaussian_blur3
cv2.imshow('DoG', dog)
cv2.waitKey(0)

gaussian_blur7 = cv2.GaussianBlur(gray, (7, 7), 0.)
gaussian_blur5 = cv2.GaussianBlur(gray, (5, 5), 0.)
dog = gaussian_blur7 - gaussian_blur5
cv2.imshow('DoG', dog)
cv2.waitKey(0)

def DoG(image, k=200, gamma=1):
    s1 = 0.5
    s2 = s1*k
    gauss1 = gaussian_filter(image, s1)
    gauss2 = gamma*gaussian_filter(image, s2)
    return gauss1 - gauss2

def XDoG(image, epsilon=0.05):
    phi = 10
    difference = DoG(image, 200, 0.98)/255
    diff = difference*image

    for i in range(0, len(difference)):
        for j in range(0, len(difference[0])):
            if difference[i][j] >= epsilon:
                difference[i][j] = 1
            else:
                ht = np.tanh(phi*(difference[i][j] - epsilon))
                difference[i][j] = 1 * ht
    return difference*255

xdog = XDoG(gray, epsilon=0.01)
cv2.imshow('XDoG', xdog)
cv2.waitKey(0)

xdog = XDoG(gray, epsilon=0.05)
cv2.imshow('XDoG', xdog)
cv2.waitKey(0)

xdog = XDoG(gray, epsilon=0.1)
cv2.imshow('XDoG', xdog)
cv2.waitKey(0)




