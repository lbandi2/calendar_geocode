from geocode import Calendar
import os
# from dotenv import load_dotenv

# load_dotenv()

API_KEY = os.getenv('API_KEY')
CAL_ID = os.getenv('CAL_ID')

Calendar(CAL_ID, API_KEY)
