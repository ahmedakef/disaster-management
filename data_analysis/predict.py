import urllib3, requests, json
 


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

array_of_values_to_be_scored = ['IA','6/11/1953',71.1,88,30.1,71.3,0,8.1,12.08,17.26]
another_array_of_values_to_be_scored =  ['IA','6/11/1953',71.1,88,30.1,71.3,0,8.1,12.08,17.26]

payload_scoring = {"fields": ["State", "Start Date", "min temperature(F)", "max temperature(F)", "Mean sea level pressure(IN)", "mean dew point(F)", "Total precipitation(IN)", "visibility(MI)", "Mean wind speed(MPH)", "max sustained wind speed(MPH)"], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/e57f2229-3fda-4e56-a902-f746bcbe466a/deployments/72bd12f3-ee64-4d33-9034-28f3f611aab6/online', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))




'''parsed = json.loads(response_scoring.text)
#print(len(payload_scoring))
for value in parsed['values']:
    fields = value[:30]
    #confidence = value[32]
    prediction = value[13]
    values = value[:]
    print("\n Prediction of flood: {}\n\tprediction: {}\n\tFields {}".format(prediction,zip(prediction, values), fields) )'''