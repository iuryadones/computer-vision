import os

import cv2
import numpy as np

if os.sep in __file__.split(os.sep)[0]:
    _file = __file__.split(os.sep)[0]
else:
    _file = ''

path = f'{os.sep}'.join([os.getcwd(), _file])
path += os.sep+'../db_aulas/Imagens/gatinhos.jpg'

print(__file__.split('/')[0])

print(path)

image = cv2.imread(path, 0)

cv2.imshow("Original", image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype="uint8")

cv2.rectangle(mask, (40,90), (150,190), 255, -1, cv2.LINE_AA)
cv2.imshow("AND", cv2.bitwise_and(image, image, mask=mask))
cv2.waitKey(0)

