import cv2

image = cv2.imread('../db_images/png/captcha.png')
cv2.imshow('RGB', image)
cv2.waitKey(0)

B = image[:,:,0] + 100
G = image[:,:,1]
R = image[:,:,2]

cv2.imshow("R", R)
cv2.waitKey(0)
cv2.imshow("G", G)
cv2.waitKey(0)
cv2.imshow("B", B)
cv2.waitKey(0)

new_image = cv2.merge([B,G,R])
cv2.imshow("new_image", new_image)
cv2.waitKey(0)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', hsv_image)
cv2.waitKey(0)
cv2.imshow('Hue channels', hsv_image[:,:,0])
cv2.waitKey(0)
cv2.imshow('Saturation channels', hsv_image[:,:,1])
cv2.waitKey(0)
cv2.imshow('Value channels', hsv_image[:,:,2])
cv2.waitKey(0)
