
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
        if result.get('origIP') not in ip_list:
            ip_list.append(result.get('origIP'))

        if result.get('respIP') not in ip_list:
            ip_list.append(result.get('respIP'))

    return ip_list

#Finds malicious results
#def extract_http_alert_info(badURLs):
