#Local Dependencies
import config

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

    #post = {"modID": 1, "description": "IDS", "severity": "High"}

    #collection.insert_one(post)



if __name__ == '__main__':
	main()
