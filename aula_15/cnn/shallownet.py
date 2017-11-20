# import the necessary packages
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras import backend as K

class ShallowNet:
    @staticmethod
    def build(width, height, depth, classes):

        # define the  CONV => RELU > FC => Softmax CNN
        #[CODE HERE]
        model = Sequential()
        inputShape = (height, width, depth)

        model.add(Conv2D(32, (3,3), padding='same', input_shape=inputShape))
        model.add(Activation('relu'))
        model.add(Flatten())
        model.add(Dense(classes))
        model.add(Activation('softmax'))

        # return the constructed network architecture
        return model


