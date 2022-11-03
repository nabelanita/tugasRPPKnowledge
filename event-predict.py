from flask import Flask
from flask import render_template

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from keras.models import load_model


app = Flask(__name__)  # Create application object

@app.route('/')
def index():
	return render_template('index.html')

def predict():
  ##TODO: import model, return model
	n_input = 6
	df = pd.read_csv('dataeventfix.csv')
	length = df['jumlah'].shape[0]
	model = load_model('regressor_model.h5')
	pred_arr = []

	enter = np.array(df['jumlah'])[length-n_input:length]
	out = model.predict(enter.reshape((1, n_input)), verbose=0)
	pred_arr.append(math.floor(out))

	for i in range (23):  
		enter = np.delete(enter, [0])
		enter = np.append(enter, values=out)

		out = model.predict(enter.reshape((1, n_input)), verbose=0)
		if (out < 0):
			out = 0
		pred_arr.append(math.floor(out))

	return pred_arr

	
	

@app.route('/predict')
def result():
	## TODO predict using model in predict(), display result
	result = predict()
	print(result)

	return render_template('results.html',prediction=result)



if __name__ == '__main__':
	app.run(debug=True)  # Run our application