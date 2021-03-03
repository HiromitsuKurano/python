import pandas as pd
import openpyxl
import os

print(os.getcwd())
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\excel")

#csvを読み込む
df = pd.read_excel("csv_to_excel2.xlsx")
print(df)

#複数シートのエクセルを読み込む。　最初のシートが読み込まれる。
df = pd.read_excel("csv_to_excel3.xlsx")
print(df)

#任意のシートを読み込む
df = pd.read_excel("csv_to_excel3.xlsx", sheet_name="国語でソート")
print(df)
