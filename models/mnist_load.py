# Benjamin Ramirez Jun 3, 2017
# loading saved mnist models and evaluating
import numpy as np
import os
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import model_from_json
from keras import backend as K
# modules for loading images
from PIL import Image
import requests
from io import BytesIO


def init_from_save(json_file, hd5_file):
    json_data = open(json_file, 'r').read()
    model = model_from_json(json_data)
    model.load_weights(hd5_file)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def np_array_greyscale(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((28, 28))
    image = image.convert(mode="L")
    np_image = np.array(image)
    # reshape image array for input to model
    np_image = np.expand_dims(np_image, axis=0)
    np_image = np.expand_dims(np_image, axis=0)
    # normalize pixel values
    np_image = np_image / 255
    return np_image


def test_model_output():
    url = "http://khanhxnguyen.com/wp-content/uploads/2017/03/mnist-2.png"
    np_image = np_array_greyscale(url)

    K.set_image_dim_ordering('th')
    # fix random seed for reproducibility
    seed = 7
    np.random.seed(seed)

    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape(X_train.shape[0], 1, 28, 28).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], 1, 28, 28).astype('float32')

    X_train = X_train / 255
    X_test = X_test / 255

    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)
    num_classes = y_test.shape[1]

    # again, this section is taken from Jason Brownlee's tutorial on saving/loading keras models
    # http://machinelearningmastery.com/save-load-keras-deep-learning-models/
    # evaluate models and compare results to results from training:
    mnist_json = './model_saves/mnist_cnn_model.json'
    mnist_hd5 = './model_saves/mnist_cnn_model.h5'
    mnist_model = init_from_save(json_file=mnist_json, hd5_file=mnist_hd5)

    output_test = mnist_model.predict(np_image)
    print("Prediction for X[0]:", np.argmax(output_test))

    scores = mnist_model.evaluate(X_test, y_test, verbose=0)
    print("Large CNN Error: %.2f%%" % (100 - scores[1] * 100))


if __name__ == "__main__":
    test_model_output()
