# Benjamin Ramirez June 6, 2017
# loading a cnn models from json and hd5 files
# then communicating with it through a Flask API
from flask import Flask, request, render_template
# keras/tensorflow and cnn modules
import numpy as np
import os
import json
from models import mnist_load, cifar10_load

# modules for creating/working with images from URL
from PIL import Image
import requests
from io import BytesIO

# creating the cnn_model which will handle image input
mnist_json = './models/model_saves/mnist_cnn_model.json'
mnist_hd5 = './models/model_saves/mnist_cnn_model.h5'
mnist_model = mnist_load.init_from_save(mnist_json, mnist_hd5)

cifar10_json = './models/model_saves/cifar10_cnn_model.json'
cifar10_hd5 = './models/model_saves/cifar10_cnn_model.h5'
cifar10_model = cifar10_load.init_from_save(cifar10_json, cifar10_hd5)

# refactor the duplicate code for mnist and cifar10
def mnist_classify(input_url):
    print(input_url)
    try:
        np_image = mnist_load.np_array_greyscale(input_url)
        model_prediction = mnist_model.predict(np_image)
        print(model_prediction)
        response_json = {'probabilities': model_prediction[0].__str__(),
                         'prediction': np.argmax(model_prediction).__str__()}
        return json.dumps(response_json)
    except:
        return "check your url"

def cifar10_classify(input_url):
    print(input_url)
    try:
        np_image = cifar10_load.np_array_rgb(input_url)
        model_prediction = np.argmax(cifar10_model.predict(np_image))
        print(model_prediction)
        response_json = {'probabilities': model_prediction[0].__str__(),
                         'prediction': np.argmax(model_prediction).__str__()}
        return json.dumps(response_json)
    except:
        return "check your url"


# the Flask Web Application code #

app = Flask(__name__)


@app.route('/api/mnist', methods=['POST'])
def mnist_api():
    input_url = request.data.decode(encoding='UTF-8')
    return mnist_classify(input_url)


@app.route('/api/cifar10', methods=['POST'])
def cifar10_api():
    input_url = request.data.decode(encoding='UTF-8')
    return cifar10_classify(input_url)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    # this keras model seems to have problems when run ing debug=True mode
    app.run()
