import requests
import json
from pprint import pprint

#現在の天気を取得する
key = "ae39dcfef5ee03138b3b32add7a498c0"
url = "https://api.openweathermap.org/data/2.5/weather?q={zipcode}&appid={key}&lang=ja&units=meric"
url = url.format(zipcode="164-0012,JP", key=key)
print(url)

jsondata = requests.get(url).json()
pprint(jsondata)

print(jsondata["name"])
print(jsondata["main"]["temp"])
print(jsondata["weather"][0]["description"])
print(jsondata["weather"][0]["main"])
