import os
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

user_params = {
    "token": os.getenv("TOKEN"),
    "username": os.getenv("USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Create User
# response = requests.post(url=os.getenv("CREATE_USER_ENDPOINT"), json=user_params)
# print(response.text)


# Create graph
header = {
    "X-USER-TOKEN": os.getenv("TOKEN")
}

graph_body = {
    "id": "graph1",
    "name": "Reading Tracker",
    "unit": "Page",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=os.getenv("CREATE_GRAPH_ENDPOINT"), json=graph_body, headers=header)
# print(response.text)

# Add Pixel to the graph

today = datetime(year=2024, month=11, day=6)
formated_date = today.strftime("%Y%m%d")


pixel_body = {
    "date": formated_date,
    "quantity": "5"
}

# response = requests.post(url=os.getenv("CREATE_PIXEL_ENDPOINT"), json=pixel_body, headers=header)
# print(response.text)

# Update a pixel
update_endpoint = os.getenv("CREATE_PIXEL_ENDPOINT") + f"/{formated_date}"
print(update_endpoint)

update_pixel = {
    "quantity": "30"
}

# response = requests.put(url=update_endpoint, json=update_pixel, headers=header)
# print(response.text)

# Delete pixel
response = requests.delete(url=update_endpoint, headers=header)
print(response.text)