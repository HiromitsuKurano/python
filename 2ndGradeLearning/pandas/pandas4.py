import pandas as pd
import os
os.getcwd()
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap3")

#csvファイルを読み込む
df = pd.read_csv("test.csv")
print(df)

#国語の点数が高い順にソート
kokugoDesc = df.sort_values("国語", ascending=False)

#csvファイルを書き出す
kokugoDesc.to_csv("testEdited.csv", index=False, header=False)
