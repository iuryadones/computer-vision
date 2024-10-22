from collections import Counter
from itertools import chain, zip_longest
from pathlib import Path

import os

from skimage.feature import hog
from sklearn.datasets.mldata import fetch_mldata
from sklearn.externals import joblib
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

import cv2
import multiprocessing as mp
import numpy as np
import pylab as plt


def loader_data(origin):
    dataset = fetch_mldata(origin, data_home="./train")
    features = np.array(dataset.data, "int64")
    labels = np.array(dataset.target, "int8")
    print("Count of digits in dataset", Counter(labels))

    return features, labels


def descriptor_hog(attr):
    im_th = np.array(attr[0].reshape((28, 28)), dtype="float64")
    plt.imsave(f"{os.getpid()}.png", im_th, cmap="Greys")

    img = cv2.imread(f"./{os.getpid()}.png")

    grey = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

    ret, im_th = cv2.threshold(
        grey, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    im2, cnts, hierarchy = cv2.findContours(
        im_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    rects = map(lambda cnt: cv2.boundingRect(cnt), cnts)
    rects = sorted(rects, key=lambda r: -r[3])

    for rect in rects:

        leng = int(rect[3] * 1.)
        pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
        pt2 = int(rect[0] + rect[2] // 2 - leng // 2)

        roi = im_th[pt1 : pt1 + leng, pt2 : pt2 + leng]
        roi = cv2.resize(roi, (28, 28), interpolation=attr[1])
        return hog(roi, **attr[2])


def feature_hog(features, labels):
    kwargs = {
        "orientations": 9,
        "pixels_per_cell": (8, 8),
        "cells_per_block": (3, 3),
        "block_norm": "L2-Hys",
        "transform_sqrt": True,
    }

    hog_labels = []
    hog_results = []

    for interpolation in [
        cv2.INTER_AREA,
        cv2.INTER_BITS,
        cv2.INTER_BITS2,
        cv2.INTER_CUBIC,
        cv2.INTER_LANCZOS4,
        cv2.INTER_LINEAR,
        cv2.INTER_LINEAR_EXACT,
        cv2.INTER_MAX,
        cv2.INTER_NEAREST,
        cv2.INTER_TAB_SIZE,
        cv2.INTER_TAB_SIZE2,
    ]:
        try:
            print(interpolation)

            pool = mp.Pool(8)
            result_hog = pool.map(
                descriptor_hog,
                ((feature, interpolation, kwargs) for feature in features),
            )
            pool.close()
            pool.join()

            hog_results.append(result_hog)
            hog_labels.append(labels)
        except:
            pass

    return (
        np.array([r for r in chain(*hog_results)], dtype="float64"),
        np.array([l for l in chain(*hog_labels)]),
    )


def dump_clf(name_pkl, hog_features, labels):
    print("Start trainng", end="\n\n")

    clf = LinearSVC()
    clf.fit(hog_features, labels)

    print("End trainng")
    print("Start Dump")
    joblib.dump(clf, name_pkl, compress=3)
    print("End Dump")


def imshow(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pipeline_process_image(src, args):
    if not args:
        return src.copy()
    elif args[0][0].__name__ == "threshold":
        pipe = args.pop(0)
        _, src = pipe[0](src.copy(), **pipe[1])
    else:
        pipe = args.pop(0)
        src = pipe[0](src.copy(), **pipe[1])
    return pipeline_process_image(src.copy(), args)


def classify(name_pkl):
    clf = joblib.load(name_pkl)

    way = Path("../../db_images/handwritten_digits/test")
    # way = Path("../../db_images/captcha/test")

    way = way.resolve()

    paths = way.rglob("*.png")

    for path in paths:

        # print(path, end="\n\n")

        img = cv2.imread(filename=path.as_posix())

        # imshow(img)

        pipe_args = [
            (cv2.cvtColor, dict(code=cv2.COLOR_BGR2GRAY)),
            (cv2.GaussianBlur, dict(ksize=(3, 3), sigmaX=0.0)),
            (cv2.GaussianBlur, dict(ksize=(5, 5), sigmaX=0.0)),
            (cv2.blur, dict(ksize=(5, 5))),
            (cv2.blur, dict(ksize=(3, 3))),
            (cv2.medianBlur, dict(ksize=3)),
            (cv2.medianBlur, dict(ksize=5)),
            (
                cv2.threshold,
                dict(
                    thresh=0,
                    maxval=255,
                    type=cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU,
                ),
            ),
        ]

        result = pipeline_process_image(img, pipe_args)

        # imshow(result)

        im_th = result

        # ret, im_th = cv2.threshold(
        #     result, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        # )

        # ret, im_th = cv2.threshold(result, 127, 255, cv2.THRESH_BINARY_INV)

        # im_th = cv2.adaptiveThreshold(
        #     result,
        #     255,
        #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #     cv2.THRESH_BINARY_INV,
        #     11,
        #     2,
        # )

        # imshow(im_th)

        im2, cnts, hierarchy = cv2.findContours(
            im_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        rects = map(lambda cnt: cv2.boundingRect(cnt), cnts)
        rects = sorted(rects, key=lambda r: r[0])

        labels = []

        for rect in rects:

            leng = int(rect[3] * 1.)
            pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
            pt2 = int(rect[0] + rect[2] // 2 - leng // 2)

            vector_predict = []

            for ntr in [
                cv2.INTER_AREA,
                cv2.INTER_BITS,
                cv2.INTER_BITS2,
                cv2.INTER_CUBIC,
                cv2.INTER_LANCZOS4,
                cv2.INTER_LINEAR,
                cv2.INTER_LINEAR_EXACT,
                cv2.INTER_MAX,
                cv2.INTER_NEAREST,
                cv2.INTER_TAB_SIZE,
                cv2.INTER_TAB_SIZE2,
            ]:
                try:
                    roi = im_th[pt1 : pt1 + leng, pt2 : pt2 + leng]
                    roi = cv2.resize(roi, (28, 28), interpolation=ntr)

                    roi_hog_fd = hog(
                        roi,
                        orientations=9,
                        pixels_per_cell=(8, 8),
                        cells_per_block=(3, 3),
                        block_norm="L2-Hys",
                        transform_sqrt=True,
                    )

                    pred = clf.predict(np.array([roi_hog_fd], "float64"))
                    vector_predict.append(pred)
                    # print(pred)
                except:
                    pass

            nbr = Counter([v[0] for v in vector_predict]).most_common()

            if nbr:
                # print(nbr)

                nbr = nbr[0]
                text_label = str(int(nbr[0]))

                cv2.rectangle(
                    img,
                    (rect[0], rect[1]),
                    (rect[0] + rect[2], rect[1] + rect[3]),
                    (0, 255, 0),
                    1,
                )

                cv2.putText(
                    img,
                    text_label,
                    (rect[0], rect[1]),
                    cv2.FONT_HERSHEY_DUPLEX,
                    1,
                    (0, 255, 255),
                    1,
                )

                labels.append(str(nbr[0]))
            else:
                labels.append("#")

            # imshow(img)

        print("\nImage Classify\n")

        cls = "".join(labels)
        label_test = path.parent.name

        print(cls, len(cls))
        print(label_test, len(label_test))

        # imshow(img)

        print(f"is_correct: {cls == label_test}")
        print(f"is_lenght_equal: {len(cls) == len(label_test)}")
        print(
            f"counter_correct: {len([True for x,y in zip_longest(label_test, cls) if x == y])}"
        )
        print(
            f"counter_error: {len(label_test) - len([True for x,y in zip_longest(label_test, cls) if x == y])}",
            end="\n\n",
        )

        # imshow(img)


def main(trainnig=False):
    name_pkl = "digits_clf_inter_all.pkl"

    dataset = "mnist-original"

    if trainnig:
        features, labels = loader_data(dataset)
        hog_features, hog_labels = feature_hog(features, labels)

        dump_clf(name_pkl, hog_features, hog_labels)

    classify(name_pkl)


if __name__ == "__main__":
    main()
