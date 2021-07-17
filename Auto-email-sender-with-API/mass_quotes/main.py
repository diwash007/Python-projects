import smtplib
import os
import requests
import html
import pandas
# from dotenv import load_dotenv
import email.message

# load_dotenv()
my_email = os.environ['email']
pas = os.environ['pass']

def get_quotes():
	response = requests.get(url="https://zenquotes.io/api/today")
	response.raise_for_status()
	quotes = response.json()
	quote = quotes[0]["q"]
	author = quotes[0]["a"]
	return (quote, author)

def send_mail(quote_author):
	data = pandas.read_csv("data.csv")
	data_list = data.to_dict(orient="records")
	msg = email.message.Message()

	msg.add_header('Content-Type','text/html')
	msg.set_payload(f'<h3>{html.unescape(quote_author[0])}</h3><p style="text-align:right"><b>-{quote_author[1]}')

	for d in data_list:
		if d['email'] == d['email']:
			msg['From'] = "Good Morning!!"
			msg['Subject'] = "Quote for the day"

			with smtplib.SMTP("smtp.gmail.com") as con:
				con.starttls()
				con.login(user=my_email, password=pas)
				con.sendmail(msg['From'], d['email'], msg.as_string())
				print(f"Email sent to {d['name']}")

		else:
			print(f"""No email address of {d["name"]}""")

quote_author = get_quotes()
send_mail(quote_author)
