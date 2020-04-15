
## Local Dependencies
import config

## Package Dependencies
import requests

#Check for malicious URLs using Google Safebrowsing API
def safebrowsing_check(http_results):


    entries = []
    badEntries = []

    for url in urls:
        url.strip()
        entries.append({'url': url})

    payload = {'client': {'clientId': "mycompany", 'clientVersion': "0.1"},
        'threatInfo': {'threatTypes': ["SOCIAL_ENGINEERING", "MALWARE"],
                       'platformTypes': ["ANY_PLATFORM"],
                       'threatEntryTypes': ["URL"],
                       'threatEntries': entries}}

    params = {'key': config.googleSafe_apikey}
    r = requests.post(config.googleSafeURL, params=params, json=payload)

    #
    if not r.json():
        return badEntries
    else:
        #Response comes in as a dictionary, with an array value, with a dictionary inside

        #Pulling JSON into Dictionary
        response = r.json()

        #Getting List
        matches = response.get('matches')

        #Looping Through List
        if matches:
            for match in matches:
                badEntries.append([match.get('threat').get('url'), match.get('threatType')])

        return badEntries
