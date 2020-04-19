#!/bin/bash

LOGIN_PATH=/home/overwatch/overwatchWeb/server/routes/api/data/login.json
PASS_PATH=/etc/nginx/.htpasswd

if [ -f "$LOGIN_PATH" ]; then
	USER=$(jq .username $LOGIN_PATH | sed 's/"//g')
	PASSWORD=$(jq .password $LOGIN_PATH | sed 's/"//g')

	htpasswd -c -b $PASS_PATH $USER $PASSWORD

	rm $LOGIN_PATH 
fi

