from matplotlib import pyplot as plt
import jieba
from wordcloud import WordCloud
import pandas as pd


def readFromXlsxToList():
    df = pd.read_excel("C:\\Users\\Terry\\PycharmProjects\\getJD\\data_1\\游戏手柄.xlsx", usecols=[1], names=None)
    df_li = df.values.tolist()
    result = ""
    for s_li in df_li:
        s_li_copy = s_li[0]
        s_1 = s_li_copy.replace("游戏", "")
        s_2 = s_1.replace("手柄", "")
        s_3 = s_2.replace("触摸", "")
        s_4 = s_3.replace("【", "")
        s_5 = s_4.replace("】", "")
        s_6 = s_5.replace("\t\n", "")
        # s_4 = s_3.replace("手写", " ")
        result += s_6
    print(len(result))
    return result


result = readFromXlsxToList()
wordlist_after_jieba = jieba.cut(result, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)
my_wordCloud = WordCloud(font_path='C:/Windows/Fonts/msyhbd.ttc', width=1200, height=1000, background_color='white',
                         max_font_size=150).generate(wl_space_split)
plt.imshow(my_wordCloud)
plt.axis("off")
plt.show()
