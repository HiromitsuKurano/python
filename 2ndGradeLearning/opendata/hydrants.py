import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import folium
import os

print(os.getcwd())
os.chdir("C:\\Users\\kurano\\Documents\\python learning\\python\\2ndGradeLearning\\opendata")

#消火栓のcsvを読み込む
df = pd.read_csv("200.csv", encoding="shift-jis")

print(len(df))
print(df.columns.values)

hydrant = df[["緯度","経度"]].values
print(len(hydrant))
print(hydrant)

#地図上に表示する
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)
for data in hydrant:
    folium.Marker([data[0], data[1]]).add_to(m)
m.save("sabae.html")
