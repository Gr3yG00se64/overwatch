import json

data = {}
data['modules'] = []
data['modules'].append({
    'name': 'Net Logger',
    'description': 'Description for network logger',
    'author': 'Gr3yG00se',
    'enabled': True,
    'id': 1
})
data['modules'].append({
    'name': 'Basic IDS',
    'description': 'Description for basic intrusion detection system',
    'author': 'Gr3yG00se',
    'enabled': True,
    'id': 2
})
data['modules'].append({
    'name': 'Honeypot',
    'description': 'Description for Honeypot',
    'author': 'Anon',
    'enabled': True,
    'id': 3
})
data['modules'].append({
    'name': 'IPS',
    'description': 'Description for Intrusion Prevention System',
    'author': 'Anon',
    'enabled': True,
    'id': 4
})
data['modules'].append({
    'name': 'Pi-Hole',
    'description': 'Block stupid ads',
    'author': 'Anon',
    'enabled': True,
    'id': 5
})

with open('/Users/joshuageise/Projects/overwatch_dev/web/overwatch_web_backend/data/mod_data.json', 'w') as outfile:
    json.dump(data, outfile)