from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

# Keep Chrome browser running after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/app/recs") # Open the website url

def click_element(x_path):
    try:
        element = driver.find_element(By.XPATH, value=x_path)
        element.click()
    except NoSuchElementException:
        time.sleep(2)
        element = driver.find_element(By.XPATH, value=x_path)
        element.click()

# Log in
click_element('//*[@id="u-825090168"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
click_element('//*[@id="u1741496052"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]')

# Change window to Facebook window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = driver.find_element(By.NAME, value="email")
email_input.send_keys("giorgi.mikautadze@live.com")

password_input = driver.find_element(By.NAME, value="pass")
password_input.send_keys("10Aa56335")
password_input.send_keys(Keys.ENTER)

#Fb Continue as notification
click_element('/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]')

driver.switch_to.window(base_window)

# Pop ups
time.sleep(3)
click_element('/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]/div[2]')
click_element('/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]')

for _ in range(100):
    # Click swipe left
    time.sleep(1)
    click_element('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')