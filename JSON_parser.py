#2019,1/02, AM 10:50, by Queenie Chen

import json
from urllib.request import urlopen

ipAddr = '50.78.253.58'
response = urlopen('http://freegeoip.net/json/'+ipAddr).read().decode('utf-8')
responseToJson = json.loads(response)
print(responseToJson.get('country_code'))
