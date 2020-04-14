import os
import sys

# Flask
from flask import Flask, flash, redirect, url_for, request, render_template, Response, jsonify, redirect

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.python.keras.backend import set_session


# Some utilites
import numpy as np
from util import base64_to_pil


# Declare a flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


MODEL_PATH = 'models/model.h5'



sess = tf.Session()
graph = tf.compat.v1.get_default_graph()

set_session(sess)
model = load_model(MODEL_PATH)



def model_predict(img, model):
    global graph,sess
    img = img.reshape((1,*img.shape))
    print(img.shape)
    # img = cv2.imread(img)
    with graph.as_default():
        set_session(sess)
        preds = model.predict(img)
    print(preds)

    preds = 'Malign' if preds >= 0.5 else 'Benign'
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    global model
    if request.method == 'POST':
        img = base64_to_pil(request.json)
        
        return jsonify(result = model_predict(img,model))


if __name__ == '__main__':
    app.run(port=5000,debug = True)
