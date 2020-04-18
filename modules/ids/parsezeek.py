##Zeek Parser

#Local Dependencies
import config

#Remote Dependencies
import os
import json

def http_parse():

    http_results = []

    if (os.path.exists(config.zeek_log_dir + 'http.log')):
        with open(config.zeek_log_dir + 'http.log', 'r') as f:
            json_string = f.read()

            if json_string[0] != '[':
                json_string = '[' + json_string + ']'

            http_log = json.loads(json_string)

            for result in http_log:
                http_results.append({'ts': result['ts'],
                                     'origIP': result['id.orig_h'],
                                     'origPort': result['id.orig_p'],
                                     'respIP': result['id.resp_h'],
                                     'respPort': result['id.resp_p'],
                                     'host': result['host']
                                     })
    return http_results