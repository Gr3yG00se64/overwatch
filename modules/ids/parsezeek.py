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
                                     'host': http_log_result['host']+http_log_result['uri']
                                     })
    return http_results

def notice_parse():

    notice_results = []

    #From CONFIG:
    #  SSH Bruteforce is index 1 in alert breakdown array
    #  Port Scan is index 2 in alert breakdown array
    if (os.path.exists(config.zeek_log_dir + 'notice.log')):
        with open(config.zeek_log_dir + 'notice.log', 'r') as f:
            for line in f:
                notice_line = json.loads(line)

                if notice_line.get('note'):
                    #Add
                    if ((notice_line.get('note').split(':')[0] == 'Scan') and (notice_line.get('note').split(':')[2]=='Port_Scan')):

                        notice_results.append({'ts': notice_line['ts'],
                                     'origIP': notice_line['src'],
                                     'msg': notice_line['msg'],
                                     'alertType': config.alertBreakdown[2].get('alertType')
                                     })

                    elif ((notice_line.get('note').split(':')[0] == 'SSH') and (notice_line.get('note').split(':')[2] == 'Password_Guessing')):
                        notice_results.append({'ts': notice_line['ts'],
                                               'origIP': notice_line['src'],
                                               'msg': notice_line['msg'],
                                               'alertType':  config.alertBreakdown[1].get('alertType')
                                               })
    return notice_results