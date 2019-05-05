import os

# Define all configuration variables for the app as environment variables
APP_REDIS_URL 	= os.getenv("APP_REDIS_URL", "localhost")
APP_REDIS_PORT 	= os.getenv("APP_REDIS_PORT", 6379)

COH_API_KEY 	= os.getenv("COH_API_KEY", "")
COH_BASE_URL 	= os.getenv("COH_BASE_URL", "localhost")

COH_FORM_SUBMIT = COH_BASE_URL + "/staging/v1/believers"
COH_CHURCHES 	= COH_BASE_URL + "/staging/v1/churches"