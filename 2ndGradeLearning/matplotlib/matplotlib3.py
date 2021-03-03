import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

#現在のディレクトリを表示
print(os.getcwd())
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap3")

#csvファイルを読み込む
df = pd.read_csv("test.csv", index_col=0)

colorList = ["skyblue", "steelblue", "tomato", "cadetblue", "orange", "sienna"]
df.T.plot.bar(color = colorList)
#plt.legend(loc="lower right")
#plt.show()

os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\matplotlib")
plt.savefig("matplot.png")
#atomとhydrogenの環境だと出力がうまくいかない。IDLEから実行すればうまく出力される。
