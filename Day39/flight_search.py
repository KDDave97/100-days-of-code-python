import requests
import os


class FlightSearch:
    def __init__(self):
        self.api_key = os.environ.get("FLIGHTS_API")

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "engine": "google_flights",
            "api_key": self.api_key,
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1"
        }

        response = requests.get(url="https://app.100daysofpython.dev/v1/flights/search", params=params)
        data = response.json()
        return data