import requests 
from pprint import pprint
import json

## IA State ##
api_address='https://samples.openweathermap.org/data/2.5/weather?lat=41.6005448&lon=-93.6091064&appid=b6907d289e10d714a6e88b30761fae22'

json_data = requests.get(api_address).json()

format_add = json_data['main']

print(json_data['main']["temp_min"])
print(json_data['main']["temp_max"])
print(json_data['main']["sea_level"])
print(json_data['wind']["speed"])
