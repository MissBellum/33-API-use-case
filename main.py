from datetime import *
import requests
import os

# to store environment variables, include no whitespace and no string quotation marks
# NUTRI_API_ID=14e1598d
# NUTRI_API_kEY=09bc12dbf72c5e4cbe5a69f9539c6078
# NUTRI_URL=https://trackapi.nutritionix.com/v2/natural/exercise
# SHEETY_TOKEN=w23e4r5t6y7u8i90op
# SHEETY_URL=https://api.sheety.co/ca13296e0e9115923ef170cb5b901350/trackMyWorkouts/workouts

NUTRI_API_ID = os.environ.get("NUTRI_API_ID")
NUTRI_API_kEY = os.environ["NUTRI_API_kEY"]
NUTRI_URL = os.environ["NUTRI_URL"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
SHEETY_URL = os.environ["SHEETY_URL"]

nutri_headers = {

    "x-app-id": NUTRI_API_ID,
    "x-app-key": NUTRI_API_kEY,
    "Content-Type": "application/json"
}
get_workout = input("How much work did you put in? ")

nutri_config = {

    "query": get_workout,
    "gender": "female",
    "weight_kg": "60",
    "height_cm": "167.64",
    "age": 23
}

response = requests.post(url=NUTRI_URL, json=nutri_config,
                         headers=nutri_headers)
result = response.json()
print(result)

headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    'Content-Type': 'application/json'
}

today = datetime.now().strftime("%a|%d|%b|%Y")
time_now = datetime.now().strftime("%X")
print(today, time_now)

for exercise in result["exercises"]:
    sheet_config = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response1 = requests.post(url=SHEETY_URL, json=sheet_config, headers=headers)
    print(response1.text)
