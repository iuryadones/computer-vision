from collections import Counter
import os

from skimage.feature import hog
from sklearn.datasets.mldata import fetch_mldata
from sklearn.externals import joblib
from sklearn.svm import LinearSVC
import cv2
import numpy as np


def loader_data(origin):
    dataset = fetch_mldata(origin, data_home='./train')
    features = np.array(dataset.data, 'int16')
    labels = np.array(dataset.target, 'int')
    print("Count of digits in dataset", Counter(labels))

    return features, labels


def feature_hog(features, labels):
    list_hog_fd = []
    for feature in features:
        fd = hog(feature.reshape((28, 28)),
                 orientations=9,
                 pixels_per_cell=(14, 14),
                 cells_per_block=(1, 1),
                 block_norm='L2-Hys')
        list_hog_fd.append(fd)
    hog_features = np.array(list_hog_fd, 'float64')
    return hog_features


def dump_clf(name_pkl, hog_features, labels):
    clf = LinearSVC()
    clf.fit(hog_features, labels)
    joblib.dump(clf, name_pkl, compress=3)


def classify(name_pkl):
    way = os.getcwd() + os.sep
    way += '../../db_images/handwritten_digits/test/'
    testing = os.listdir(way)
    clf = joblib.load(name_pkl)

    for test in testing:
        path = way + test
        im = cv2.imread(path)
        cv2.imshow('Digits Original', im)
        cv2.waitKey(200)
        cv2.destroyAllWindows()

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Original Gray', gray)
        cv2.waitKey(200)
        cv2.destroyAllWindows()

        for _ in range(5):
            gray = cv2.GaussianBlur(gray, (21, 21), 0.5)
            cv2.imshow('GaussianBlur Gray', gray)
        cv2.waitKey(200)
        cv2.destroyAllWindows()

        ret, im_th = cv2.threshold(gray,
                                   0,
                                   255,
                                   cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        cv2.imshow('THRESH_BINARY_INV and THRESH_OTSU', im_th)
        cv2.waitKey(200)
        cv2.destroyAllWindows()

        im2, cnts, hierarchy = cv2.findContours(im_th,
                                                cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)

        rects = map(lambda cnt: cv2.boundingRect(cnt), cnts)

        for rect in rects:

            leng = int(rect[3] * 1.)
            pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
            pt2 = int(rect[0] + rect[2] // 2 - leng // 2)

            vector_predict = []
            for ntr in [cv2.INTER_NEAREST,
                        cv2.INTER_AREA,
                        cv2.INTER_LINEAR,
                        cv2.INTER_CUBIC,
                        cv2.INTER_LANCZOS4]:

                roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
                roi = cv2.resize(roi, (28, 28), interpolation=ntr)

                cv2.imshow("Roi", roi)
                cv2.waitKey(100)
                cv2.destroyAllWindows()

                roi_hog_fd = hog(roi,
                                 orientations=9,
                                 pixels_per_cell=(14, 14),
                                 cells_per_block=(1, 1),
                                 block_norm='L2-Hys')

                vector_predict.append(
                    clf.predict(np.array([roi_hog_fd], 'float64')))

            nbr = Counter([v[0] for v in vector_predict]).most_common()
            print(nbr)
            nbr = nbr[0]

            cv2.rectangle(im,
                          (rect[0], rect[1]),
                          (rect[0] + rect[2], rect[1] + rect[3]),
                          (0, 255, 0),
                          1)

            cv2.putText(im,
                        str(int(nbr[0])),
                        (rect[0], rect[1]),
                        cv2.FONT_HERSHEY_DUPLEX,
                        1,
                        (0, 255, 255),
                        1)

        cv2.imshow("Resulting Image with Rectangular ROIs", im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    name_pkl = 'digits_clf.pkl'
    dataset = 'mnist-original'

    features, labels = loader_data(dataset)
    hog_features = feature_hog(features, labels)
    if not os.path.exists(name_pkl):
        dump_clf(name_pkl, hog_features, labels)
    classify(name_pkl)


if __name__ == "__main__":
    main()
