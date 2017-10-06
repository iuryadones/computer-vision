import cv2
import numpy as np

image = cv2.imread('./numbers.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)
cv2.waitKey(0)

cv2.imshow('Gray', gray)
cv2.waitKey(0)

(_, cnts, hierarquia) = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0,255,0), 2)
print("found %d countours" %(len(cnts)))
cv2.imshow("all contours", clone)
cv2.waitKey(0)

clone = image.copy()
for i in range(len(cnts)):
    print("desenhando contorno "+str(i))
    cv2.drawContours(clone, cnts, i, (0,255,0),2)
    cv2.imshow("Contorno Sozinho", clone)
    cv2.waitKey(0)

for i in range(len(cnts)):
    mask = np.zeros(gray.shape, dtype="uint8")
    cv2.drawContours(mask, [cnts[i]],-1,255,-1)
    print("found {}".format(i))
    cv2.imshow("Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image+Mask", cv2.bitwise_and(image,image,mask=mask))
    cv2.waitKey(0)

clone = image.copy()
for c in cnts:
    (x,y,w,h) = cv2.boundingRect(c)
    cv2.rectangle(clone, (x,y), (x+w, y+h), (0, 255,0), 2)
cv2.imshow("Bounding Boxes", clone)
cv2.waitKey(0)
