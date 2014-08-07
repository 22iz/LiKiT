import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def likit():
	return render_template('likit.html')

if __name__ == '__main__':
	app.run(debug=True)