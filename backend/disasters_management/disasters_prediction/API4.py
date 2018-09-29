import requests as req
from pprint import pprint
import json


def get_weather(lat, lon):
    api_address = 'https://samples.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b6907d289e10d714a6e88b30761fae22' 

    url = api_address.format(lat, lon)
    json_data = req.get(url).json()
    
    weather = {
        "min_temp" : json_data['main']["temp_min"],
        "max_temp" : json_data['main']["temp_max"],
        "sea_level" : json_data['main']["sea_level"],
        "wind_speed" : json_data['wind']["speed"]

    }
    
    return weather
    





