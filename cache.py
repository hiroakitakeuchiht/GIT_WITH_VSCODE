import functools
import json
import requests
import time

#CHANGED

@functools.lru_cache()
def get_weather_data(city: str) -> dict[str:str]:
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&APPID=*******"
    )
    weather_data = json.loads(response.text)
    weather = weather_data["weather"][0]["main"]
    temperature = str(int(weather_data["main"]["temp"] - 273))
    return {"City": city, "Weather": weather, "Temperature": temperature}


if __name__ == "__main__":
    cities = ["Singapore", "Sydney", "Singapore", "Singapore", "Tokyo", "Singapore"]
    for city in cities:
        print(get_weather_data(city))
        print(get_weather_data.cache_info(), end="\n" * 2)
        time.sleep(1)

# Looping through a list of cities to simulate different clients using their city name as their input to get weather data
# least recently used -> remove the least recently used frame when the cache is full (when maxsize value is reached) ** Default 128
# Used when the function will be run with the same argument multiple times!
# Once cached, the function does not need to be run again -> Faster and save the number of API calls to be made
# might want to do the following every 30 minutes e.g. with multithreading in this implementation because we can get the data from 20 hours ago for example
# get_weather_data.cache_clear()
