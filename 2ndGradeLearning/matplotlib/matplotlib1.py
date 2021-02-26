import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

#ディレクトリを移動
os.getcwd()
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap3")

#csvファイルを読み込む
df = pd.read_csv("test.csv", index_col=0)

#グラフ作成、表示
df.plot.bar()
plt.legend(loc="lower right")
plt.show()

df.plot.barh()
plt.legend(loc="lower left")
plt.show()
