import os
import requests
import json
from pprint import pprint

print(os.getcwd())
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\python2nen_sample\\chap5")

with open("test2.json", mode="r") as f:
    jsondata = json.loads(f.read())
    print("1つ目のオブジェクト=", jsondata[0])
    print("都市名=", jsondata[0]["name"])
    print("緯度=", jsondata[0]["coord"]["lat"])
    print("経度=", jsondata[0]["coord"]["lon"])
