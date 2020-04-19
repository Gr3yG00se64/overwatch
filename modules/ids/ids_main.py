#Local Dependencies
import config
import parsezeek
import detect
import db_handler
import zeek_result_handler
import alert_builder

#Package Dependencies

def main():
    #Set Global Variables
    config.init()

    #Local Variable Setup
    alerts = []

    #Retrieve list of registered devices
    regDevices = db_handler.retrieve_regDevices()

    #Parse Zeek File
    http_results = parsezeek.http_parse()
    notice_results = parsezeek.notice_parse()

    #Run detection methods
    alerts = detect.safebrowsing_check(http_results, alerts)
    alerts = detect.zeekScript_check(notice_results, alerts)

    #Modify Alert Values for database insertion
    alert_builder.modAlerts(alerts, http_results, regDevices)

    #Insert new Alerts into database
    db_handler.insert_alerts(alerts)
    #print(alerts)

if __name__ == '__main__':
	main()
