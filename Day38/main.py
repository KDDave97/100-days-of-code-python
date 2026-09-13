import requests
from datetime import datetime
import os

nutrition_endpoint = "https://app.100daysofpython.dev"
sheety_endpoint = "https://api.sheety.co/817ce8ad97d8b1875048494a4448e4f2/udemyWorkoutsSheet/workouts"

headers = {
    "nutrition":{
        "x-app-id": os.environ.get("NUT_APP_ID"),
        "x-app-key": os.environ.get("NUT_API_KEY")
    },
    "sheety":{
        "Authorization": f"Bearer {os.environ.get("NUT_APP_ID")}"
    }
}

nutrition_params = {
    "query": input("What excercise you did? "),
    "weight_kg": 70,
    "height_cm": 177,
    "age": 29,
    "gender": "male"
}

post_exercise = f"{nutrition_endpoint}/v1/nutrition/natural/exercise"

response = requests.post(url=post_exercise, json=nutrition_params, headers=headers["nutrition"])
result = response.json()

today = datetime.now()
duration = result["exercises"][0]["duration_min"]
exercise = result["exercises"][0]["name"].title()
calories = result["exercises"][0]["nf_calories"]

sheety_params = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": "15:00:00",
        "duration": duration,
        "exercise": exercise,
        "calories": calories
    }
}

response = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers["sheety"])