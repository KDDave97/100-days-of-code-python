import requests
import os

header = {
    "Authorization": f"Bearer {os.environ.get("NUT_APP_ID")}"
}

sheety_endpoint = "https://api.sheety.co/817ce8ad97d8b1875048494a4448e4f2/flightDeals/prices"


class DataManager:
    def __init__(self):
        response = requests.get(url=sheety_endpoint, headers=header)
        self.data = response.json()