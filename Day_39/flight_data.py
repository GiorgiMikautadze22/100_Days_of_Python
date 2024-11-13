class FlightData:
    #This class is responsible for structuring the flight data.
    def find_cheapest_flight(self, flight_data):
        cheapest_flight = {}
        for index in range(0, len(flight_data)):
            if cheapest_flight == {}:
                cheapest_flight = flight_data[index]
            elif cheapest_flight["price"]["grandTotal"] < flight_data[index]["price"]["grandTotal"]:
                cheapest_flight = flight_data[index]

        return cheapest_flight