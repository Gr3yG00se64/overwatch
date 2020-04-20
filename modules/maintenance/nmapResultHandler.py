#Local Dependencies

#Package Dependencies

def convertNmapResults(ip_list, regDevices):
    #Currently, just IPs are received
    unregDevices = {'devices': []}
    regDevice_ips = []

    if  regDevices:
        for device in regDevices:
            regDevice_ips.append(device.get('ip'))

    for ip in ip_list:
        if (ip not in regDevice_ips):
            unregDevices['devices'].append({'ip': ip})

    return unregDevices
