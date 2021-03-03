import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

#現在のディレクトリを表示
print(os.getcwd())
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap3")

#csvファイルを読み込む
df = pd.read_csv("test.csv", index_col=0)

#国語の棒グラフをつくる
df["国語"].plot.barh()
#plt.legend(loc="lower left")
#plt.show()

#国語と数学の棒グラフ
df[["国語","数学"]].plot.barh()
#plt.legend(loc="lower left")
#plt.show()

#C子の棒グラフをつくる
df.loc["C子"].plot.barh()
#plt.legend(loc="lower left)
#plt.show()

#C子の円グラフを作る
df.loc["C子"].plot.pie(labeldistance=0.6)
#plt.legend(loc="lower left)
#plt.show()

df.T.plot.bar()
