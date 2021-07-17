import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
	def __init__(self):
		self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
		self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
		self.client = Client(self.account_sid, self.auth_token)

	def send_message(self,data):
		""" sends messages """
		msg = f"""Low price alert!
					Only {data.price} to fly from
					{data.origin_city}-{data.origin_airport}
					to {data.destination_city}-{data.destination_airport},
					from {data.out_date} to {data.return_date}
					"""
		message = self.client.messages \
					.create(
					     body=msg,
					     from_=os.environ['from'],
					     to=os.environ['to']
					)
		print(message.sid)