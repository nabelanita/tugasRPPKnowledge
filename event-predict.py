from flask import Flask
from flask import render_template, request, redirect

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from keras.models import load_model


app = Flask(__name__)  # Create application object

df = pd.read_csv('dataeventfix.csv')

@app.route('/')
def index():
	return render_template('index.html', tables=[df.to_html(index=False)], titles=[''])

def predict():
  ##TODO: import model, return model
	n_input = 6
	length = df['jumlah'].shape[0]
	model = load_model('regressor_model.h5')
	pred_arr = []

	enter = np.array(df['jumlah'])[length-n_input:length]
	out = model.predict(enter.reshape((1, n_input)), verbose=0)
	pred_arr.append(math.floor(out))

	for i in range (59):  
		enter = np.delete(enter, [0])
		enter = np.append(enter, values=out)

		out = model.predict(enter.reshape((1, n_input)), verbose=0)
		if (out < 0):
			out = 0
		pred_arr.append(math.floor(out))

	return pred_arr
	

@app.route('/predict/<id>')
def prediction(id):
	result = predict()
	idx = int(id)
	prediction = result[idx]
	month_id = idx % 12
	year = idx // 12 + 2020

	month = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

	return render_template('prediction.html',month=month[month_id],year=year,prediction=prediction)

@app.route('/handle_data', methods=['POST'])
def handle_data():
	month = request.form['month']
	year = request.form['year']

	idx = (int(month) - 1) + (int(year) - 2020) * 12

	return redirect('/predict/'+str(idx))
	
if __name__ == '__main__':
	app.run(debug=True)  # Run our application