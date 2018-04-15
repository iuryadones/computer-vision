#-*- coding: utf-8 -*-

import os

import cv2


path = os.path.dirname(os.path.realpath(__file__))

img_paths = [
    '../db_images/png/captcha.png',
    '../db_images/jpeg/captcha.jpeg'
]

image_fundo = cv2.imread(os.path.join(path, img_paths[0]))
image_menor = cv2.imread(os.path.join(path, img_paths[1]))

altura = image_fundo.shape[0]
channels = image_fundo.shape[2]
largura = image_fundo.shape[1]

meia_altura = int(altura/2)
meia_largura = int(largura/2)

print("altura: {} pixels".format(image_fundo.shape[0]))
print("channels: {} pixels".format(image_fundo.shape[2]))
print("largura: {} pixels".format(image_fundo.shape[1]))

print (image_menor[0:meia_altura, 0:meia_largura])

image_fundo[0:meia_altura, 0:meia_largura] = (0, 255, 0)  # (Blue, Green, Red)

# ou

image_fundo[0:meia_altura, 0:meia_largura] = image_menor[0:meia_altura, 0:meia_largura]

cv2.imshow("Imagem", image_fundo )
cv2.waitKey(0)
