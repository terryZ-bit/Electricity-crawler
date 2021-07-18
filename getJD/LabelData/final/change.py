# -*- coding: UTF-8 -*-
import pandas as pd
from tqdm import *
import numpy as np


def Normalization(x):
    return [(float(i) - min(x)) / float(max(x) - min(x)) for i in x]


name_i = "智能血压仪"
df_1 = pd.read_excel(name_i + ".xlsx")
df_2 = pd.read_csv(name_i + ".csv")
df_3 = pd.read_excel("评论1" + name_i + ".xlsx")

brands = df_2['品牌']
brands = brands.values.tolist()

names = df_1[['商品名']]
names = names.values.tolist()
list_brand_list = []
for brand in brands:
    list_brand_list.append([])
j = 0
for brand in brands:
    i = 0
    for name in names:
        if brand in name[0]:
            list_brand_list[j].append(i)
        i += 1
    j += 1

attention_list = []
ave_prise_list = []
discounts_list = []
volume_list = []
poor_commit_list = []
vitality_list = []
course_list = []

d2 = df_2['关注度']
d2 = d2.values.tolist()
total_attention = sum(d2)

d1 = df_2['得分']
d1 = d1.values.tolist()
course_list = d1
total_course = sum(d1)
ave_course = total_course / j
course_list = Normalization(d1)

# 计算关注度纲量
attention_list = Normalization(d2)
for brand in tqdm(list_brand_list):  # 每个品牌的商品list
    if len(brand) == 0:
        ave_prise_list.append(0.00000000000001)
        discounts_list.append(0.0000000000001)
        volume_list.append(0.00000000000001)
        poor_commit_list.append(0.000000000001)
        vitality_list.append(0.00000000000001)
        continue
    prise_sum = 0  # 求单个品牌产品价格之和
    cut_range_sum = 0.0  # 求单个品牌优惠率之和
    volume_sum = 0  # 求单个品牌销量总和
    poor_rate_sum = 0.0  # 求单个品牌差评率和
    vit_commit_rate_sum = 0.0
    for i in brand:  # 取出该品牌list中一个计算
        k = df_1.loc[i]
        p = df_3.loc[i]
        # 价格纲量计算部分
        prise = k[['活动价']]
        prise = prise.values.tolist()
        prise = prise[0]
        prise_sum += prise
        # 优惠力度计算部分
        re_prise = k[['原价']]
        re_prise = re_prise.values.tolist()
        re_prise = re_prise[0]
        cut_prise = re_prise - prise
        cut_range = cut_prise / re_prise
        cut_range_sum += cut_range
        # 销量纲量计算部分
        volume = p[['总评论数']]
        volume = volume.values.tolist()
        volume = volume[0]
        volume_sum += volume
        # 差评率纲量计算部分
        poor_rate = k[['差评率']]
        poor_rate = poor_rate.values.tolist()
        poor_rate = poor_rate[0]
        poor_rate_sum += poor_rate
        # 活跃度纲量计算部分
        if volume == 0:
            continue
        add_commit = p[['追加评价']]
        add_commit = add_commit.values.tolist()
        add_commit = add_commit[0]
        pic_commit = p[['晒图评价']]
        pic_commit = pic_commit.values.tolist()
        pic_commit = pic_commit[0]
        vio_commit = p[['视频评价']]
        vio_commit = vio_commit.values.tolist()
        vio_commit = vio_commit[0]
        vit_commit = add_commit + pic_commit + vio_commit
        vit_commit_rate = vit_commit / volume
        vit_commit_rate_sum += vit_commit_rate

    prise_brand_ave = prise_sum / len(brand)  # 每个品牌每个产品的产品平均价格
    ave_prise_list.append(prise_brand_ave)
    cut_range_ave = cut_range_sum / len(brand)  # 每个品牌每个产品平均优惠力度
    discounts_list.append(cut_range_ave)
    volume_list.append(volume_sum)  # 每个品牌销量和
    poor_rate_ave = poor_rate_sum / len(brand)  # 每个品牌每个产品平均差评率
    poor_commit_list.append(poor_rate_ave)
    vit_commit_rate_ave = vit_commit_rate_sum / len(brand)  # 每个品牌每个产品的平均活跃度
    vitality_list.append(vit_commit_rate_ave)

'''# 计算价格纲量
total_ave_prise = sum(ave_prise_list)  # 全部品牌的平均价格之和
ave_total_prise = total_ave_prise / j
ave_prise_list = list(map(lambda x: x / ave_total_prise, ave_prise_list))
# 计算优惠力度纲量
total_ave_cut = sum(discounts_list)
ave_total_cut = total_ave_cut / j
discounts_list = list(map(lambda x: x / ave_total_cut, discounts_list))
# 计算销量纲量
total_volume = sum(volume_list)
ave_total_volume = total_volume / j
volume_list = list(map(lambda x: x / ave_total_volume, volume_list))
# 计算差评率纲量
total_poor = sum(poor_commit_list)
ave_total_poor = total_poor / j
poor_commit_list = list(map(lambda x: x / ave_total_poor, poor_commit_list))
# 计算活跃度纲量
total_vit = sum(vitality_list)
ave_total_vit = total_vit / j
vitality_list = list(map(lambda x: x / ave_total_vit, vitality_list))'''

attention_list = Normalization(attention_list)
ave_prise_list = Normalization(ave_prise_list)
discounts_list = Normalization(discounts_list)
volume_list = Normalization(volume_list)
poor_commit_list = Normalization(poor_commit_list)
vitality_list = Normalization(vitality_list)

data = {
    '关注度': attention_list,
    '价格': ave_prise_list,
    '优惠力度': discounts_list,
    '销量': volume_list,
    '差评率': poor_commit_list,
    '活跃度': vitality_list,
    '得分': course_list
}

train_x = [
    attention_list,
    ave_prise_list,
    discounts_list,
    volume_list,
    poor_commit_list,
    vitality_list,
]

fp_train_x = open(str(name_i + 'train_x.txt'), 'w+')
fp_train_y = open(str(name_i + 'train_y.txt'), 'w+')
fp_train_x.write('[')
for i in range(len(train_x[0])):
    fp_train_x.write('[')
    for p in train_x:
        fp_train_x.write(str(p[i]) + ', ')
    fp_train_x.write('],\n')
fp_train_x.write(']')
fp_train_x.close()
fp_train_y.write('[')
for one in course_list:
    fp_train_y.write((str(one) + ','))
fp_train_y.write(']')
fp_train_y.close()
# df_4 = pd.DataFrame(data, index=brands)

# df_4.to_csv((str(name_i) + "品牌分析.csv"))
