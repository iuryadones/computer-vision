import os

import cv2
import numpy as np


path = os.path.dirname(os.path.realpath(__file__))
img_path = '../db_aulas/Imagens/gatinhos.jpg'
path = os.path.join(path, img_path)

print(path)

image = cv2.imread(path, 0)

cv2.imshow("Original", image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype="uint8")

cv2.rectangle(mask, (40,90), (150,190), 255, -1, cv2.LINE_AA)
cv2.imshow("AND", cv2.bitwise_and(image, image, mask=mask))
cv2.waitKey(0)

