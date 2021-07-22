import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

email = 
passd = 
YOUR_EMAIL= 
TARGET=800.0
url = "https://www.amazon.com/Acer-i5-9300H-GeForce-Keyboard-AN515-54-5812/dp/B086KJBKDW"
headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; rv:90.0) Gecko/20100101 Firefox/90.0",
	"Accept-Language" : "en-US,en;q=0.5"
}

response = requests.get(url, headers=headers)
data = response.content

soup = BeautifulSoup(data, "lxml")

price = soup.find(class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice")
price = float(price.getText().strip(" $"))

if price < TARGET:
	with smtplib.SMTP("smtp.gmail.com") as con:
		con.starttls()
		con.login(user=email,password=passd)
		con.sendmail(
			from_addr=email,
			to_addrs=YOUR_EMAIL,
			msg=f"Subject:price nigga \n\nPrice dropped to {price}")