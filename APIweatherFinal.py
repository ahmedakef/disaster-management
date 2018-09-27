import requests 
from pprint import pprint
import json



api_address='https://samples.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b6907d289e10d714a6e88b30761fae22'


lat = input("latitude of the city: ")
lat=float(lat)
lon = input("longtuide of the city: ")
lon=float(lon)
state = ""
if (lat== 41.619549 and lon==-93.598022) or (lat== 43.002316 and lon==-89.424095) or (lat== 40.666149 and  lon== -89.580101) or (lat== 45.560230 and lon==-94.172852):
    
    if lat== 41.619549 and lon==-93.598022:
        state='IA'
    elif   lat== 43.002316 and lon==-89.424095 :
        state='WI'
    elif  lat== 40.666149 and lon== -89.580101:
        state='IL'   
    elif  lat== 45.560230 and lon==-94.172852:
        state='MN'
    
    url = api_address.format( lat, lon)

    json_data = requests.get(url).json()
 
    min_temp = json_data['main']["temp_min"]
    max_temp = json_data['main']["temp_max"]
    sea_level = json_data['main']["sea_level"]
    wind_speed = json_data['wind']["speed"]
