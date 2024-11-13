#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
import data_manager
import time
import notification_manager
import flight_data

search_flight = FlightSearch()
manager = data_manager.DataManager()
alert = notification_manager.NotificationManager()
flight_structure = flight_data.FlightData()

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

    flight_data = search_flight.get_flight_offers(row)
    if flight_data["meta"]["count"] >= 1:

        cheapest_flight = flight_structure.find_cheapest_flight(flight_data["data"])

        departure_date = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["at"]
        arrival_date = cheapest_flight["itineraries"][0]["segments"][-1]["arrival"]["at"]
        departure = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        arrival = cheapest_flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
        price = cheapest_flight["price"]["grandTotal"]
        city = row["city"]
        alert.send_notification(price=price, departure_date=departure_date, arrival_date=arrival_date, departure=departure, arrival=arrival, city=city)
    else:
        print("No flight found")

