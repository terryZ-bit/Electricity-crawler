import json

import requests as rq
from bs4 import BeautifulSoup as bS

url = 'https://wq.jd.com/commodity/itembranch/getspecification?callback=commParamCallBackA&skuid=100018357518'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache - Control': 'max - age = 0',
}


def getProductInfo(j_id):
    # file_name = 'C:\\Users\\Terry\\PycharmProjects\\getJD\\product_info\\' + str(j_id) + '.txt'
    # file = open(file_name, 'w', encoding='utf-8')
    url = 'https://wq.jd.com/commodity/itembranch/getspecification?callback=commParamCallBackA&skuid=' + str(j_id)
    rsp = rq.get(url, headers=header)
    result = rsp.text
    result = result[19: -2]
    result = result.replace('\n\t', '')
    result = json.loads(result)
    result = result['data']['propGroups']
    group_list = []
    info_str = ""
    for i in result:
        atts_list = {
            i['groupName']: []
        }
        for j in i['atts']:
            atts = {
                str(j['attName']): str(j['vals'][0])
            }
            # file.write(str(j['attName']) + ',' + str(j['vals'][0]) + '\n')
            info_str += str(j['attName']) + ':' +str(j['vals'][0]) + '\n'
            atts_list[i['groupName']].append(atts)
        group_list.append(atts_list)
    return info_str

getProductInfo(100018357518)
