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


if __name__ == '__main__':
	app.run(debug=True)  # Run our application