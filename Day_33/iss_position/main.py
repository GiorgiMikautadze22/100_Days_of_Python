import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 41.715137 # Your latitude
MY_LONG = 44.827095 # Your longitude
MY_EMAIL = "giorgi.mikautadze2223@gmail.com"
PASSWORD = "wjqi gdge uyed ikah"

time_now = datetime.now().hour

def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True
    else:
        return False

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if sunset <= time_now or sunrise >= time_now:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_close() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look Up\n\niss is flying above you"
            )



