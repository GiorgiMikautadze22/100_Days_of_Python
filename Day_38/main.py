import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

headers = {
    "x-app-id": os.getenv("NUTRITIONX_APP_ID"),
    "x-app-KEY": os.getenv("NUTRITIONX_API_KEY")
}

user_input = input("Tell me which exercise you did?: ")

body = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=os.getenv("BASE_API_URL"), json=body, headers=headers)
response.raise_for_status()
data = response.json()

# Sheety request
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheety_body = {
        "sheet1": {
            "date": today,
            "time": time,
            "exercise": exercise['user_input'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    print(sheety_body)

    sheety_response = requests.post(url=os.getenv("SHEETY_API_URL"), json=sheety_body)
    print(sheety_response.text)
    sheety_response.raise_for_status()