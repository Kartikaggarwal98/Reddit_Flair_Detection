from flask import Flask, request, render_template,send_from_directory, jsonify
from prediction import predict
import os,json

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

@app.route('/automated_testing', methods=['POST'])
def handle_form():
	print("Posted file: {}".format(request.files['file']))
	file = request.files['file']
	urls = file.read().decode("utf-8").split('\n')
	json_dict={}
	for url in urls:
		flairName, trueFlair = predict(url)
		json_dict[url]=flairName

	json_object = json.dumps(json_dict, indent = 4)
	with open("output.json", "w") as outfile: 
		outfile.write(json_object) 

	return send_from_directory(directory='.',filename='output.json', as_attachment=True)
	
if __name__ == "__main__":
	app.run(debug=True)