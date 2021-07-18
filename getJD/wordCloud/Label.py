import pandas as pd
from pandas.core.frame import DataFrame

name = "VR眼镜"
label_1 = '体感'
label_2 = '虚拟现实'
path = "C:\\Users\\Terry\\PycharmProjects\\getJD\\data_1\\"
to_path = 'C:\\Users\\Terry\\PycharmProjects\\getJD\\LabelData\\休闲娱乐\\'


def readFromXlsxToList():
    df = pd.read_excel(path + name + '.xlsx', usecols=[1, 3], names=None)
    df_li = df.values.tolist()
    return df_li


r_list = []
r_list = readFromXlsxToList()
r_list.insert(0, ['名称', '价格', label_1 + ' Or ' + label_2])
for i in range(1, len(r_list)):
    j = r_list[i]
    if label_1 in j[0] and label_2 in j[0]:
        r_list[i].append('1')
    elif label_1 in j[0]:
        r_list[i].append('2')
    elif label_2 in j[0]:
        r_list[i].append('3')
    else:
        r_list[i].append('0')
data = DataFrame(r_list)
data.to_excel(to_path + name + '.xlsx', header=None)
