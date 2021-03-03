import pandas as pd
import openpyxl
import os

print(os.getcwd())
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap3")

#csvを読み込む
df = pd.read_csv("test.csv")
kokugo = df.sort_values("国語", ascending=False)

os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\excel")

#そのまま出力
kokugo.to_excel("csv_to_excel1.xlsx")

#インデックスなし、シート名を国語にして出力
kokugo.to_excel("csv_to_excel2.xlsx", index=False, sheet_name="国語")

with pd.ExcelWriter("csv_to_excel3.xlsx") as writer:
    df.to_excel(writer, index=False, sheet_name="元のデータ")
    kokugo.to_excel(writer, index=False, sheet_name="国語でソート")
