
## Local Dependencies
import config
import alert_builder
import zeek_result_handler

## Package Dependencies
import requests

#Alert Generator Format seen below:
#(alertInfo, threatType, alertType, sendIP, respIP)

#Check for malicious URLs using Google Safebrowsing API
def safebrowsing_check(http_results, alerts):

    urls = zeek_result_handler.http_to_url(http_results)

    entries = []

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
    print(r.json())
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

        #Looping Through List if results are populated
        if matches:
            for match in matches:
                if match.get('threat').get('url') not in bad_urls:
                    bad_urls.append(match.get('threat').get('url'))

                    for result in http_results:
                        if (result.get('host') == match.get('threat').get('url')):
                            newDict = {'sendIP': result.get('origIP'), 'recIP': result.get('respIP'),
                                        'url': match.get('threat').get('url'), 'threatType': match.get('threatType')}

                            if newDict not in matched_alerts:
                                matched_alerts.append(newDict)

            for matchesFound in matched_alerts:
                    alerts.append(alert_builder.alert_generator(matchesFound.get('url'), matchesFound.get('threatType'),
                                config.alertBreakdown[0].get('alertType'), matchesFound.get('sendIP'), matchesFound.get('respIP')))

        return alerts

def zeekScript_check(notice_results, alerts):

    for notice_alert in notice_results:

        #Modify paramaters for alert builder depending on which zeek script generated a notice

        # SSH Bruteforce Check: Index 1 in alert breakdown array
        if notice_alert.get('alertType') == config.alertBreakdown[1].get('alertType'):
            alerts.append(alert_builder.alert_generator(notice_alert.get('msg'), notice_alert.get('alertType'),
                                config.alertBreakdown[1].get('alertType'), '', ''))

        # Port Scan Check: Index 2 in alert breakdown array
        elif notice_alert.get('alertType') == config.alertBreakdown[2].get('alertType'):
            alerts.append(alert_builder.alert_generator(notice_alert.get('msg'), notice_alert.get('alertType'),
                          config.alertBreakdown[2].get('alertType'), '', ''))

    return alerts
