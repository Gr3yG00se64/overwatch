#Local Dependencies
import config

#Package Dependencies
from pymongo import MongoClient

def remove_alerts(alerts):
    #Establish DB Connection
    connection = MongoClient(config.mongoURI)

    #Set Up DB for Alerts
    alertDB = connection["alerts"]
    alertCollection = alertDB["alerts"]

    if alerts:
        for alert in alerts:
            alertCollection.remove({'_id': alert.get('_id')})

def retrieve_alerts():
    alerts = []

    # Establish DB Connection
    connection = MongoClient(config.mongoURI)

    # Retrieve names of all databases
    dbNames = connection.list_database_names()

    if 'alerts' in dbNames:
        # Set Up DB for Alerts
        alertDB = connection["alerts"]
        alertCollection = alertDB["alerts"]

        #Retrieve all alerts
        db_alerts = alertCollection.find()

        #Generate list of alerts
        for alert in db_alerts:
            alerts.append(alert)

    return alerts



#Returns list of dictionaries that contained registered device information
def retrieve_regDevices():
    regDevices = []

    #Establish DB Connection
    connection = MongoClient(config.mongoURI)

    # Retrieve names of all databases
    dbNames = connection.list_database_names()

    if 'netmap' in dbNames:

        #Set up DB for NetMap Devices
        netmapDB = connection["netmap"]
        netmapCollection = netmapDB["netmaps"]

        #Retrieve all registered devices
        devices = netmapCollection.find()

        #Generate list of registered devices
        for device in devices:
            regDevices.append(device)

    #Export the list of dictonaries
    return regDevices

