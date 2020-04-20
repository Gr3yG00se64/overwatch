#Local Dependencies

#Package Dependencies
import os
import json

def init():

    global zeek_dir
    global zeek_log_dir
    global mod_id
    global googleSafe_apikey
    global googleSafeURL
    global mongoURI
    global alertSeverityLevels
    global alertBreakdown
    global web_data_dir
    global mod_enabled

    #Overwatch Module Configuration
    mod_id = 2

    #Alert Variables
    alertSeverityLevels = ['LOW', 'MEDIUM', 'HIGH']
    alertBreakdown = [{'alertType': 'maliciousURL', 'severity': 0, 'description': 'Found traffic to malicious website'},
                      {'alertType': 'SSHBruteforce', 'severity': 2, 'description': 'Malicious Login Attempts'},
                      {'alertType': 'PortScan', 'severity': 1, 'description': 'Malicious Reconnaissance'}]

    #MongoDB Configuration
    mongoURI = 'mongodb://localhost:27017'

    #Zeek Configuration
    #zeek_dir = '/usr/local/zeek/'
    #zeek_log_dir = zeek_dir + 'logs/current/'

    #Web Data Directory Configuration
    #web_data_dir = '/home/overwatch/overwatchWeb/server/routes/api/data/'

    #Dev Zeek Configuration
    zeek_dir = '/Users/joshuageise/Projects/overwatch_dev/zeek/'
    zeek_log_dir = zeek_dir + 'logs/current/'

    #Dev Web Data Directory Configuration
    web_data_dir = '/Users/joshuageise/Projects/overwatch_dev/overwatchWeb/server/routes/api/data/'

    ##Google Safebrowsing Configuration
    google_safe_name = 'googlesafebrowsing'
    googleSafe_apikey = '' #AIzaSyAn4zlbI5v4xc4jf51qd9WIcAVyNyesaTg
    googleSafeURL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

    #Mod Enabled Default
    mod_enabled = True

    #Retrive All API Keys
    if (os.path.exists(web_data_dir + 'apikeys.json')):
        with open(web_data_dir + 'apikeys.json', 'r') as f:
            api_keys = json.load(f)

            for key in api_keys.get('apikeys'):
                if key.get('name') == google_safe_name:
                    googleSafe_apikey = key.get('key')

    #Check if mod is enabled
    if (os.path.exists(web_data_dir + 'mod_data.json')):
        with open(web_data_dir + 'mod_data.json', 'r') as f:
            module_info = json.load(f)

            for module in module_info.get('modules'):
                if module.get('id') == 2:
                    mod_enabled = module.get('enabled')