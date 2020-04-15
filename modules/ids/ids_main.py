#Local Dependencies
import config
import parsezeek
import detect
import db_handler
import zeek_result_handler

#Package Dependencies
from pymongo import MongoClient

#mongodb://localhost:27017/alerts

def main():
    #Set Global Variables
    config.init()

    #Retrive list of registered devices
    db_handler.retrieve_regDevices()

    #Retrieve visited URLS from zeek logs
    http_results = parsezeek.http_parse()

    #Retrieve Bad URLS determined by Google SafeBrowsing
    #badUrls = detect.checkURLS(urls)

    # Alerts

    zeek_result_handler.http_to_ip(http_results)

if __name__ == '__main__':
	main()
