import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47.316631
MY_LONG = 20.922060

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }

    sunrise_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sunrise_response.raise_for_status()
    sunrise_data = sunrise_response.json()
    sunrise = int(sunrise_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunrise_data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else: return False

def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_long = float(iss_data["iss_position"]["longitude"])

    if abs(MY_LONG - iss_long) <= 5 and abs(MY_LAT - iss_lat) <= 5:
        return True
    else: return False

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject: ISS Overhead!\n\n"
                                                                            "ISS is above you!\n"
                                                                            "Look up!")


