import time
from datetime import datetime
import requests

MY_LAT = 4.796063
MY_LONG = 7.031308
api_key = "5495071f8c400ca3cc072afee6f32899"


param = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast/daily', params=param)
response.raise_for_status()
weather_data = response.json()
weather_hour = weather_data["hour"]
print(weather_data)
