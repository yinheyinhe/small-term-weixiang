# -*- coding: utf-8 -*-
'''
Convolutional Neural Network
'''

# Importing the Keras libraries and packages
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers.convolutional import Conv2D
from tensorflow.python.keras.layers.convolutional import MaxPooling2D
from tensorflow.python.keras.layers.core import Activation
from tensorflow.python.keras.layers.core import Flatten
from tensorflow.python.keras.layers.core import Dense
#from keras.layers import Dropout
from tensorflow.python.keras import backend as K


class LeNet:
    @staticmethod
    def build(input_shape_width, input_shape_height, classes, 
              weight_path = '', input_shape_depth = 3):
        '''
        weight_path: a .hdf5 file. If exists, we can load model.
        '''
        
        # initialize the model
        model = Sequential()
        
        input_shape = (input_shape_height, input_shape_width, 
                       input_shape_depth)
        # if we are using "channels first", update the input shape
        if K.image_data_format() == 'channels_first':
             input_shape = (input_shape_depth, input_shape_height, 
                            input_shape_width)
        
        # first Convolution + relu + pooling layer
        model.add(Conv2D(filters = 20, kernel_size = (5, 5), 
                         padding = 'same', input_shape = input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size = (2, 2), strides=(2, 2)))
        
        # second convolutional layer
        model.add(Conv2D(filters = 50, kernel_size = (5, 5), 
                         padding = 'same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        
        # Flattening
        model.add(Flatten())

        # Full connection
        model.add(Dense(units = 500))
        model.add(Activation('relu'))

        # output layer
        model.add(Dense(units = classes))
        model.add(Activation('softmax'))

        if weight_path:
            model.load_weights(weight_path)

        # return the constructed network architecture
        return model
