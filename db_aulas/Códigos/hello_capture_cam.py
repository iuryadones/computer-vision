import cv2
import imutils

cam = cv2.VideoCapture(0)
s, img = cam.read()


winName = "Hello Camera"
#cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
#ubuntu
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)

while s:
  img = imutils.resize(img,600)
  cv2.imshow( winName,img )

  s, img = cam.read()

  key = cv2.waitKey(10)
  #tecla esc
  if key == 27:
    cv2.destroyWindow(winName)
    break

print "Goodbye"

