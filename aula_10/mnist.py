from collections import Counter

import numpy as np
from skimage.feature import hog
from sklearn.externals import joblib
from sklearn.datasets.mldata import fetch_mldata
from sklearn.svm import LinearSVC

dataset = fetch_mldata('mnist-original', data_home='./MNIST')

features = np.array(dataset.data, 'int16')
labels = np.array(dataset.target, 'int')

list_hog_fd = []
for feature in features:
    fd = hog(feature.reshape((28, 28)), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1))
    list_hog_fd.append(fd)

hog_features = np.array(list_hog_fd, 'float64')

print("Count of digits in dataset", Counter(labels))

clf = LinearSVC()
clf.fit(hog_features, labels)

joblib.dump(clf, 'digits_cls.pkl', compress=3)

clf = joblib.load('digits_cls.pkl')
