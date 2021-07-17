import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

class DataManager:
	def __init__(self):
		self.link = os.environ["SENDPOINT"]
		self.auth_headers = {
			"Authorization" : os.environ["BEARER"]
		}
	def get_data(self):
		response = requests.get(url=self.link, headers=self.auth_headers)
		data = response.json()
		return data['price']

	def insert_codes(self, code, id):
		codes = {
			"price" : {
				"iataCode" : code,
			}
		}
		response = requests.put(url=f"{self.link}/{id}", headers=self.auth_headers, json=codes)
		print(f"Succesfully inserted IATA code {code}")