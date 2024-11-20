import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

website_html = requests.get(url="https://appbrewery.github.io/Zillow-Clone/").text
soup = BeautifulSoup(website_html, "html.parser")
price_list = [price.text.replace("/mo", "").split("+")[0] for price in soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")]
street_list = [street.text.strip() for street in soup.find_all(name="address")]
link_list = [link.get("href") for link in soup.find_all(class_="property-card-link")]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdPR5d1kbMFmdrvpkWBGtlpQ50RT5BNslISVqQJbW-FI-sp6w/viewform?usp=sf_link") # Open the website url

for index in range(len(price_list[0:10])):
    time.sleep(1)
    address = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address.send_keys(f"{street_list[index]}")

    price = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(f"{price_list[index]}")

    link = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(f"{link_list[index]}")

    send = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')
    send.click()

    time.sleep(1)

    new_form = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_form.click()