from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def render_form_template():
	return render_template('form.html')

@app.route('/heart-beat')
def heart_beat():
	return 1