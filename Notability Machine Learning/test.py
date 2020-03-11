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
import cv2
from keras.models import model_from_yaml

K.set_image_dim_ordering('th') #sets depth, input_depth, rows, columns for the convolutional neural network


#load the models

yaml_file = open('models/model1.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new models
loaded_model.load_weights("models/model1.h5")
print("Loaded models from disk")

loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

letter = cv2.imread("bletter.png", 0)
letter = cv2.resize(letter, (28, 28))
letter = letter.reshape((1, 1, 28, 28)).astype("float32") / 255
result = loaded_model.predict(letter)
print(result)
result = result[0]

max = np.where(result == np.amax(result))
print(np.amax(result))


