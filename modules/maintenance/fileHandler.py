#Local Dependencies
import config

#Package Dependencies
import os
import json

def pullNmapIPs():
    ip_list = []

    if (os.path.exists(config.tmp_dir + 'iplist.txt')):
        with open(config.tmp_dir + 'iplist.txt', 'r') as f:
            for line in f:
                ip_list.append(line.strip())

    return ip_list

def writeUnregJSON(nmap_json):
    with open(config.web_data_dir+'unregDevices.json', 'w') as f:
        json.dump(nmap_json, f)