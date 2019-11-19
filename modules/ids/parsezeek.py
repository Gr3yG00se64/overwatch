##Zeek Parser

#Local Dependencies
import config
#Remote Dependencies
import os
import json

def getHosts():
    #http.log , ssl.log

    urls = []

    #http --> host:
    #ssl --> server_name

    #http --> host:
    if (os.path.exists(config.zeek_log_dir+'http.log')):
        with open(config.zeek_log_dir+'http.log') as host_file:
            for line in host_file:
                url = eval((line.split(':')[9]).split(',')[0])
                if url not in urls:
                    urls.append(url)

    if (os.path.exists(config.zeek_log_dir+'ssl.log')):
        with open(config.zeek_log_dir+'http.log') as host_file:
            for line in host_file:
                url = eval((line.split(':')[9]).split(',')[0])
                if url not in urls:
                    urls.append(url)

    return urls
