from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
# from predict import predict
import numpy as np

app = Flask(__name__)

# Route for the index page 
@app.route("/", methods=['GET', 'POST'])
def index(name=None):
    # get frame here
    if request.method == 'GET':
        return render_template('index.html', name=name,count=5)
    else:
        # This is where we can handle the POST request to pytorch
        print("Request made: " + request.method)
        print("Not implemented yet")
        
        return render_template('index.html', name=name,count=10)

# @app.route(/api)