
## Local Dependencies
import config
import alert_builder
import zeek_result_handler

## Package Dependencies
import requests

#Check for malicious URLs using Google Safebrowsing API
def safebrowsing_check(http_results):

    urls = zeek_result_handler.http_to_url(http_results)

    entries = []
    alerts = []

    for url in urls:
        url = url.strip('"')
        entries.append({'url': str(url)})

    payload = {'client': {'clientId': "mycompany", 'clientVersion': "0.1"},
        'threatInfo': {'threatTypes': ["SOCIAL_ENGINEERING", "MALWARE"],
                       'platformTypes': ["ANY_PLATFORM"],
                       'threatEntryTypes': ["URL"],
                       'threatEntries': entries}}

    params = {'key': config.googleSafe_apikey}
    r = requests.post(config.googleSafeURL, params=params, json=payload)

    if not r.json():
        return alerts
    else:
        #Response comes in as a dictionary, with an array value, with a dictionary inside

        #Pulling JSON into Dictionary
        response = r.json()

        #Getting List
        matches = response.get('matches')

        matched_alerts = []
        bad_urls = []

        #Looping Through List
        if matches:
            for match in matches:
                if match.get('threat').get('url') not in bad_urls:
                    bad_urls.append(match.get('threat').get('url'))

                    for result in http_results:
                        if (result.get('host') == match.get('threat').get('url')):
                            newDict = {'sendIP': result.get('origIP'), 'recIP': result.get('respIP')}
                            if newDict not in matched_alerts:
                                matched_alerts.append({'sendIP': result.get('origIP'), 'recIP': result.get('respIP')})

            for matchesFound in matched_alerts:
                    alerts.append(alert_builder.alert_generator(match.get('threat').get('url'), match.get('threatType'), 'maliciousURL',
                                                                    matchesFound.get('sendIP'), matchesFound.get('respIP')))

        return alerts