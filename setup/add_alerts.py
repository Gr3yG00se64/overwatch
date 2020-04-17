import json

data = []
data.append({
    'ts': '1574053161.804296',
    'uid': 'C7Nzqy4J1H3f9JUDed',
    'id.orig_h': '192.168.1.5',
    'id.orig_p': '51508',
    'id.resp_h': '23.79.244.155',
    'id.resp_p': '80',
    'trans_depth': '2,',
    'method': 'GET',
    'host': 'https://testsafebrowsing.appspot.com/s/phishing.html',
    'uri': '/filestreamingservice/files/fc989f39-6b38-4ee7-b13a-6f6b68435329?P1=1574053617&P2=402&P3=2&P4=VwbJChfabzKiBTXbHqdbcrCbu7+SUgA15enBstQtHr1qZRdvZo9dYhm52BIPOpPz5uFEbENvTEv/G0awych5Sw==',
    'user_agent': 'Microsoft-Delivery-Optimization/10.0',
    'request_body_len': '0,',
    'tags': []
})

data.appen({
'ts': '1604053161.804296',
    'uid': 'C7Nzqy4J1H3f9JUDed',
    'id.orig_h': '192.168.1.10',
    'id.orig_p': '51508',
    'id.resp_h': '23.79.244.155',
    'id.resp_p': '80',
    'trans_depth': '2,',
    'method': 'GET',
    'host': 'malware.testing.google.test/testing/malware/',
    'uri': '/filestreamingservice/files/fc989f39-6b38-4ee7-b13a-6f6b68435329?P1=1574053617&P2=402&P3=2&P4=VwbJChfabzKiBTXbHqdbcrCbu7+SUgA15enBstQtHr1qZRdvZo9dYhm52BIPOpPz5uFEbENvTEv/G0awych5Sw==',
    'user_agent': 'Microsoft-Delivery-Optimization/10.0',
    'request_body_len': '0,',
    'tags': []
})
#with open('/Users/joshuageise/Projects/overwatch/setup/http.log', 'a+') as outfile:
with open('/usr/local/zeek/logs/current/http.log', 'a+') as outfile:
    json.dump(data, outfile)