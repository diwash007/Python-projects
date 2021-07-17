import os
import requests
import json
from datetime import datetime,timedelta
from flight_data import FlightData
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
	def __init__(self):
		self.headers = {
		"apikey" : os.environ["kiwiapi"]
		}
	def get_codes(self, city):
		params = {
			"term" : city
		}
		response = requests.get(url=os.environ["kiwiurl"], headers=self.headers, params=params)
		data = response.json()
		return data["locations"][0]["code"]

	def get_info(self, code):
		today = datetime.now()
		params = {
			"fly_from" : "LON",
			"fly_to" : code,
			"date_from" : (today+timedelta(days=1)).strftime("%d/%m/%Y"),
			"date_to" : (today+timedelta(days=181)).strftime("%d/%m/%Y"),
			"nights_in_dst_from" : 7,
			"nights_in_dst_to" : 28,
			"fly_type" : "round",
			"one_for_city" : 1,
			"max_stopovers": 0,
			"curr": "GBP"
			}
		response = requests.get(url=os.environ["flightsearch"], headers=self.headers, params=params)
		
		try:
			data = response.json()["data"][0]
		except IndexError:
			print(f"No flights found for {code}")
			return None
			
		flight_data = FlightData(
			price=data["price"],
			origin_city=data["route"][0]["cityFrom"],
			origin_airport=data["route"][0]["flyFrom"],
			destination_city=data["route"][0]["cityTo"],
			destination_airport=data["route"][0]["flyTo"],
			out_date=data["route"][0]["local_departure"].split("T")[0],
			return_date=data["route"][1]["local_departure"].split("T")[0]
			)
		print(f"{flight_data.destination_city}: £{flight_data.price}")
		return flight_data