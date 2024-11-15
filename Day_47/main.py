from pprint import pprint
from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url="https://www.amazon.com/dp/B0DLHDCN6P/ref=fs_a_mbt2_us0", headers=header)


soup = BeautifulSoup(response.text, "html.parser")
# Check you are getting the actual Amazon page back and not something else:
print(soup)
# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen")
print(price)

# Amazon has anti-scraping measures, so I can not get the price of the product.