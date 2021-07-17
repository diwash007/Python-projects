import requests
from datetime import datetime
import time
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.environ['email']
pas = os.environ['pass']

LATITUDE = 26.678829
LONGITUDE = 87.967003

def is_iss_up():
	response = requests.get(url="http://api.open-notify.org/iss-now.json")
	response.raise_for_status()
	data = response.json()

	iss_latitude = float(data["iss_position"]["latitude"])
	iss_longitude = float(data["iss_position"]["longitude"])

	if abs(iss_latitude - LATITUDE) <= 5 and abs(iss_longitude - LONGITUDE) <= 5:
		return True
	
def is_night():
	parameters = {
	    "lat": LATITUDE,
	    "lng": LONGITUDE,
	    "formatted": 0,
	}
	response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
	response.raise_for_status()
	data = response.json()
	sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
	sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
	time_now = datetime.now()
	if time_now.hour >= sunset:
		return True

while True:
	if is_iss_up() and is_night():
		with smtplib.SMTP("smtp.gmail.com") as con:
			con.starttls()
			con.login(user=my_email, password=pas)
			con.sendmail(
				from_addr=my_email,
				to_addrs="diwashdahal75@gmail.com",
				msg="Subject:Look Up!!\n\nLook Up to iss!",
				)
			print("Email sent!!")
	time.sleep(60)