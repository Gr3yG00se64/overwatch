#Local Dependencies
import config
import fileHandler
import db_handler
import nmapResultHandler
import expiryHandler

#Package Dependencies

def main():
    #Set Global Variables
    config.init()

    #####   Unregistered Device Maintenance

    #Retrieve Registered Devices
    regDevices = db_handler.retrieve_regDevices()

    #Retrieve Nmap Results
    nmap_ip_list = fileHandler.pullNmapIPs()

    #Create dictionary of unregistered devices on network
    unreg_dict = nmapResultHandler.convertNmapResults(nmap_ip_list, regDevices)

    #Write unregistered device information to JSON file in Web Directory
    fileHandler.writeUnregJSON(unreg_dict)

    #####   Expiry Maintenance

    #Retrieve Alerts
    alerts = db_handler.retrieve_alerts()

    #Return list of Expired Alerts
    expired_alerts = expiryHandler.expiredAlertsFinder(alerts)

    #Remove Expired Alerts from DB
    db_handler.remove_alerts(expired_alerts)



if __name__ == '__main__':
	main()
