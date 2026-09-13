import requests
from datetime import datetime

USERNAME = "NAME"
TOKEN = "TOKEN"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

grapgh_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=grapgh_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.5"
}

graph_1 = f"{graph_endpoint}/{grapgh_config["id"]}"

# response = requests.post(url=f"{graph_endpoint}/{grapgh_config["id"]}", json=pixel_data, headers=headers)
# print(response.text)

pixel_update = {
    "quantity": "8.6"
}

# response = requests.put(url=f"{graph_1}/{pixel_data["date"]}", json=pixel_update, headers=headers)
# print(response.text)

response = requests.delete(f"{graph_1}/{pixel_data["date"]}", headers=headers)
print(response.text)