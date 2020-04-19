#!/bin/sh

#Shell Script to copy zeek logs (excluding the ones for the current day) to the data folder in the Overwatch Web Directory

#Path Variables
zeek_path="/usr/local/zeek"
log_path="/home/overwatch/overwatchWeb/server/routes/api/data/log.zip"
mod_path="/home/overwatch/overwatchWeb/server/routes/api/data/mod_data.json"

#Logger is Module One
#Check to see if this module is enabled
is_enabled=$(jq .modules[0].enabled $mod_path)

if [ "$is_enabled" = true ]; then
	#Change to zeek directory
	cd $zeek_path

	#Zip required contents except current, store log file in web directory data folder
	zip -r $log_path logs -x "logs/current/*"
fi


