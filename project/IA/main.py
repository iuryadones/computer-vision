from collections import Counter
import os

from skimage.feature import hog
from sklearn.datasets.mldata import fetch_mldata
from sklearn.externals import joblib
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
import cv2
import numpy as np
import pylab as plt
import multiprocessing as mp


def loader_data(origin):
    dataset = fetch_mldata(origin, data_home='./train')
    features = np.array(dataset.data, 'int64')
    labels = np.array(dataset.target, 'int8')
    print("Count of digits in dataset", Counter(labels))

    return features, labels

def descriptor_hog(attr):
    im_th = np.array(attr[0].reshape((28,28)), dtype='float64')
    plt.imsave(f'{os.getpid()}.png', im_th, cmap='Greys')

    img = cv2.imread(f'./{os.getpid()}.png',)

    grey = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

    ret, im_th = cv2.threshold(grey,
                               0,
                               255,
                               cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    im2, cnts, hierarchy = cv2.findContours(im_th,
                                            cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)

    rects = map(lambda cnt: cv2.boundingRect(cnt), cnts)
    rects = sorted(rects, key=lambda r: -r[3])

    for rect in rects:

        leng = int(rect[3] * 1.)
        pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
        pt2 = int(rect[0] + rect[2] // 2 - leng // 2)

        vector_predict = []
        for ntr in [cv2.INTER_AREA]:
            roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
            roi = cv2.resize(roi, (28, 28), interpolation=ntr)
            return hog(roi, **attr[1])

def feature_hog(features, labels):
    kwargs = {
        'orientations': 9,
        'pixels_per_cell': (8, 8),
        'cells_per_block': (3, 3),
        'block_norm': 'L2-Hys',
        'transform_sqrt': True
    }

    pool = mp.Pool(8)
    result_hog = pool.map(
        descriptor_hog,
        ((feature, kwargs) for feature in features),
    )
    pool.close()
    pool.join()

    return np.array(result_hog, dtype='float64')


def dump_clf(name_pkl, hog_features, labels):
    print('Start trainng')
    clf = LinearSVC()
    clf.fit(hog_features, labels)
    print('End trainng')
    print('Start Dump')
    joblib.dump(clf, name_pkl, compress=3)
    print('End Dump')

def imshow(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def pipeline_process_image(src, args):
    if not args:
        return src.copy()
    pipe = args.pop(0)
    src = pipe[0](src.copy(), **pipe[1])
    return pipeline_process_image(src.copy(), args)

def classify(name_pkl):
    way = os.getcwd() + os.sep
    way += '../../db_images/handwritten_digits/test/'
    testing = os.listdir(way)
    clf = joblib.load(name_pkl)

    paths = [(way + test) for test in testing]

    for path in paths:
        img = cv2.imread(filename=path)

        imshow(img)

        pipe_args = [
            (cv2.cvtColor, dict(code=cv2.COLOR_BGR2GRAY)),
            (cv2.GaussianBlur, dict(ksize=(5, 5), sigmaX=0.0)),
            (cv2.medianBlur, dict(ksize=3)),
        ]

        result = pipeline_process_image(img, pipe_args)

        imshow(result)

        ret, im_th = cv2.threshold(result,
                                   0,
                                   255,
                                   cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        imshow(im_th)

        im2, cnts, hierarchy = cv2.findContours(im_th,
                                                cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)

        rects = map(lambda cnt: cv2.boundingRect(cnt), cnts)
        rects = sorted(rects, key=lambda r: r[0])

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

                roi_hog_fd = hog(roi,
                                 orientations=9,
                                 pixels_per_cell=(8, 8),
                                 cells_per_block=(3, 3),
                                 block_norm='L2-Hys',
                                 transform_sqrt=True)

                pred = clf.predict(np.array([roi_hog_fd], 'float64'))
                vector_predict.append(pred)
                print(pred)

            nbr = Counter([v[0] for v in vector_predict]).most_common()
            print(nbr)
            nbr = nbr[0]

            cv2.rectangle(img,
                          (rect[0], rect[1]),
                          (rect[0] + rect[2], rect[1] + rect[3]),
                          (0, 255, 0),
                          1)

            cv2.putText(img,
                        str(int(nbr[0])),
                        (rect[0], rect[1]),
                        cv2.FONT_HERSHEY_DUPLEX,
                        1,
                        (0, 255, 255),
                        1)

            imshow(img)


def main(trainnig=False):
    name_pkl = 'digits_clf.pkl'
    dataset = 'mnist-original'

    if trainnig:
        features, labels = loader_data(dataset)
        hog_features = feature_hog(features, labels)
        dump_clf(name_pkl, hog_features, labels)

    classify(name_pkl)

if __name__ == "__main__":
    main(False)
