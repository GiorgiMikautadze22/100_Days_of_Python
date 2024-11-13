import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        self.token = self.get_amadeus_token()

    load_dotenv()

    def get_destination_code(self, city:str):
        params = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }

        headers = {
            "Authorization": "Bearer " + self.token
        }
        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities", params=params, headers=headers)
        data = response.json()["data"][0]["iataCode"]
        return data

    def get_amadeus_token(self):
        body = {
            "grant_type": "client_credentials",
            "client_id": os.getenv("AMADEUS_API_KEY"),
            "client_secret": os.getenv("AMADEUS_SECRET")
        }

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)
        data = response.json()
        token = data["access_token"]

        return token

    def get_flight_offers(self, row):
        headers = {
            "Authorization": "Bearer " + self.token
        }

        tomorrow = datetime.now() + timedelta(days=1)

        query = {
            "originLocationCode": "TBS",
            "destinationLocationCode": row["iataCode"],
            "departureDate": tomorrow.strftime("%Y-%m-%d"),
            "adults": 1,
            "max": "10",
            "maxPrice": row["lowestPrice"]
        }

        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers",params=query, headers=headers)
        data = response.json()
        return data