import pandas as pd
from matplotlib import pyplot as plt
import os
import random
import time
from tqdm import *
import re

plt.rcParams['font.sans-serif'] = ['STZhongsong']
path = "C:\\Users\\Terry\\PycharmProjects\\getJD\\data_1"
path_1 = "C:\\Users\\Terry\\PycharmProjects\\getJD\\data\\电子产品"
path_2 = "C:\\Users\\Terry\\PycharmProjects\\getJD\\data\\个人健康"
path_3 = "C:\\Users\\Terry\\PycharmProjects\\getJD\\data\\家居生活"
path_4 = "C:\\Users\\Terry\\PycharmProjects\\getJD\\data\\教育学习"
path_5 = "C:\\Users\\Terry\\PycharmProjects\\getJD\\data\\休闲娱乐"
xlsx_list = os.listdir(path_1)
xlsx_list.extend(os.listdir(path_2))
xlsx_list.extend(os.listdir(path_3))
xlsx_list.extend(os.listdir(path_4))
xlsx_list.extend(os.listdir(path_5))
x_label_list = []
y_num_list = []
for one_label in tqdm(xlsx_list):
    label = ''
    label = one_label.replace('.xlsx', '')
    x_label_list.append(label)
for one_xlsx in tqdm(xlsx_list):
    df = pd.read_excel(path + "\\" + one_xlsx, usecols=[4], names=None)
    list = df.values.tolist()
    data = 0
    for i in list:
        commit = ''
        commit = i[0]
        result = 0
        back = 0
        num_str = ''
        commit_replace = ''
        if '万' in commit:
            commit_replace = commit.replace('万+', '')
            back = random.randint(0, 9999)
            num_str = commit_replace + '0' * (4 - len(str(back))) + str(back)
            result = int(num_str)
        elif '+' in commit:
            commit_replace = commit.replace('+', '')
            back = random.randint(0, len(commit)-1)
            num_str = commit_replace[0] + '0' * (3 - len(str(back))) + str(back)
            result = int(num_str)
        else:
            result = int(commit)
        data += result
    y_num_list.append(data)
x_label = []
for i in x_label_list:
    pattern = re.compile('.{1,1}')
    j = '\n'.join(pattern.findall(i))
    x_label.append(j)
    print(j)
    print('---------')
colors = []
for i in range(6):
    colors.append('#FFD700')
for i in range(10):
    colors.append('#DAA520')
for i in range(23):
    colors.append('#ADD8E6')
for i in range(7):
    colors.append('#90EE90')
for i in range(5):
    colors.append('#87CEFA')
plt.bar(range(len(y_num_list)), y_num_list, 1, color=colors)
plt.xticks(range(len(y_num_list)), labels=x_label)
fp_1 = open('sal.txt', 'w+')
for i in range(len(x_label_list)):
    fp_1.write(str(x_label_list[i]) + ':' + str(y_num_list[i]) + '\n')
fp_1.close()
plt.xlabel('类别')
plt.ylabel('类别销量总数')
plt.tight_layout()
plt.show()
