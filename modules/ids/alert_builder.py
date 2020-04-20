#Local Dependencies
import config
import zeek_result_handler

#Package Dependencies
from datetime import datetime

def modAlerts(alerts, zeek_results, regDevices):

    for alert in alerts:
        setAlertSeverity(alert, regDevices)
        setAlertDescription(alert)

    return alerts

#Alert Results, Associated IP, Registered Devices, Type of Alert
def setAlertSeverity(alert, regDevices):

    #Complete checks based off alert type

    #Malicious URL Check: Index 0 in alert breakdown array
    if alert.get('alertType') == config.alertBreakdown[0].get('alertType'):

        #Check to see if malicious URL activity was done by a registered device

        if regDevices:
            for device in regDevices:
                if (device.get('ip') == alert.get('sendIP')) or (device.get('ip') == alert.get('respIP')):
                    #Check if severity level is already maximum
                    if config.alertBreakdown[0].get('severity') < len(config.alertSeverityLevels)+1:
                        alert['severity'] = config.alertSeverityLevels[config.alertBreakdown[0].get('severity')+1]
                else:
                    alert['severity'] = config.alertSeverityLevels[config.alertBreakdown[0].get('severity')]
        else:
            alert['severity'] = config.alertSeverityLevels[config.alertBreakdown[0].get('severity')]

    # SSH Bruteforce Check: Index 1 in alert breakdown array
    elif alert.get('alertType') == config.alertBreakdown[1].get('alertType'):
        alert['severity'] = config.alertSeverityLevels[config.alertBreakdown[1].get('severity')]

    # Port Scan Check: Index 2 in alert breakdown array
    elif alert.get('alertType') == config.alertBreakdown[2].get('alertType'):
        alert['severity'] = config.alertSeverityLevels[config.alertBreakdown[2].get('severity')]

def setAlertDescription(alert):
    #Set Description based off of Threat Type

    # Malicious URL Check: Index 0 in alert breakdown array
    if alert.get('alertType') == config.alertBreakdown[0].get('alertType'):
        alert['description'] = config.alertBreakdown[0].get('description')

    # SSH Bruteforce Check: Index 1 in alert breakdown array
    elif alert.get('alertType') == config.alertBreakdown[1].get('alertType'):
        alert['description'] = config.alertBreakdown[1].get('description')

    # Port Scan Check: Index 2 in alert breakdown array
    elif alert.get('alertType') == config.alertBreakdown[2].get('alertType'):
        alert['description'] = config.alertBreakdown[2].get('description')

def setAlertDate(ts):
    ts_to_date = datetime.fromtimestamp(int(ts))

    return ts_to_date.strftime("%m/%d/%Y")

def alert_generator(alertInfo, threatType, alertType, sendIP, respIP, ts):
    date = setAlertDate(ts)

    return {
        'alertInfo': alertInfo,
        'threatType': threatType,
        'alertType': alertType,
        'severity': '',
        'description': '',
        'sendIP': sendIP,
        'respIP': respIP,
        'date': date
    }