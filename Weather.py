import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

city = input("Enter The City Name: ")

url = "https://api.weatherapi.com/v1/current.json"

params = {
    "key": api_key,
    "q": city
}

r = requests.get(url, params=params)

wdic = r.json()

print("City:", wdic["location"]["name"])
print("Temperature:", wdic["current"]["temp_c"], "°C")
print("Condition:", wdic["current"]["condition"]["text"])