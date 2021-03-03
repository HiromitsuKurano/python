import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

print(os.getcwd())
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\opendata")

df1 = pd.read_csv("Sample_20210303112919.csv")
df2 = pd.read_csv("Sample_20210303112952.csv")
df3 = pd.read_csv("Sample_20210303113004.csv")

print(df1.columns.values)
print(df2.columns.values)
print(df3.columns.values)

#違うデータソースからグラフを重ねて表示する
df1["年平均気温【℃】"].plot()
df2["最高気温（日最高気温の月平均の最高値）【℃】"].plot()
df3["最低気温（日最低気温の月平均の最低値）【℃】"].plot()

plt.ylim(-10,40)
plt.show()
