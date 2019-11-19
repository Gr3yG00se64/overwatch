#Local Dependencies
import config
import parsezeek
import detect

#Package Dependencies
import time
from pymongo import MongoClient

#mongodb://localhost:27017/alerts

def main():
    #Set Global Variables
    config.init()

    #URI
    uri = 'mongodb://localhost:27017'

    #Set Up mongodb
    connection = MongoClient(uri)
    db = connection["alerts"]
    collection = db["alerts"]

    urls = parsezeek.getHosts()
    badUrls = detect.checkURLS(urls)

    if badUrls:
        for badUrl in badUrls:
            desc = 'Traffic going to possible malicious url. Url: '+badUrl[0]+' is known for '+badUrl[1]+' attacks.'
            post = {"modID": config.mod_id, "description": desc, "severity": "Medium" }
            collection.insert_one(post)

    #READ FROM MONGO
    #items = collection.find()
    #for x in items:
    #    print(x)

    #ADD TO MONGO
    #post = {"modID": 1, "description": "IDS", "severity": "High"}
    #collection.insert_one(post)


if __name__ == '__main__':
	main()
