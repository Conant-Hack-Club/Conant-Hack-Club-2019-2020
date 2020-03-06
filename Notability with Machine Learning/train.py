import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
import matplotlib.pyplot as plt
import cv2
import os
from sklearn.model_selection import train_test_split

#tf version: 1.8.0
#keras version: 2.1.5

K.set_image_dim_ordering('th') #sets depth, input_depth, rows, columns for the convolutional neural network


X = []
y = []

X = np.array(X)
y = np.array(y)

X = X.reshape(X.shape[0], 1, 45, 45).astype('float32') #3d array

# normalize inputs from 0-255 to 0-1
X = X / 255

y = np_utils.to_categorical(y)
num_classes = y.shape[1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)


