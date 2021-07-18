import pandas as pd
import numpy as np

data = {"one": np.random.randn(4), "two": np.linspace(1, 4, 4), "three": ['zhangsan', '李四', 999, 0.1]}
df = pd.DataFrame(data, index=[1, 2, 3, 4])

df.to_excel("test.xlsx")
