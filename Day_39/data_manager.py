import os
import requests
from dotenv import load_dotenv
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    load_dotenv()

    def get_sheet_data(self):
        headers = {
            "Authorization": "Bearer " + os.getenv("SHEETY_BEARER_TOKEN")
        }
        response = requests.get(url="https://api.sheety.co/59d0cd834a456796b7c66fb3e08a7d9b/flightDeals/prices", headers=headers)
        data = response.json()["prices"]
        return data

    def update_iata_code(self, row):
        headers = {
            "Authorization": "Bearer " + os.getenv("SHEETY_BEARER_TOKEN")
        }
        params = {
            "prices": row
        }
        api_url = f"https://api.sheety.co/59d0cd834a456796b7c66fb3e08a7d9b/flightDeals/prices/" + str(row["id"])
        response = requests.put(url=api_url,
                                headers=headers,
                                json=params
                                )
        print(response.text)

    def get_costumer_list(self):
        headers = {
            "Authorization": "Bearer " + os.getenv("SHEETY_BEARER_TOKEN")
        }
        response = requests.get(url="https://api.sheety.co/59d0cd834a456796b7c66fb3e08a7d9b/flightDeals/users",
                                headers=headers)
        data = response.json()["users"]
        return data