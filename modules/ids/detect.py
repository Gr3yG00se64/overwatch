
## Local Dependencies
#import config

## Package Dependencies
import requests
import json

def checkURLS(urls):
    entries = []
    badEntries = []
    safeURL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

    for url in urls:
        entries.append({'url': 'https://'+url})

    payload = {'client': {'clientId': "mycompany", 'clientVersion': "0.1"},
        'threatInfo': {'threatTypes': ["SOCIAL_ENGINEERING", "MALWARE"],
                       'platformTypes': ["ANY_PLATFORM"],
                       'threatEntryTypes': ["URL"],
                       'threatEntries': entries}}
                       #'threatEntries': [{'url': "https://testsafebrowsing.appspot.com/s/phishing.html"}]}}

    params = {'key': 'AIzaSyAn4zlbI5v4xc4jf51qd9WIcAVyNyesaTg'}
    r = requests.post(safeURL, params=params, json=payload)
    # Print response
    if not r.json():
        return badEntries
    else:
        #Response comes in as a dictionary, with an array value, with a dictionary inside

        #Pulling JSON into Dictionary
        response = r.json()

        #Getting List
        matches = response.get('matches')

        #Looping Through List
        for match in matches:
            badEntries.append([match.get('threat').get('url'), match.get('threatType')])
            #print(match.get('threatType'))
            #print(match.get('threat').get('url'))

        return badEntries
