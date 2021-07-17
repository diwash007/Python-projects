import smtplib
import random
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

today = dt.datetime.now()

my_email = os.environ['email']
pas = os.environ['pass']

emails = "diwashdahal75@gmail.com"

if today.weekday() == 5:
	# Getting quotes
	with open("quotes.txt") as f:
		quotes = f.readlines()
		quote = random.choice(quotes)

	# sending mail
	with smtplib.SMTP("smtp.gmail.com") as con:
		con.starttls()
		con.login(user=my_email, password=pas)
		con.sendmail(
			from_addr=my_email,
			to_addrs=emails,
			msg=f"subject:Powerful Motivation Quote\n\n{quote}"
			)
		print(quote)
else:
	print("Not monday")