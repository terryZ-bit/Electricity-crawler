# -*- coding: UTF-8 -*-
import os

import requests as rq
from bs4 import BeautifulSoup as Bs
import random
import getProxy as gP
import pandas as pd
import time
import test_getProductInfo as gInfo
from selenium import webdriver
from tqdm import *

user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 '
    'Safari/537.36 Edg/90.0.818.56',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 '
    'Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 '
    'Core/1.70.3869.400 QQBrowser/10.8.4394.400',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 '
    'OPR/76.0.4017.123',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 '
    'Safari/537.36',
    'Windows / IE 10: Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2'
    '.XMetaSr1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR '
    '3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E',
]
proxy_list = []


def getProxy():
    time.sleep(1)
    return random.choice(proxy_list)


def getHeader():
    header = {
        'User-Agent': random.choice(user_agent),
    }
    return header


def getPrice(product_id):
    price_url = 'https://p.3.cn/prices/mgets?skuIds=J_' + product_id
    price_rsp = rq.get(price_url)
    price_result = price_rsp.json()
    price = {
        '活动价': str(price_result[0]['p']),
        '原价': str(price_result[0]['m'])
    }
    return price


def get_product_id_name(page_num, search_word):
    url = 'https://search.jd.com/Search?keyword=' + str(search_word) + '&qrst=1&stock=1&page=' + str(
        page_num) + '&s=56&click=0'
    search_page = rq.get(url, headers=getHeader())
    data = search_page.text
    soup = Bs(data, 'lxml')
    li_result = soup.find_all('li', class_='gl-item')
    product_id = []
    product_name = []
    for i in li_result:
        product_id.append(i.get('data-sku'))
        name = i.find('div', class_='p-name p-name-type-2')
        name = name.select('em')
        name = name[0]
        name = name.text
        product_name.append(name)
    return product_id, product_name


def getCommit(product_id):
    time.sleep(2)
    url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=' + str(product_id)
    commit_result = {}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
    }  # ''' proxies=gP.getProxy(),'''
    while 1:
        try:
            commit_rsp = rq.get(url, headers=getHeader())
        except rq.exceptions.ProxyError or rq.exceptions.SSLError or rq.exceptions.ConnectionError:
            continue
        if len(commit_rsp.text) > 10:
            break
        else:
            continue
    commit_result = commit_rsp.json()
    commit_r = {
        '总评论数': str(commit_result['CommentsCount'][0]['CommentCountStr']),
        '好评数': str(commit_result['CommentsCount'][0]['GoodCountStr']),
        '好评率': str(commit_result['CommentsCount'][0]['GoodRate']),
        '差评数': str(commit_result['CommentsCount'][0]['PoorCountStr']),
        '差评率': str(commit_result['CommentsCount'][0]['PoorRate']),
        '晒图评价': str(commit_result['CommentsCount'][0]['ShowCountStr']),
        '视频评价': str(commit_result['CommentsCount'][0]['VideoCountStr']),
        '追评': str(commit_result['CommentsCount'][0]['AfterCountStr']),
    }
    return commit_r


all_commit_list = []
good_commit_list = []
good_rate_list = []
bad_commit_list = []
bad_rate_list = []
pic_commit_list = []
video_commit_list = []
append_commit_list = []
real_price_list = []
ex_price_list = []
all_id_list = []
all_name_list = []
address_list = []

'''goods_type_list = [
    '智能手表', '智能空调', '智能儿童手表', '互联网监控', '智能门锁', '蓝牙耳机', '平板电脑', '签到机',
    '智能机器人', '智能马桶', '智能台灯', '智能插座', '智能电视', '智能手机', '智能人体秤', '智能投影仪', '智能开关', '智能电烤箱',
    '智能高压锅', '智能电饭煲', '智能洗衣机', '智能洗手机', '智能水龙头', '智能门铃', '智能手环', '智能窗帘', '智能遥控器', '智能眼镜',
    '智能垃圾桶', '智能床', '智能按摩椅', '智能枕头', '智能轮椅', '智能呼啦圈', 'VR眼镜', '数位板', '无线鼠标', '无线键盘',
    '移动热点', '磁吸充电宝', '智能椅子', '智能衣柜', '游戏手柄', '扫地机器人', '写字机器人', '智能白板', '擦窗机器人', '空气净化器',
    '早教机器人', '干衣器', '电子书', '智能血压仪', '智能血糖仪', '无人机', '智能麦克风', '便携显示器', '无线充电器', '助听器',
    '智能洗碗机'
]'''

goods_type_list = [
    '云台', '点读笔', '行车记录仪'
]
for key_word in goods_type_list:
    all_commit_list = []
    good_commit_list = []
    good_rate_list = []
    bad_commit_list = []
    bad_rate_list = []
    pic_commit_list = []
    video_commit_list = []
    append_commit_list = []
    real_price_list = []
    ex_price_list = []
    all_id_list = []
    all_name_list = []
    address_list = []
    all_info_list = []
    for i in tqdm(range(0, 80, 2)):
        proxy_list = []
        id_list, name_list = get_product_id_name(i, key_word)
        all_id_list.extend(id_list)
        all_name_list.extend(name_list)
        count = 0
        for j in id_list:
            # print(count)
            count += 1
            price = getPrice(str(j))
            commit = getCommit(str(j))
            product_info = gInfo.getProductInfo(str(j))
            all_commit_list.append(commit['总评论数'])
            good_commit_list.append(commit['好评数'])
            good_rate_list.append(commit['好评率'])
            bad_commit_list.append(commit['差评数'])
            bad_rate_list.append(commit['差评率'])
            pic_commit_list.append(commit['晒图评价'])
            video_commit_list.append(commit['视频评价'])
            append_commit_list.append(commit['追评'])
            real_price_list.append(price['活动价'])
            ex_price_list.append(price['原价'])
            all_info_list.append(product_info)
        # print(i)
    data = {
        '商品名': all_name_list,
        '活动价': real_price_list,
        '原价': ex_price_list,
        '总评论数': all_commit_list,
        '好评数': good_commit_list,
        '好评率': good_rate_list,
        '差评数': bad_commit_list,
        '差评率': bad_rate_list,
        '晒图评价': pic_commit_list,
        '视频评价': video_commit_list,
        '追加评价': append_commit_list,
        '商品参数': all_info_list
    }
    df = pd.DataFrame(data, index=all_id_list)
    xlsx_name = key_word + '.xlsx'
    df.to_excel(xlsx_name)
    print('success')
