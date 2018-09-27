import urllib3, requests, json
import APIweatherFinal
from backend_handler import BackendHandler  

# retrieve your wml_service_credentials_username, wml_service_credentials_password, and wml_service_credentials_url from the
# Service credentials associated with your IBM Cloud Watson Machine Learning Service instance

wml_credentials={
"password": "6474d6e5-d34b-406f-aa61-78c57f23df16",
  "url": "https://us-south.ml.cloud.ibm.com",
  "username": "8fac2350-a183-460d-8efc-35a1567bb818"
}

headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
url = '{}/v3/identity/token'.format(wml_credentials['url'])
response = requests.get(url, headers=headers)
mltoken = json.loads(response.text).get('token')

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line


array_of_values_to_be_scored = [APIweatherFinal.state, None , APIweatherFinal.min_temp, APIweatherFinal.max_temp, APIweatherFinal.sea_level, None , None,  None, APIweatherFinal.wind_speed, None ]
another_array_of_values_to_be_scored = [APIweatherFinal.state, None , APIweatherFinal.min_temp, APIweatherFinal.max_temp, APIweatherFinal.sea_level, None , None,  None, APIweatherFinal.wind_speed, None ]
payload_scoring = {"fields": ["State", "Start Date", "min temperature(F)", "max temperature(F)", "Mean sea level pressure(IN)", "mean dew point(F)", "Total precipitation(IN)", "visibility(MI)", "Mean wind speed(MPH)", "max sustained wind speed(MPH)"], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/e57f2229-3fda-4e56-a902-f746bcbe466a/deployments/72bd12f3-ee64-4d33-9034-28f3f611aab6/online', json=payload_scoring, headers=header)
print("Scoring response")
#print(json.loads(response_scoring.text))

parsed = json.loads(response_scoring.text)
for value in parsed['values']:
  prediction = value[-3]
  print("The prediction is: ", prediction)

if prediction > 0.5:
  disaster = {
        "diameter": 1000,
        "level_of_danger": "D",
        "lat"	:	APIweatherFinal.lat,
        "lang"	:	APIweatherFinal.lon
    }
  response = BackendHandler.create_disaster(**disaster)
  print(response)



 