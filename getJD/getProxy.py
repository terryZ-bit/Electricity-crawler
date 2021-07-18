import time

import requests as rq

targetUrl_1 = 'http://tiqu.linksocket.com:81/abroad?num=100&type=2&lb=1&sb=0&flow=1&regions=china&port=1&n=1'
targetUrl_2 = 'http://tiqu.linksocket.com:81/abroad?num=1&type=2&lb=1&sb=0&flow=1&regions=china&port=1&n=1'
white_url = 'http://api.ipidea.net/index/index/save_white?neek=269439&appkey=d63186adc97d384130178c89e482f3d7&white' \
            '=10.253.231.150 '
white_url_2 = 'http://api.ipidea.net/index/index/save_white?neek=269439&appkey=d63186adc97d384130178c89e482f3d7&white' \
              '=106.85.78.66'
white_url_3 = 'http://api.ipidea.net/index/index/save_white?neek=269439&appkey=d63186adc97d384130178c89e482f3d7&white' \
              '=106.85.78.173'
white_url_4 = 'http://api.ipidea.net/index/index/save_white?neek=269439&appkey=d63186adc97d384130178c89e482f3d7&white' \
              '=106.84.148.230'
white_url_5 = 'http://api.ipidea.net/index/index/save_white?neek=269439&appkey=d63186adc97d384130178c89e482f3d7&white' \
              '=106.84.188.162'
white_url_6 = 'http://api.ipidea.net/index/index/save_white?neek=269439&appkey=d63186adc97d384130178c89e482f3d7&white' \
              '=106.84.157.45'
# rsp_1 = rq.get(white_url)
# rsp_2 = rq.get(white_url_2)
# rsp_3 = rq.get(white_url_3)
# rsp_4 = rq.get(white_url_4)
# rsp_5 = rq.get(white_url_5)
rsp_6 = rq.get(white_url_6)
header = {
    'X-Forwarded-For': '1.1.1.1',
    'X-Forwarded-Port': '443',
}


def getProxies():
    rsp = rq.get(targetUrl_1)
    proxy_dict_1 = rsp.json()
    proxy_list_1 = proxy_dict_1['data']
    proxy_list = []
    for i in proxy_list_1:
        proxy = {
            'http': 'http://' + str(i['ip']) + ':' + str(i['port']),
            'https': 'http://' + str(i['ip']) + ':' + str(i['port'])
        }
        proxy_list.append(proxy)
    return proxy_list


pro = getProxies()


def getProxy():
    time.sleep(2)
    rsp = rq.get(targetUrl_2)
    proxy_dict_1 = rsp.json()
    proxy_list_1 = proxy_dict_1['data'][0]
    proxy = {
        'http': 'http://' + str(proxy_list_1['ip']) + ':' + str(proxy_list_1['port']),
        'https': 'http://' + str(proxy_list_1['ip']) + ':' + str(proxy_list_1['port'])
    }

    return proxy

getProxy()
