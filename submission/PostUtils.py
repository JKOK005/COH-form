import requests
import os

class PostUtils(object):
	@classmethod
	def dispatch(cls, form_data):
		# Dispatch form informatin over to server implementation
		return requests.codes.ok 