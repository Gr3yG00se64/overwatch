
## Local Dependencies
import config

## Package Dependencies
import requests
import json


url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
payload = {'client': {'clientId': "mycompany", 'clientVersion': "0.1"},
        'threatInfo': {'threatTypes': ["SOCIAL_ENGINEERING", "MALWARE"],
                       'platformTypes': ["ANY_PLATFORM"],
                       'threatEntryTypes': ["URL"],
                       'threatEntries': [{'url': "https://testsafebrowsing.appspot.com/s/phishing.html", "url": "https://testsafebrowsing.appspot.com/s/malware.html"}]}}

params = {'key': config.goog_safe_api}
r = requests.post(url, params=params, json=payload)
# Print response
print(r)
print(r.json())
