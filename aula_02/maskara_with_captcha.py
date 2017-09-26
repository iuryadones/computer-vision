import os
import cv2
import numpy as np

path = os.getcwd()
image = cv2.imread(path + '/db_aulas/images/gatinhos.jpg')
cv2.imshow("Original", image)
#cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype="uint8")

#rectangle = np.zeros((300,300), dtype="uint8")
cv2.rectangle(mask, (40,90), (150,190), 255, -1)

#circle = np.zeros((300,300), dtype="uint8")
#cv2.circle(circle, (150,150), 150, 255, -1)

#cv2.imshow("Rectangle", rectangle)
#cv2.waitKey(0)
#cv2.imshow("Circle", circle)
#cv2.waitKey(0)
cv2.imshow("AND", cv2.bitwise_and(image, image, mask=mask))
cv2.waitKey(0)
#cv2.imshow("OR", cv2.bitwise_or(rectangle, circle))
#cv2.waitKey(0)
#cv2.imshow("XOR", cv2.bitwise_xor(rectangle, circle))
#cv2.waitKey(0)


