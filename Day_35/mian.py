import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
api_url = os.getenv("API_URL")

parameters = {
    "q": "Tbilisi",
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url=api_url, params=parameters)
response.raise_for_status()
data = response.json()
weather_data = data["list"]
will_rain = False

for data in weather_data:
    condition_code = int(data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True
        break

if will_rain:
    account_sid = os.getenv("ACCOUNT_ID")
    auth_token = os.getenv("SMS_AUTH_TK")
    client = Client(account_sid, auth_token)

    # For phone number
    message = client.messages.create(
        messaging_service_sid=os.getenv("MESSAGE_ID"),
        body='Today is going to rain so take the umbrella',
        to=os.getenv("MY_PHONE_NUMBER")
    )

    # For whatsApp
    # message = client.messages.create(
    #     from_=f"whatsapp:{os.getenv("TW_PHONE_NUMBER")}",
    #     content_sid=os.getenv("CONTENT_ID"),
    #     body="It's going to rain today",
    #     to=f"whatsapp:{os.getenv("MY_PHONE_NUMBER")}"
    # )
    print(message.status)
