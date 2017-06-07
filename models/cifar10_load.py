# Benjamin Ramirez Jun 5, 2017
# loading saved CIFAR10 models and evaluating on an image from the web
import numpy as np
import os

from keras.datasets import cifar10
from keras.utils import np_utils
from keras.models import model_from_json
from keras import backend as K


# modules for loading images
from PIL import Image
import requests
from io import BytesIO

url = "http://khanhxnguyen.com/wp-content/uploads/2017/03/mnist-2.png"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
image = image.resize((32, 32))
image = image.convert(mode="RGB")
image.show()


K.set_image_dim_ordering('th')
# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
# load data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
# reshape to be [samples][pixels][width][height]
print(X_train.shape[1:])
X_train = X_train.reshape(X_train.shape[0], 3, 32, 32).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 3, 32, 32).astype('float32')
# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255
# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]


# again, this section is taken from Jason Brownlee's tutorial on saving/loading keras models
# http://machinelearningmastery.com/save-load-keras-deep-learning-models/
# loading json and creating models from saved files
json_file = open('./model_saves/cifar10_cnn_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new models
loaded_model.load_weights('./model_saves/cifar10_cnn_model.h5')
print("Loaded models from disk")

# evaluate models and compare results to trained models:
loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

test_input_image = X_test[0]
print(test_input_image.shape)

test_img = Image.fromarray(test_input_image, 'HSV')
test_img.show()

# expanded_dim_img = np.expand_dims(np_image, axis=0) /255
output_test = loaded_model.predict(np.expand_dims(test_input_image, axis=0))
print("Prediction for X[0]:", np.argmax(output_test))

scores = loaded_model.evaluate(X_test, y_test, verbose=0)
print("Large CNN Error: %.2f%%" % (100-scores[1]*100))

