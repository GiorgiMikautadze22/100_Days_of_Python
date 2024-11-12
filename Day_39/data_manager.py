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
        response = requests.get(url="https://api.sheety.co/59d0cd834a456796b7c66fb3e08a7d9b/flightDeals/sheet1", headers=headers)
        data = response.json()["sheet1"]
        return data

    def update_iata_code(self, row):
        headers = {
            "Authorization": "Bearer " + os.getenv("SHEETY_BEARER_TOKEN")
        }
        params = {
            "sheet1": row
        }
        api_url = f"https://api.sheety.co/59d0cd834a456796b7c66fb3e08a7d9b/flightDeals/sheet1/" + str(row["id"])
        response = requests.put(url=api_url,
                                headers=headers,
                                json=params
                                )
        print(response.text)