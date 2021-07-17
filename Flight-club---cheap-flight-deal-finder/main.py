from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
messenger = NotificationManager()
sheet_data = data_manager.get_data()

for data in sheet_data:
	code = flight_search.get_codes(data["city"])
	
	# inputting IATA Codes into the sheets
	# if data["iataCode"] == "TESTING":
	# 	data_manager.insert_codes(code, data["id"])

	# getting flight details
	flight_data = flight_search.get_info(code)

	# sending messages
	if flight_data != None and flight_data.price < data["lowestPrice"]:
		print("yes")
		messenger.send_message(flight_data)