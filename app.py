from flask import Flask, render_template, request
from submission.PostUtils import PostUtils
import os
import requests as req

app = Flask(__name__)

@app.route('/', methods=["GET"])
def render_form_template():
	app.logger.debug("Rendering main form")
	return render_template('form.html')

@app.route('/form-submission', methods=["POST"])
def submit_form():
	form_data = request.json
	resp = PostUtils.dispatch(form_data=form_data)
	if resp == req.codes.ok:
		return render_template('post_submission.html')
	else:
		return render_template('post_submission.html')

@app.route('/heart-beat')
def heart_beat():
	return 1