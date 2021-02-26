import pandas as pd
import os
os.getcwd()
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap3")
df = pd.read_csv("test.csv")
print(df)

#表データの情報を表示
print("データの件数 =", len(df))
print("項目名 =", df.columns.values)
print("インデックス =", df.index.values)

print("国語の列データ\n", df["国語"])
print("国語の列データ\n", df[["国語","数学"]])

df.loc[0]
df.loc[[0,1]]
df.loc[2]["国語"]

print("C子のデータ\n", df.loc[2])
print("C子とD郎のデータ\n", df.loc[[2,3]])
print("C子の国語データ\n", df.loc[2]["国語"])
