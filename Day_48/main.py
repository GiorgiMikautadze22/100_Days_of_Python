from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser running after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/") # Open the website url

menu = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li")
# a_tag = driver.find_element(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li a")
# a_tag.click()

# Find link elements by their values
# all_portals = driver.find_element(By.LINK_TEXT, value="PyConAU 2024")
# all_portals.click()

# Find input by their name
search = driver.find_element(By.NAME, value="q")
search.send_keys("Gela")
search.send_keys(Keys.ENTER)

# event_dic = {}
#
# for index in range(len(menu)):
#     time = menu[index].text.split()[0]
#     name = ' '.join(menu[index].text.split()[1:])
#
#
#     item = {
#         "time" : time,
#         "name" : name
#     }
#     event_dic[index] = item
#
# print(event_dic)


# driver.find_element(By.XPATH, value='//*[@id="CardInstance63NKsSe51ywHHZqLjEjPaQ"]/div[1]/h2/span/span[2]')


# driver.quit() # Quit the Browser
# driver.close() # Close the tab