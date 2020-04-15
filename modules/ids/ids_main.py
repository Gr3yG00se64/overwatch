#Local Dependencies
import config
import parsezeek
import detect
import db_handler
import zeek_result_handler
import alert_builder

#Package Dependencies
from pymongo import MongoClient

#mongodb://localhost:27017/alerts

def main():
    #Set Global Variables
    config.init()

    #Retrive list of registered devices
    regDevices = db_handler.retrieve_regDevices()

    #Parse Zeek File
    http_results = parsezeek.http_parse()

    #Run detection methods
    http_alerts = detect.safebrowsing_check(zeek_result_handler.http_to_url(http_results))

    #Modify Alert Values for database insertion
    alert_builder.modAlerts(http_alerts, http_results, regDevices)

    #Insert new Alerts into database
    #db_handler.insert_alerts(http_alerts)
    print(http_alerts)

if __name__ == '__main__':
	main()
