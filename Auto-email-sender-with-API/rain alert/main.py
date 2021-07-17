import requests

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
will_rain = False

parameters = {
	"lat" : 26.678829,
	"lon" : 87.967003,
	"appid" : "ID",
	"exclude" : "current,minutely,daily"
}
response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
data = response.json()

rain_data = [ "will_rain" for i in range(0,12) if data["hourly"][i]["weather"][0]["id"] < 700]

if "will_rain" in rain_data:
	print("Bring an Umbrella") 