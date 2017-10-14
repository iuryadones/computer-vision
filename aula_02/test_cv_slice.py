#-*- coding: utf-8 -*-

import os
import cv2

path = os.getcwd() + os.sep
path += '../db_images/'

image_fundo = cv2.imread(path + 'png/captcha.png')
image_menor = cv2.imread(path + 'jpeg/captcha.jpeg')

print(image_menor)

altura = image_fundo.shape[0]
channels = image_fundo.shape[2]
largura = image_fundo.shape[1]

meia_altura = int(altura/2)
meia_largura = int(largura/2)

print("largura: {} pixels".format(image_fundo.shape[1]))
print("altura: {} pixels".format(image_fundo.shape[0]))
print("channels: {} pixels".format(image_fundo.shape[2]))

# print (image_menor[0:meia_altura, 0:meia_largura])
# image_fundo[0:meia_altura, 0:meia_largura] = (0, 255, 0)  # (Blue, Green, Red)

#image_fundo[0:meia_altura, 0:meia_largura] = image_menor[0:meia_altura, 0:meia_largura]

red = (0,0,255)
init_point =  (meia_largura, meia_altura)
end_point = (meia_largura + 50, meia_altura + 20)

cv2.rectangle(image_fundo, init_point, end_point, red, 0)
image_crop = image_fundo[init_point[1]:end_point[1], init_point[0]:end_point[0]]

cv2.imshow("Imagem_crop", image_crop)
cv2.waitKey(0)

cv2.imshow("Imagem", image_fundo)
cv2.waitKey(0)
