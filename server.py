from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template("index.html")

@app.route('/string')
def string():
	return("hello")

if __name__ == '__main__':
	app.run()