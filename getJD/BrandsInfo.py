# -*- coding: UTF-8 -*-
import pandas as pd
import requests as rq
from matplotlib import pyplot as plt
import time
import os
from tqdm import *
import random
from bs4 import BeautifulSoup as Bs

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


def get_product_id_name(search_word):
    url = 'https://search.jd.com/Search?keyword=' + str(search_word) + '&qrst=1&stock=1&page=' + str(
        0) + '&s=56&click=0'
    search_page = rq.get(url, headers=getHeader())
    data = search_page.text
    soup = Bs(data, 'lxml')
    ul_result = soup.find('ul', class_='J_valueList v-fixed')
    brands_name = []
    final_brands_name = []
    li_result = soup.find_all('li')
    for li in li_result:
        a = li.select('a')
        # name = a.get('title')
        # brands_name.append(name)
    for brand in brands_name:
        index = brand.find('(')
        final_brand = brand[0: index]
        final_brands_name.append(final_brand)
    return final_brands_name


i = get_product_id_name('扫地机器人')

plt.rcParams['font.sans-serif'] = ['STZhongsong']
path = "C:\\Users\\Terry\\PycharmProjects\\getJD\\data"
xlsx_list = os.listdir(path)
product_name_list = []
y_num_list = []
for one_label in tqdm(xlsx_list):
    label = ''
    label = one_label.replace('.xlsx', '')
    product_name_list.append(label)
