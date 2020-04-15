##

def init():

    global zeek_dir
    global zeek_log_dir
    global mod_id
    global googleSafe_apikey
    global googleSafeURL
    global mongoURI

    #Overwatch Module Configuration
    mod_id = 2

    #MongoDB Configuration
    mongoURI = 'mongodb://localhost:27017'

    #Zeek Configuration
    zeek_dir = '/Users/joshuageise/Projects/overwatch_dev/zeek/'
    zeek_log_dir = zeek_dir + 'logs/current/'


    ##Google Safebrowsing Configuration
    googleSafe_apikey = 'AIzaSyAn4zlbI5v4xc4jf51qd9WIcAVyNyesaTg'
    googleSafeURL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"