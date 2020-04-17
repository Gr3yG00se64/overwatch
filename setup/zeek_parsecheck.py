
ts = 0
origIP = 2
origPort = 3
respIP = 4
respPort = 5
host = 8

results = []

with open('/Users/joshuageise/Projects/overwatch_dev/zeek/logs/current/http.log') as host_file:
    for line in host_file:
        #Base Split
        base_split = line.split('\'')[0].split(',')
        '''results.append({'ts': base_split[ts].split(':')[1],
                        'origIP': base_split[origIP].split(':')[1],
                        'origPort': base_split[origPort].split(':')[1],
                        'respIP': base_split[respIP].split(':')[1],
                        'respPort': base_split[respPort].split(':')[1],
                        'host': base_split[host].split(':')[1]
                        })'''
        #ts
        print(base_split[0].split(',')[0].split(':')[1])
        results.append(base_split[0].split(',')[0].split(':')[1])

        #Orig IP = 2
        #print(base_split[0].split(',')[2].split(':')[1])

        #Orig Port = 3
        #print(base_split[0].split(',')[3].split(':')[1])

        #Resp IP = 4
        #print(base_split[0].split(',')[4].split(':')[1])

        #Resp Port = 5
        #print(base_split[0].split(',')[5].split(':')[1])

        #Host(website)=8
        #print(base_split[0].split(',')[8].split(':')[1])

    print(results)
