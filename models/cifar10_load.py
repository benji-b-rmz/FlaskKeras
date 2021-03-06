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


cifar10_json = './model_saves/cifar10_cnn_model.json'
cifar10_hd5 = './model_saves/cifar10_cnn_model.h5'


def np_array_rgb(image_url):

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((32, 32))
    image = image.convert(mode="RGB") \
        # reshape for input to model
    np_image = np.array(image)
    np_image = np_image.reshape(3, 32, 32)
    # normalize rgb values
    np_image = np_image / 255
    np_image = np.expand_dims(np_image, axis=0)
    # print(np_image.shape)
    return np_image


def init_from_save(json_file, hd5_file):
    json_data = open(json_file, 'r').read()
    model = model_from_json(json_data)
    model.load_weights(hd5_file)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def test_cifar10_model():
    K.set_image_dim_ordering('th')
    # fix random seed for reproducibility
    seed = 7
    np.random.seed(seed)
    # load data
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    # reshape to be [samples][pixels][width][height]
    X_test = X_test.reshape(X_test.shape[0], 3, 32, 32).astype('float32')
    # normalize inputs from 0-255 to 0-1
    X_test = X_test / 255
    # one hot encode outputs
    y_test = np_utils.to_categorical(y_test)

    # again, this section is taken from Jason Brownlee's tutorial on saving/loading keras models
    # http://machinelearningmastery.com/save-load-keras-deep-learning-models/
    # loading json and creating models from saved files
    cifar10_model = init_from_save(cifar10_json, cifar10_hd5)
    print("Loaded models from disk")

    # an image of a red car for testing
    url = "http://www.teckinfo.com/images/automobile_img.jpg"
    test_image = np_array_rgb(url)
    print(test_image.shape)

    output_test = cifar10_model.predict(test_image)
    print("Prediction for X[0]:", np.argmax(output_test)) # should output 1, the index for car

    scores = cifar10_model.evaluate(X_test, y_test, verbose=0)
    print("Large CNN Error: %.2f%%" % (100 - scores[1] * 100))


if __name__ == "__main__":
    test_cifar10_model()
