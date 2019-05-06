import requests
import os
import settings
import logging
import json

class PostUtils(object):
	logger = logging.getLogger("PostUtils")

	@classmethod
	def dispatch(cls, form_data):
		# Dispatch form information over to server implementation
		headers = {
			"APIKey" : settings.COH_API_KEY
		}

		body = {
			"Believers" : [
				{
					"LanguageType" 			: form_data["preferred_language"],
					"RallyTime" 			: form_data["rally_attended"],
					"FirstName" 			: form_data["name"],
					"LastName"				: form_data["surname"],
		            "Gender"				: form_data["gender"],
		            "AgeGroup" 				: form_data["age_group"],
		            "MobileNumber"			: form_data["phone_no"],
		            "EmailAddress" 			: form_data["email"],
		            "DecisionMade"			: form_data["decision_made"],
		            "HomePostalCode"		: form_data["postal_code"],
		            "NameOfFriend" 			: form_data["person_who_invited"],
		            "FriendContactNumber" 	: "",
		            "FriendChurchName" 		: form_data["church_of_person_who_invited"],
		            "AdditionalComments" 	: form_data["message"]
				}
			]
		}

		resp = requests.post(settings.COH_FORM_SUBMIT, data=json.dumps(body), headers=headers)
		cls.logger.debug("POST with headers: {0}, data {1}".format(body, headers))
		cls.logger.info("Submitted with response: {0}".format(resp.content))
		return resp.status_code

	@classmethod
	def churches(cls):
		# API calls to server to get church lists
		# Thereafter, caches information in redis
		pass