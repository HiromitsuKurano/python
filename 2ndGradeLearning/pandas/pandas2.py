import pandas as pd
import os
os.getcwd()
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap3")
df = pd.read_csv("test.csv")
print(df)

df["美術"] = [68, 73, 82, 77, 94, 96]
df.loc[6] = ["G恵", 90, 92, 94, 96, 92,98]

print("行データ（G恵）を追加\n", df)
print("名前の列を削除\n", df.drop("名前", axis=1))
print("インデックス2の行を削除\n", df.drop(2, axis=0))
