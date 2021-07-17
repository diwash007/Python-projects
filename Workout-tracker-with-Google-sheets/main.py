import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
today = datetime.now()
NENDPOINT = os.environ["NENDPOINT"]
SENDPOINT = os.environ["SENDPOINT"]
NUTRI_KEY = os.environ.get('NUTRI_KEY')
NUTRI_ID = os.environ.get('NUTRI_ID')
GENDER = os.environ.get('GENDER')
WEIGHT_KG = os.environ.get('WEIGHT_KG')
HEIGHT_CM = os.environ.get('HEIGHT_CM')
AGE = os.environ.get('AGE')
BEARER = os.environ["BEARER"]

# fetching exercise details
headers = {
	"x-app-id" : NUTRI_ID,
	"x-app-key" : NUTRI_KEY
}
params = {
	"query" : input("Tell me what you did today: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=NENDPOINT, headers=headers, json=params)
data = response.json()

# Adding data to sheets
auth_headers = {
	"Authorization" : BEARER
}
for item in data['exercises']:
	workout = {
	"workout" : {
		"date" : f"{today.strftime('%d/%m/%Y')}",
		"time" : f"{today.strftime('%H:%M:%S')}",
		"exercise" : item["name"].title(),
		"duration" : item["duration_min"],
		"calories" : item["nf_calories"],
		}
	}
	response = requests.post(url=SENDPOINT, headers=auth_headers, json=workout)
	print(response)
