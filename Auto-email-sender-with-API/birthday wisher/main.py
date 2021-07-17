import datetime as dt 
import smtplib
import pandas
import random
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.environ['email']
pas = os.environ['pass']

today = dt.datetime.now()
month = today.month
day = today.day

data = pandas.read_csv("birthdays.csv")
data_list = data.to_dict(orient="records")

for data in data_list:
	if month == data["month"] and day == data["day"]:
		letter_id = random.randint(1,3)

		with open(f"letter_templates/letter_{letter_id}.txt") as f:
			message = f.read()
			message = message.replace("[NAME]", data['name'])
		
		with smtplib.SMTP("smtp.gmail.com") as con:
			con.starttls()
			con.login(user=my_email, password=pas)
			con.sendmail(
				from_addr=my_email,
				to_addrs=data["email"],
				msg=f"subject:Happy Birthday {data['name']}!\n\n{message}"
				)
			print(f"Email sent to {data['name']}")


