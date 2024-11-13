import os

from twilio.rest import Client
from dotenv import load_dotenv
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    load_dotenv()

    def send_notification(self, price, departure, arrival, departure_date,arrival_date, city):
        account_sid = os.getenv("TWILIO_ID")
        auth_token = os.getenv("TWILIO_TOKEN")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            messaging_service_sid=os.getenv("TWILIO_SERVICE_ID"),
            body=f'Low price alert! Cheap flight to {city}.\nDeparture date: {departure_date} from {departure}.\nArrival date: {arrival_date} to {arrival}.\nFor only {price}€!',
            to='+995571058206'
        )
        print(message.status)