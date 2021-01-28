import requests
from pprint import pprint

TOKEN = "33655c93c2msh4578a20b4f74438p123895jsnf551913e72b9"


URL = "https://community-open-weather-map.p.rapidapi.com/weather"

def ask_weather(city):
    querystring = {
        "q": city,
        "units": "metric",
    }

    headers = {
        'x-rapidapi-key': TOKEN,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.get(URL, headers=headers, params=querystring)

    print(response.url)
    data = response.json()
    return data["main"]["feels_like"]

while True:
    city = input("Enter a city: ")
    print(ask_weather(city))
