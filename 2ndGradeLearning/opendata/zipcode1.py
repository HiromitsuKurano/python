import pandas as pd
import os

#現在のディレクトリを表示
print(os.getcwd())

#csvを読み込む
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap4")
df = pd.read_csv("FEH_00200524_210301170404.csv", header=None, encoding="shift_JIS")

print(len(df))
print(df.columns.values)

#「2」の列が「1600006」の住所を抽出する
results1 = df[df[2] == 1600006]
print(results1[[2,6,7,8]])

result2 = df[df[7].str.contains("中野")]
print(result2[[2,6,7,8]])
