from pprint import pprint
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

DESIRED_PRICE = 60
url = "https://www.amazon.com/CHESONA-Keyboard-Detachable-Adjustable-Landscape/dp/B0D4GY64TQ/ref=pd_ci_mcx_mh_mcx_views_0_title?pd_rd_w=S27Uo&content-id=amzn1.sym.bb21fc54-1dd8-448e-92bb-2ddce187f4ac%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=bb21fc54-1dd8-448e-92bb-2ddce187f4ac&pf_rd_r=WN9XY3Q3GDA7XXVM4PKF&pd_rd_wg=YaZ1s&pd_rd_r=0792a9d3-a734-40bd-a3a3-71f39206bc1d&pd_rd_i=B0D4GY64TQ"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").getText().split("$")[1]
title = soup.find(class_="productTitle").getText()
print(price)

if float(price) < DESIRED_PRICE:
    #send email
    message = f"{title} is for sale at {price}"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

# NOTE: On some product Amazon has anti-scraping measures, so I can not get the price of the product.