import os
import requests
from datetime import datetime

TOKEN = os.environ.get('TOKEN')
USER = os.environ.get('USER')
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
graph_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs"
data_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs/graph1"
headers = {
	"X-USER-TOKEN" : TOKEN
	}
today = datetime.now()
date = f"{today.strftime('%Y%m%d')}"

# creating user account
user_params = {
	"token": TOKEN,
	"username" : USER,
	"agreeTermsOfService" : "yes",
	"notMinor" : "yes",
}
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

# creating a graph
graph_params = {
	"id" : "graph1",
	"name" : "Time waste graph",
	"unit" : "Min",
	"type" : "int",
	"color" : "momiji"
}
response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

# adding data
data_params = {
	"date" : date,
	"quantity": "78"
}
response = requests.post(url=data_endpoint, json=data_params, headers=headers)
print(response.text)

# updating data
put_endpoint = f"{data_endpoint}/{date}"
put_params = {
	"quantity" : input("How much time today?")
}
response = requests.put(url=put_endpoint, json=put_params, headers=headers)
print(response.text)

# deleting data
del_endpoint = f"{data_endpoint}/{date}"
response = requests.delete(url=del_endpoint, headers=headers)
print(response.text)
