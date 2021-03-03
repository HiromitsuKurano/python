import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import folium
import os

print(os.getcwd())
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\opendata")

#消火栓のcsvを読み込む
df = pd.read_csv("898.csv")

print(len(df))
print(df.columns.values)

shops = df[["緯度","経度","店舗名(日本語)","住所"]].values

m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)
for data in shops:
    folium.Marker([data[0], data[1]], tooltip=data[2]+"</br>"+data[3]).add_to(m)
m.save("shops.html")
