import requests
import os

header = {
    "Authorization": f"Bearer {os.environ.get("NUT_APP_ID")}"
}

sheety_endpoint = "https://api.sheety.co/817ce8ad97d8b1875048494a4448e4f2/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint, headers=header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price":{
                "lowestPrice": new_price
            }
        }
        requests.put(url=f"{sheety_endpoint}/{row_id}", json=new_data, headers=header)