# import smtplib
import time
from datetime import datetime
import requests

MY_LAT = 4.796063
MY_LONG = 7.031308

my_email = "missbellumspython@gmail.com"
password = "dpuhxzwdbfzlddao"


def is_close():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()

    data1 = response1.json()

    iss_longitude = float(data1["iss_position"]["longitude"])
    iss_latitude = float(data1["iss_position"]["latitude"])

    iss_position = (iss_longitude, iss_latitude)
    print(iss_position)
    print(MY_LAT, MY_LONG)

    # Leave room for margin of error
    if MY_LAT - 5 <= iss_latitude <= MY_LONG + 5 and MY_LONG - 5 <= iss_longitude <= MY_LAT + 5:
        return True


def is_night():
    param = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=param)
    response.raise_for_status()

    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    rise_split = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    set_split = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise, sunset)
    print(rise_split, set_split)

    time_now = datetime.now().hour
    # print(time_now.hour)

    if time_now >= set_split or time_now <= rise_split:
        # it's night
        return True


if is_close() and is_night():
    print("Big Baby GGGGG, Look Up!")

while True:
    time.sleep(60)
    if is_close() and is_night():
        # connection = smtplib.SMTP("http.gmail.com")
        # connection.starttls()
        # connection.login(user=my_email, password=password)
        # connection.sendmail(from_addr=my_email,
        #                     to_addrs=my_email,
        #                     msg="Subject: Look UP!\n\nThe ISS is above you! Look to the Sky!")
        # connection.close()
