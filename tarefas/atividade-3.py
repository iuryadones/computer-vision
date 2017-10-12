import cv2
import numpy as np

def mean_std(image, win):
    height = image.shape[0]
    width = image.shape[1]
    
    mean = np.ones(image.shape)
    std = np.ones(image.shape)

    for h in range(0, height, win):
        for w in range(0, width, win):
            mean[h:h+win, w:w+win]*=np.mean(image[h:h+win, w:w+win])
            std[h:h+win, w:w+win]*=np.std(image[h:h+win, w:w+win])
    return mean, std

def threshold_sauvola(image, window_size, k, r=None):
    result = np.zeros(image.shape)

    if r is None: 
        r = 0.5*(image.max()-image.min()) 

    m, s = mean_std(image, window_size)
    T = m * (1 + k * ((s / r) - 1))

    bright = T >= image
    dark = T < image
    result[bright] = 1
    result[dark] = 0

    return result

img = cv2.imread("../db_images/png/captcha.png", 0)

image = threshold_sauvola(img, window_size=3, k=0.999, r=128)
cv2.imshow('Sauvola win=3, k=0.999', image)
cv2.waitKey(0)

image = threshold_sauvola(img, window_size=5, k=0.05)
cv2.imshow('Sauvola win=5, k=0.05', image)
cv2.waitKey(0)

image = threshold_sauvola(img, window_size=7, k=0.032)
cv2.imshow('Sauvola win=7, k=0.032', image)
cv2.waitKey(0)

image = threshold_sauvola(img, window_size=3, k=0.999)
cv2.imshow('Sauvola win=3, k=0.999', image)
cv2.waitKey(0)

ret, thresh1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV)

threshN = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for n,thresh in enumerate(threshN):
    cv2.imshow('Thresh {}'.format(n), thresh)
    cv2.waitKey(0)
