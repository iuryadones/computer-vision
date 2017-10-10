# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from skimage import exposure
from skimage import feature
from imutils import paths
import argparse
import imutils
import cv2

#modo de usar
#python car_logo.py --training car_logos --test test_images 

# construct the argument parse and parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--training", required=True, help="Path to the logos training dataset")
ap.add_argument("-t", "--test", required=True, help="Path to the test dataset")
args = vars(ap.parse_args())
 
# initialize the data matrix and labels
print("[INFO] extracting features...")
data = []
labels = []

# loop over the image paths in the training set
for imagePath in paths.list_images(args["training"]):
    # extract the make of the car
    make = imagePath.split("/")[-2]

    # load the image, convert it to grayscale, and detect edges or binarize

    ######[CODE HERE]#######
    img = cv2.imread(imagePath, 0)
    gray = img
    ######[END CODE]#######

    # find contours in the edge map, keeping only the largest one which
    # is presumed to be the car logo

    #####[CODE HERE]#######
    ret,thresh = cv2.threshold(gray,127,255,0)
    im2,cnts,hierarchy = cv2.findContours(thresh, 1, 2)
    c = max(cnts, key=cv2.contourArea)
    #####[END CODE]#######

     
    # extract the logo of the car and resize it to a canonical width
    # and height
    (x, y, w, h) = cv2.boundingRect(c)
    logo = gray[y:y + h, x:x + w]
    logo = cv2.resize(logo, (200, 100))

    # extract Histogram of Oriented Gradients from the logo
    #####[CODE HERE]#######
    (H, hogImage) = feature.hog(logo, orientations=9, pixels_per_cell=(10,10), cells_per_block=(2,2), transform_sqrt=True, visualise=True) 

    #####[END CODE]#######
    # update the data and labels
    data.append(H)
    labels.append(make)

# "train" the nearest neighbors classifier
print("[INFO] training classifier...")
model = KNeighborsClassifier(n_neighbors=1)
model.fit(data, labels)
print("[INFO] evaluating...")

for imagePath in paths.list_images(args["test"]):
    # load the test image, convert it to grayscale, and resize it to
    # the canonical size
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    logo = cv2.resize(gray, (200, 100))

    # extract Histogram of Oriented Gradients from the test image and
    # predict the make of the car
    (H, hogImage) = feature.hog(logo, orientations=9, pixels_per_cell=(10, 10),
            cells_per_block=(2, 2), transform_sqrt=True, visualise=True)
    pred = model.predict(H.reshape(1, -1))[0]

    # visualize the HOG image
    hogImage = exposure.rescale_intensity(hogImage, out_range=(0, 255))
    hogImage = hogImage.astype("uint8")
    cv2.imshow("HOG Image", hogImage)

    # draw the prediction on the test image and display it
    cv2.putText(image, pred.title(), (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
            (0, 255, 0), 3)
    cv2.imshow("Test Image", image)
    cv2.waitKey(0)
