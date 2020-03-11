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
import pandas as pd
import random

#tf version: 1.8.0
#keras version: 2.1.5

K.set_image_dim_ordering('th') #sets depth, input_depth, rows, columns for the convolutional neural network

raw_data = pd.read_csv("emnist-letters-train.csv")

all_X = raw_data.values[:,1:]
all_y = raw_data.values[:,0]

all_X = np.array(all_X)
all_y = np.array(all_y)

X = all_X.reshape(all_X.shape[0], 1, 28, 28).astype('float32') #3d array
y = all_y

#displays random letters
for i in range(15):
    index = random.randint(0, len(all_X) - 1)
    random_letter = all_X[index].reshape(28, 28, 1).astype('float32') #3d array

    random_letter = cv2.rotate(random_letter, cv2.ROTATE_90_CLOCKWISE)
    random_letter = cv2.flip(random_letter, 1)

    random_letter = cv2.resize(random_letter, (400, 400))
    cv2.imshow("image", random_letter)
    print(chr(64 + all_y[index]))
    cv2.waitKey(0)

# normalize inputs from 0-255 to 0-1
X = X / 255

y = np_utils.to_categorical(y)
num_classes = y.shape[1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)


