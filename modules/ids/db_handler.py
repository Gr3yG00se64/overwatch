#Local Dependencies
import config

#Package Dependencies
from pymongo import MongoClient

def insert_alerts(alerts):
    #Establish DB Connection
    connection = MongoClient(config.mongoURI)

    #Set Up DB for Alerts
    alertDB = connection["alerts"]
    alertCollection = alertDB["alerts"]

    if alerts:
        for alert in alerts:
            post = {"modID": config.mod_id, "description": alert.get('description'), "severity": alert.get('severity')}
                    #,"threatType": alert.get('threatType') }
            alertCollection.insert_one(post)

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

