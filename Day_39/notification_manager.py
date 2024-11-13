import os
import smtplib
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

    def send_email(self, users, price, departure_date, arrival_date, departure, arrival, city):
        for user in users:
            username = user["name"] + " " + user["lastName"]
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user="giorgi.mikautadze2223@gmail.com", password=os.getenv("MY_EMAIL_SECRET_PASSWORD"))
                connection.sendmail(
                    from_addr="giorgi.mikautadze2223@gmail.com",
                    to_addrs=user["email"],
                    msg=f"Subject:Cheap, Flight ALERT!\n\nHello, {username}.\nCheap flight to {city}.\nDeparture date: {departure_date} from {departure}.\nArrival date: {arrival_date} to {arrival}.\nFor only {price}EUR!"
                )