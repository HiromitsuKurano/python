import pandas as pd
import matplotlib as plt
import japanize_matplotlib
import os

#現在のディレクトリを表示
print(os.getcwd())

#csvを読み込む
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\opendata")
df = pd.read_csv("FEH_00200524_210301170404.csv", index_col="全国・都道府県", encoding="shift_JIS")

print(df.loc["全国"]["2019年"])
print(df.columns.values)

df = df.drop("全国", axis=0)

#データ内のカンマを削除、数値に変換
df["2019年"] = pd.to_numeric(df["2019年"].str.replace(",", ""))
df = df.sort_values("2019年", ascending=False)

#2019年のデータで棒グラフをつくる
df["2019年"].plot.bar(figsize=(10,6))
#plt.show()

#人口増減データをつくる
df["2018年"] = pd.to_numeric(df["2018年"].str.replace(",", ""))
df["増減データ"] = df["2019年"] - df["2018年"]
df = df.sort_values("増減データ", ascending=False)
df["増減データ"].plot.bar(figsize=(10,6))
#plt.show()
