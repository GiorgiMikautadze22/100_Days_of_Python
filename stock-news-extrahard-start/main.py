import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("API_KEY")
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=os.getenv("API_URL"), params=params)
response.raise_for_status()
data = response.json()
dates = data["Time Series (Daily)"]
dates_list = [dates[date] for date in dates]
yesterday_data = dates_list[0]
day_after_yesterday_data = dates_list[1]


def calculate_change(new, old):
    percentage = round((new - old) / old * 100, 2)
    return percentage

change = calculate_change(float(yesterday_data["4. close"]), float(day_after_yesterday_data["4. close"]))

if change < 0:
    print(f"Decrease {abs(change)}%")
elif change > 0:
    print(f"Increase {abs(change)}%")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

year = datetime.now().year
month = datetime.now().month - 1
day = datetime.now().day

news_params = {
    "q": "tesla",
    "from": f"{year}-{month}-{day}",
    "sortBy": "publishedAt",
    "apiKey": os.getenv("NEWS_API_KEY")
}

news_response = requests.get(url=os.getenv("NEWS_API_URL"), params=news_params)
news_response.raise_for_status()
news_data = news_response.json()["articles"][0:3]
print(news_data)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

