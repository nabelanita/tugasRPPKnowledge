from flask import Flask
from flask import render_template

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)  # Create application object

@app.route('/')
def index():
	return render_template('index.html')

def predict():
	##TODO: import model, return model
	return 0

@app.route('/predict', method=['POST'])
def result():
	## TODO predict using model in predict(), display result
	
	return render_template('predict.html',prediction='test')



if __name__ == '__main__':
	app.run(debug=True)  # Run our application