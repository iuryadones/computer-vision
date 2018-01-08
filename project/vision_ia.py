import cv2
import numpy as np
import pylab as plt

image = cv2.imread('../db_images/jpeg/captcha.jpeg')
plt.title("BGR")
plt.xticks([])
plt.yticks([])
plt.imshow(image)
plt.tight_layout()
plt.show()
