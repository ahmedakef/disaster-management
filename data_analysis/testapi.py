import requests as req
from pprint import pprint
import json


api_address = 'https://samples.openweathermap.org/data/2.5/forecast?appid=5aba5640f410444530f8355107819e82&lat={}&lon={}'
lat = input("latitude of the city: ")
lon = input("longtuide of the city: ")

url = api_address.format( lat, lon)

json_data = req.get(url).json()


for each in json_data["list"]:
    print(each["main"]["temp_min"])
    print(each["main"]["temp_max"])
    print(each["main"]["sea_level"])
    print(each["wind"]["speed"])
    print(each["rain"])
    if each.get("rain") == {}:
       rain = 0

    
