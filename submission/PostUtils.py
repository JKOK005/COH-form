import requests
import os
from ..settings import *

class PostUtils(object):
	@classmethod
	def dispatch(cls, form_data):
		# Dispatch form informatin over to server implementation
		return requests.codes.ok 

	@classmethod
	def churches(cls):
		# API calls to server to get church lists
		# Thereafter, caches information in redis
		pass