import requests
import os
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")

MY_LAT = "47.3088349"
MY_LONG = "20.943673"

weather_parameters = {
    "lat":59.329323,
    "lon":18.068581,
    "cnt":4,
    "appid":api_key
}

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


response = requests.get(OMW_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for weather in weather_data["list"]:
    weather_id = weather["weather"][0]["id"]
    if weather_id > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="sms_account_alerts",
        to="TO_PHONE_NUMBER",
        from_="FROM_TWILIO_NUMBER")
print(message.status)

