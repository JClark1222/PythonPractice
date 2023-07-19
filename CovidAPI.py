import requests
import pip._vendor.requests
import json


response = requests.get('https://api.covid19india.org/state_district_wise.json')
data = response.text
print(data)
parse_json = json.dumps(data, sort_keys= True)
active_cases = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print("Active cases in South Andaman: ", active_cases)
