from secrets import json_secret
from geocode import Calendar

API_KEY = json_secret('google', 'api_key')
CAL_ID = json_secret('calendar', 'id')

Calendar(CAL_ID, API_KEY)
