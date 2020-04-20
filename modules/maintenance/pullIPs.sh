#!/bin/bash

NMAP_RESULT_PATH=/home/overwatch/testing/nmap_result.txt
IP_LIST_PATH=/home/overwatch/testing/iplist.txt

nmap -sn 192.168.1.0/24 -oG $NMAP_RESULT_PATH
grep Host $NMAP_RESULT_PATH | awk '{print $2}' > $IP_LIST_PATH

chown -R overwatch:overwatch $IP_LIST_PATH
