import os

import cv2
import numpy as np

import pylab as plt

path = os.getcwd() + os.sep
png = path + '../db_images/png/captcha.png'
jpeg = path + '../db_images/jpeg/captcha.jpeg'
path_images = [png, jpeg]

test = path + '../db_aulas/Imagens/basic_shapes.png'

img = cv2.imread(test)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', img)
cv2.waitKey(0)

(_, cnts, hierarquia) = cv2.findContours(gray, 
                                         cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)

print('found {} countours'.format(len(cnts)))

clone = img.copy()
cv2.drawContours(clone, cnts, -1, (0,255,0), 2)
cv2.imshow('All contours', clone)
cv2.waitKey(0)

clone = img.copy()
for i in range(len(cnts)):
    print('Desenhado cotorno {}'.format(i))

    cv2.drawContours(clone, cnts, i, (0,255,0), 2)
    cv2.imshow("Contorno único", clone)
    cv2.waitKey(0)

for i, c in enumerate(cnts):
    print('Mask and Image {}'.format(i+1))

    mask = np.zeros(gray.shape, dtype='uint8')
    cv2.drawContours(mask, [c], -1, 255, -1)

    cv2.imshow('Image', img)
    cv2.imshow('Mask', mask)
    cv2.imshow('Image + Mask', cv2.bitwise_and(clone, clone, mask=mask))
    cv2.waitKey(0)

clone = img.copy()
for i, c in enumerate(cnts):
    print('Retangulo {}'.format(i+1))

    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(clone, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow('Bounding Boxes', clone)
    cv2.waitKey(0)
