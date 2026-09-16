from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=30 * 60)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LHR"

for destination in sheet_data:
    pprint(f"Getting flights for {destination["city"]}...")
    flights = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"], from_time=tomorrow, to_time=six_months_from_today)

    cheapest_flight = find_cheapest_flight(flights, return_date=six_months_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination["city"]}: GBP {cheapest_flight.price}")

    if cheapest_flight != "NA" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lowest price  flight found to {destination["city"]}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        print(f"Low price alert! Only GBP {cheapest_flight.price} to fly\n"
              f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}\n"
              f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}")






































#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.