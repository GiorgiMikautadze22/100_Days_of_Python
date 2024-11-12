#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
import data_manager
import time

search_flight = FlightSearch()
manager = data_manager.DataManager()

# print(search_flight.get_destination_code("Frankfurt"))

sheety_data = data_manager.DataManager().get_sheet_data()

for row in sheety_data:
    while row["iataCode"] == "":
        try:
            row["iataCode"] = search_flight.get_destination_code(row["city"])
            manager.update_iata_code(row)
            time.sleep(2)
            print(row["iataCode"])
        except KeyError:
            print("Key Error")
