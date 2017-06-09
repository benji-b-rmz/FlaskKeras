# Benjamin Ramirez June 6, 2017
# loading a cnn models from json and hd5 files
# then communicating with it through a Flask API
from flask import Flask, request, render_template
# keras/tensorflow and cnn modules
import numpy as np
import os
from models.mnist_load import load_model_from_save, np_array_from_image
# modules for creating/working with images from URL
from PIL import Image
import requests
from io import BytesIO

# creating the cnn_model which will handle image input
mnist_json = './models/model_saves/mnist_cnn_model.json'
mnist_hd5 = './models/model_saves/mnist_cnn_model.h5'
mnist_model = load_model_from_save(mnist_json, mnist_hd5)


def classify_image(input_url):
    print(input_url)
    try:
        np_image = np_array_from_image(input_url)
        model_prediction = np.argmax(mnist_model.predict(np_image))
        print(model_prediction)
        return model_prediction.__str__()
    except:
        return "check your url"

# the Flask Web Application code #

app = Flask(__name__)


@app.route('/api/mnist', methods=['POST'])
def classify():
    input_url = request.data.decode(encoding='UTF-8')
    return classify_image(input_url)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
