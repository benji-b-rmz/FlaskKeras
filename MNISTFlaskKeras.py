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

# testing using model for classifying an image from URL

# url = "http://khanhxnguyen.com/wp-content/uploads/2017/03/mnist-2.png"
# np_image = np_array_from_image(url)
#
# mnist_model.predict(np.expand_dims(np.expand_dims(np_image, axis=0), axis=0))
# Function for creating an image from the URL


# the Flask Web Application code #

app = Flask(__name__)

@app.route('/api/mnist', methods=['POST'])
def classify():

    return 42

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
