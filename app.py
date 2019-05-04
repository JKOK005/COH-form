from flask import Flask, render_template, request, abort
import os

app = Flask(__name__)

@app.route('/')
def render_form_template():
	if request.method == "GET":
		app.logger.debug("Rendering main form")
		return render_template('form.html')
	else: 
		abort(404)

@app.route('/heart-beat')
def heart_beat():
	return 1