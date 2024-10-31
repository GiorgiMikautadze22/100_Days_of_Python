# import smtplib
#
# my_email = "giorgi.mikautadze2223@gmail.com"
# password = "wjqi gdge uyed ikah" # This is app password that we need to create for accessing
# # our account without using real password. This is required for security reasons.
#
# # Host should be same Email provider we are using.
# # Google uses port 587 for security measures. Some provider might use other ports.
# # We need to open connection, and after we are done close the connection.
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#
#     # TLS is for security. If our mail is intercepted then it will be encrypted.
#     connection.starttls()
#
#     # Log in to our account
#     connection.login(user=my_email, password=password)
#
#     # Send mail
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="mikautadze.giorgi2223@gmail.com",
#         msg="Subject:Hello\n\nThis is body text"
#     )

import random
import datetime as dt
import smtplib

now = dt.datetime.now()
week_of_day = now.weekday()

if week_of_day == 3:
    with open(file="quotes.txt", mode='r') as file:
        data = file.readlines()
        random_quote = random.choice(data)

    my_email = "giorgi.mikautadze2223@gmail.com"
    password = "wjqi gdge uyed ikah"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mikautadze.giorgi2223@gmail.com",
            msg=f"Subject:Quote\n\n{random_quote}"
        )