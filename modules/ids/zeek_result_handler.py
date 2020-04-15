
#Takes in results extracted from http.log, returns all urls
def http_to_url(http_results):
    urls = []

    for result in http_results:
        if result.get('host') not in urls:
            urls.append(result.get('host'))

    return urls

def http_to_ip(http_results):
    ip_list = []

    for result in http_results:
        if result.get('origIP').strip('"') not in ip_list:
            ip_list.append(result.get('origIP').strip('"'))

        if result.get('respIP').strip('"') not in ip_list:
            ip_list.append(result.get('respIP').strip('"'))

    return ip_list
