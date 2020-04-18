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

                for line in f:
                    http_log_result = json.loads(line)

                    http_results.append({'ts': http_log_result['ts'],
                                         'origIP': http_log_result['id.orig_h'],
                                         'origPort': http_log_result['id.orig_p'],
                                         'respIP': http_log_result['id.resp_h'],
                                         'respPort': http_log_result['id.resp_p'],
                                         'host': http_log_result['host']
                                         })
    return http_results


'''
json_string = f.read()

            if json_string[0] != '[':
                json_string = '[' + json_string + ']'
                
            http_log_result = json.loads(json_string)

            for result in http_log:
                http_results.append({'ts': result['ts'],
                                     'origIP': result['id.orig_h'],
                                     'origPort': result['id.orig_p'],
                                     'respIP': result['id.resp_h'],
                                     'respPort': result['id.resp_p'],
                                     'host': result['host']
                                     })
'''