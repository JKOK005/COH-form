from flask import Flask, render_template, request, redirect, url_for
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
	try:
		form_data = request.form
		resp_code = PostUtils.dispatch(form_data=form_data)
		if resp_code == req.codes.ok:
			return url_for("post_form_submission", is_success=True, code=resp_code)
		else:
			raise Exception("Form submission failed with code {0}".format(resp_code))
	except Exception as ex:
		print(ex)
		return url_for("post_form_submission", is_success=False, code=req.codes.bad_request)

@app.route('/form-status')
def post_form_submission():
	is_success = request.args["is_success"]
	code = request.args["code"]
	return render_template('post_submission.html', is_success=is_success, code=code)

@app.route('/heart-beat')
def heart_beat():
	return 1