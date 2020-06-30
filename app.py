import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html", page_title="Home")

@app.route('/about')
def about():
	return render_template("about.html", page_title="About Us")

@app.route('/services')
def services():
	return render_template("services.html", page_title="Services")

@app.route('/testomonials')
def testomonials():
	data = []
	with open("data/about.json", "r") as json_data:
		data = json.load(json_data)
	return render_template("testomonials.html", page_title="Testomonials", about=data)

	
	
if __name__ == '__main__':
	app.run(host=os.environ.get('IP'),
					port=os.environ.get('PORT'),
					debug=True)