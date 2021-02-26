import pandas as pd
import os
os.getcwd()
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap3")
df = pd.read_csv("test.csv")
print(df)

#抽出
data_s = df[df["国語"] >= 90]
print("国語が90点以上\n", data_s)

data_c = df[df["数学"] < 70]
print("数学が70点未満\n", data_c)

#集計
print("数学の最高点 =", df["数学"].max())
print("数学の最低点 =", df["数学"].min())
print("数学の平均値 =", df["数学"].mean())
print("数学の中央地 =", df["数学"].median())
print("数学の合計 =", df["数学"].sum())

#ソート
kokugoAsc = df.sort_values("国語")
print(kokugoAsc)
kokugoDesc = df.sort_values("国語", ascending=False)
print(kokugoDesc)

#データ操作
print("行と列を入れ替える\n", df.T)
print("pythonのリストに変換する\n", df.values)
