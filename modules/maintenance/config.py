#Local Dependencies

#Package Dependencies
import os
import json

def init():

    global mongoURI
    global web_data_dir
    global tmp_dir
    global alertExpiry

    #MongoDB Configuration
    mongoURI = 'mongodb://localhost:27017'

    #Web Data Directory Configuration
    #web_data_dir = '/home/overwatch/overwatchWeb/server/routes/api/data/'

    #Tmp Directory
    #tmp_dir = ''

    #Dev Web Data Directory Configuration
    web_data_dir = '/Users/joshuageise/Projects/overwatch_dev/overwatchWeb/server/routes/api/data/'

    #Dev Tmp Directory
    tmp_dir = '/Users/joshuageise/Projects/overwatch/modules/maintenance/temp/'

    #Default Alert Expiry
    alertExpiry = 0

    #Find and assign alert expiry time
    if (os.path.exists(web_data_dir + 'expiry.json')):
        with open(web_data_dir + 'expiry.json', 'r') as f:
            all_expiry = json.load(f)

            alertExpiry = all_expiry.get('alert')