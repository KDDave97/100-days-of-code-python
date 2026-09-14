from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=30 * 60)

sheety_data = DataManager()

flight_search = FlightSearch()
pprint(flight_search.check_flights("LHR", "CDG", tomorrow, six_months_from_today))




































#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.