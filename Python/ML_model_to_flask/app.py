# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:12:23 2024

@author: Piyus
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)

# load pcikle model
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    
    return render_template("index.html",prediction_text = "The flower species is {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)