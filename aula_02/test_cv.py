#-*- coding: utf-8 -*-

import os

import cv2


if os.sep in __file__.split(os.sep)[0]:
    _file = __file__.split(os.sep)[0]
else:
    _file = ''

path = f'{os.sep}'.join([os.getcwd(), _file])
path += os.sep+'../db_images/'

image_fundo = cv2.imread(path + 'png/captcha.png')
image_menor = cv2.imread(path + 'jpeg/captcha.jpeg')

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
