import pandas as pd
import os
from tqdm import *
import random

path = "C:\\Users\\Terry\\PycharmProjects\\getJD\\LabelData\\final"
xlsx_list = os.listdir(path)
x_label_list = []

for one_label in xlsx_list:
    label = ''
    label = one_label.replace('.xlsx', '')
    x_label_list.append(label)

for one_xlsx in tqdm(xlsx_list):
    list_one_label = []
    for k in trange(4, 9):
        list_one_co = []
        df = pd.read_excel(path + "\\" + one_xlsx, usecols=[k], names=None)
        list = df.values.tolist()
        for i in list:
            commit = ''
            commit = i[0]
            result = 0
            back = 0
            num_str = ''
            commit_replace = ''
            if r"\." in commit:
                commit_replace = commit.replace('万+', '')
                back = random.randint(0, 999)
                commit_replace = float(commit_replace)
                commit_replace = commit_replace * 10
                commit_replace = int(commit_replace)
                num_str = str(commit_replace) + '0' * (3 - len(str(back))) + str(back)
                result = int(num_str)
                list_one_co.append(result)
            if '万+' in commit:
                commit_replace = commit.replace('万+', '')
                back = random.randint(0, 9999)
                num_str = commit_replace + '0' * (4 - len(str(back))) + str(back)
                result = int(num_str)
                list_one_co.append(result)
            elif '+' in commit:
                commit_replace = commit.replace('+', '')
                if len(commit_replace) <= 2:
                    num_str = commit_replace[0] + str(random(0, 9))
                    result = int(num_str)
                    list_one_co.append(result)
                else:
                    back = random.randint(0, len(commit) - 1)
                    num_str = commit_replace[0] + '0' * (3 - len(str(back))) + str(back)
                    result = int(num_str)
                    list_one_co.append(result)
            else:
                result = int(commit)
                list_one_co.append(result)
        list_one_label.append(list_one_co)
    data_final = {
        '总评论数': list_one_label[0],
        '好评数': list_one_label[1],
        '差评数': list_one_label[2],
        '晒图评价': list_one_label[3],
        '视频评价': list_one_label[4],
        '追加评价': list_one_label[5]
    }
    df_3 = pd.DataFrame(data_final)
    xlsx_name = '评论1' + one_xlsx
    df_3.to_excel(xlsx_name)
    print('success')
