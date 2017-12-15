import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0,100,(51,2)).astype(np.float32)
responses = np.random.randint(0,2,(51,1)).astype(np.float32)

red = trainData[responses.ravel()==0] 
blue = trainData[responses.ravel()==1]

plt.scatter(red[:,0], red[:,1], 80, 'r', '^')
plt.scatter(blue[:,0], blue[:,1], 80, 'b', 's')

newcomer = np.random.randint(0, 100, (1,2)).astype(np.float32)
plt.scatter(newcomer[:,0], newcomer[:,1], 80, 'g', 'o')

knn = cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE,responses)

ret, results, neighbours, dist = knn.findNearest(newcomer, 3)

print ("results: ", results,"\n")
print ("neighbours: ", neighbours,"\n")
print ("distances: ", dist)

plt.show()
