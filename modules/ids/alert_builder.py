#Local Dependencies
import config
import zeek_result_handler

#Package Dependencies

def modAlerts(alert_results, zeek_results, regDevices):

    for alert in alert_results:
        setAlertSeverity(alert, zeek_results, regDevices)
        setAlertDescription(alert)

#Alert Results, Associated IP, Registered Devices, Type of Alert
def setAlertSeverity(alert, zeek_results, regDevices):

    #Complete checks based off alert type
    if alert.get('alertType') == 'maliciousURL':

        #Get all registered device IPs
        ip_list = zeek_result_handler.http_to_ip(zeek_results)

        #Check to see if malicious URL activity was done by a registered device
        for device in regDevices:
            if (device.get('ip') == alert.get('sendIP')) or (device.get('ip') == alert.get('respIP')):
                #Check if severity level is already maximum
                if config.alertBreakdown[0].get('severity') < len(config.alertSeverityLevels)+1:
                    alert['severity'] = config.alertSeverityLevels[config.alertBreakdown[0].get('severity')+1]
            else:
                alert['severity'] = config.alertSeverityLevels[config.alertBreakdown[0].get('severity')]

def setAlertDescription(alert):

    if alert.get('alertType') == 'maliciousURL':
        alert['description'] = 'Device connected to Malicious URL: '+alert.get('alertInfo')

def alert_generator(alertInfo, threatType, alertType, sendIP, respIP):
    return {
        'alertInfo': alertInfo,
        'threatType': threatType,
        'alertType': alertType,
        'severity': '',
        'description': '',
        'sendIP': sendIP,
        'respIP': respIP
    }