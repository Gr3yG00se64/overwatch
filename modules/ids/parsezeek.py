##Zeek Parser

#Local Dependencies
import config
#Remote Dependencies
import os

def http_parse():
    #Prep Parser Value Location Variables
    ts = 0
    origIP = 2
    origPort = 3
    respIP = 4
    respPort = 5
    host = 8

    #Create list for
    http_results = []

    if (os.path.exists(config.zeek_log_dir+'http.log')):
        with open(config.zeek_log_dir+'http.log') as host_file:
            for line in host_file:
                base_split = line.split('\'')[0].split(',')

                http_results.append({'ts': base_split[ts].split(':')[1],
                                'origIP': base_split[origIP].split(':')[1],
                                'origPort': base_split[origPort].split(':')[1],
                                'respIP': base_split[respIP].split(':')[1],
                                'respPort': base_split[respPort].split(':')[1],
                                'host': base_split[host].split(':')[1]
                                })

    return http_results
