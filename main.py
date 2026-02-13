from service import weather_status
import os
from dotenv import load_dotenv
from service import weather_status

load_dotenv() 
API_KEY = os.getenv("WEATHER_API_KEY")


def start():
    city = input("Enter Your Location: ")
    weather = weather_status(city, API_KEY)
    if weather:
        print(f"---{city.upper()} for weather---")
        print(f"Temperature: {weather['temp']}°C")
        print(f"Sky: {weather['status']}")

        if weather['temp'] < 10:
            print("Weather is cold")
        elif weather['temp'] < 20:
            print("Go out weather is sweet")
        else:
            print("WHAT İS THİS MAN WEATHER VERY HOT OMG")

if __name__ == "__main__":
    start()