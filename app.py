from flask import Flask, request, render_template
from prediction import predict
import os

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

@app.route('/getFlair', methods=['POST', 'GET'])
def predictFlair():
	if request.method=='POST':
		x = request.form['getUrl']
		flairName, trueFlair = predict(x)
		return  render_template('predict.html', flair=flairName,trueFlair=trueFlair)
	
if __name__ == "__main__":
	app.run(debug=True)