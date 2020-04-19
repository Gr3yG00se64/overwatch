import json

#API SETUP

api_data= {}

api_data['apikeys'] = []

api_data['apikeys'].append({
    'name': 'googlesafebrowsing',
    'key': 'testing safebrowsing'
})

with open('/Users/joshuageise/Projects/overwatch_dev/overwatchWeb/server/routes/api/data/apikeys.json', 'w') as outfile:
    json.dump(api_data, outfile)

#WIfi Setup

wifi_data = {'ssid':'testing ssid','password':'testing password'}

with open('/Users/joshuageise/Projects/overwatch_dev/overwatchWeb/server/routes/api/data/wifisettings.json', 'w') as outfile:
    json.dump(wifi_data, outfile)
