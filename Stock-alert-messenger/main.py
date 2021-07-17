import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
SKEY=os.environ.get('skey')
NKEY=os.environ.get('nkey')
FROM=os.environ.get('from')
TO=os.environ.get('to')

# getting stock data
parameters = {
	"function" : "TIME_SERIES_DAILY_ADJUSTED",
	"symbol" : STOCK,
	"apikey" : SKEY,
}
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
data = response.json()
yesterday = float(list(data["Time Series (Daily)"].items())[0][1]["5. adjusted close"])
older = float(list(data["Time Series (Daily)"].items())[1][1]["5. adjusted close"])

change = yesterday-older
changePercent = change*100/older

if abs(change) > 0.05*older:
	# getting news
	parameters = {
	"apiKey" : NKEY,
	"q" : COMPANY_NAME,
	}
	response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
	data = response.json()

	news_title = [data["articles"][i]["title"] for i in range(0,3)]
	news_brief = [data["articles"][i]["description"] for i in range(0,3)]

	# sending messages
	account_sid = os.environ['TWILIO_ACCOUNT_SID']
	auth_token = os.environ['TWILIO_AUTH_TOKEN']
	client = Client(account_sid, auth_token)

	for i in range(0,3):
		if change > 0:
			icon = "🔺"
		else:
			icon = "🔻"
		msg = f"""TSLA: {icon}2%
				Headline: {news_title[i]}
				Brief: {news_brief[i]}
				"""
		message = client.messages \
		                .create(
		                     body=msg,
		                     from_=FROM,
		                     to=TO
		                 )
		print(message.sid)