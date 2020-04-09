#!/bin/sh

#Shell Script to copy zeek logs (excluding the ones for the current day) to the data folder in the Overwatch Web Directory

#Path Variables
zeek_path="/usr/local/zeek"
web_path="/home/overwatch/overwatchWeb/server/routes/api/data/logs.zip"

#Change to zeek directory
cd $zeek_path

#Zip required contents except current, store log file in web directory data folder
zip -r $web_path logs -x "logs/current/*"