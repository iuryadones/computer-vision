from imutils import paths
from scipy.io import loadmat
from skimage import io
import dlib
import cv2
import os

path = os.getcwd()+os.sep
path_sign = path + "../db_aulas/Imagens/minibases/data_101/data_101/car_side_train"
path_ann = path + "../db_aulas/Imagens/minibases/data_101/data_101/annotation/car_side"
# grab the default training options for our HOG + Linear SVM detector initialize the
# list of images and bounding boxes used to train the classifier
print("[INFO] gathering images and bounding boxes...")
options = dlib.simple_object_detector_training_options()
images = []
boxes = []

# loop over the image paths
for imagePath in paths.list_images(path_sign):
    # extract the image ID from the image path and load the annotations file
    imageID = imagePath[imagePath.rfind("/") + 1:].split("_")[1]
    imageID = imageID.replace(".jpg", "")
    p = "%s/annotation_%s.mat" % (path_ann,imageID)
    annotations = loadmat(p)["box_coord"]

    # loop over the annotations and add each annotation to the list of bounding
    # boxes
    bb = [dlib.rectangle(left=int(x), top=int(y), right=int(w), bottom=int(h))
                    for (y, h, x, w) in annotations]
    print(bb)
    boxes.append(bb)
    
    # add the image to the list of images
    images.append(cv2.imread(imagePath,0))

# train the object detector
print("[INFO] training detector...")
print(boxes)
detector = dlib.train_simple_object_detector(images, boxes, options)

# dump the classifier to file
print("[INFO] dumping classifier to file...")
detector.save('stop_sign.svm')

# visualize the results of the detector
win = dlib.image_window()
win.set_image(detector)
dlib.hit_enter_to_continue()

