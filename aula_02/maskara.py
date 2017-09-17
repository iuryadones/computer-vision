import cv2
import numpy as np

rectangle = np.zeros((300,300), dtype="uint8")
cv2.rectangle(rectangle, (25,25), (275,275), 255, -1)

circle = np.zeros((300,300), dtype="uint8")
cv2.circle(circle, (150,150), 150, 255, -1)

cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)
cv2.imshow("Circle", circle)
cv2.waitKey(0)
cv2.imshow("AND", cv2.bitwise_and(rectangle, circle))
cv2.waitKey(0)
cv2.imshow("OR", cv2.bitwise_or(rectangle, circle))
cv2.waitKey(0)
cv2.imshow("XOR", cv2.bitwise_xor(rectangle, circle))
cv2.waitKey(0)


