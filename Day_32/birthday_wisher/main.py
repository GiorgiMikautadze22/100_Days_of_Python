import pandas
import datetime as dt
import smtplib
import random

data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict(orient="records")

MY_EMAIL = "giorgi.mikautadze2223@gmail.com"
PASSWORD = "wjqi gdge uyed ikah"

now = dt.datetime.now()
month = now.month
day = now.day

for birthday in data_dict:
    if birthday["month"] == month and birthday["day"] == day:

        random_letter = random.randint(1,4)
        with open(f"./letter_templates/letter_{random_letter}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", birthday["name"])

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthday["email"],
                    msg=f"Subject:Happy Birthday\n\n{letter}"
                )


