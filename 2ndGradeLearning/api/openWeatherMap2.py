import requests
import json
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from datetime import datetime, timedelta, timezone

#タイムゾーンを指定
jst = timezone(timedelta(hours=+9), "JST")

#現在の天気を取得する
key = "ae39dcfef5ee03138b3b32add7a498c0"
url = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=meric"
url = url.format(city="TOKYO,JP", key=key)

jsondata = requests.get(url).json()
pprint(jsondata)

#グラフ用のデータフレームをつくる
df = pd.DataFrame(columns=["気温"])
for dat in jsondata["list"]:
    tokyoTime = str(datetime.fromtimestamp(dat["dt"], jst))[:-9]
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"] / 10
    print("日時：{tokyoTime}、天気：{weather}、気温；{temp}度".format(tokyoTime=str(tokyoTime)[:-9], weather=weather, temp=temp))
    df.loc[tokyoTime] = temp

#グラフを出力する
df.plot(figsize=(15,8))
plt.ylim(20,30)
plt.grid()
#plt.show()
