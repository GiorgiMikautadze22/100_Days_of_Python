from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time

# Keep Chrome browser running after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, value="cookie")
cookie.click()

now = datetime.now()
five_minutes_later = now + timedelta(minutes=1)

start = datetime.now()

def check_for_upgrades():
    can_buy = []
    store = driver.find_elements(By.CSS_SELECTOR, value="#store div")

    for item in store:
        if item.get_attribute("class") == "":
            can_buy.append(item)

    if can_buy:
        can_buy[-1].click()


while datetime.now() <= five_minutes_later:
    every_five_seconds = start + timedelta(seconds=5)
    if every_five_seconds < datetime.now():
        check_for_upgrades()
        start = datetime.now()

    time.sleep(0.05)
    cookie.click()

cps= driver.find_element(By.ID, value="cps")
print(cps.text)
driver.quit()
