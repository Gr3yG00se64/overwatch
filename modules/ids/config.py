##

def init():

    global zeek_dir
    global zeek_log_dir
    global mod_id
    global googleSafe_apikey
    global googleSafeURL
    global mongoURI
    global alertSeverityLevels
    global alertBreakdown

    #Overwatch Module Configuration
    mod_id = 2

    #Alert Variables
    alertSeverityLevels = ['Low', 'Medium', 'High']
    alertBreakdown = [{'alertType': 'maliciousURL', 'severity': 1, 'Description': 'Found traffic to malicious website'}
                        ]

    #MongoDB Configuration
    mongoURI = 'mongodb://localhost:27017'

    #Zeek Configuration
    zeek_dir = '/usr/local/zeek/'
    zeek_log_dir = zeek_dir + 'logs/current/'

    #Zeek Dev Configuration
    #zeek_dir = '/Users/joshuageise/Projects/overwatch_dev/zeek/'
    #zeek_log_dir = zeek_dir + 'logs/current/'


    ##Google Safebrowsing Configuration
    googleSafe_apikey = 'AIzaSyAn4zlbI5v4xc4jf51qd9WIcAVyNyesaTg'
    googleSafeURL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"