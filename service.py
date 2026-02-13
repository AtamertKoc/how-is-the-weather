import requests

def weather_status(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "status": data["weather"][0]["description"],
            "moisture": data["main"]["humidity"],
        }
    else:
        return None