from pathlib import Path
from bs4 import BeautifulSoup
import requests
import urllib
import time

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

folder = Path("download")
folder.mkdir(exist_ok = True)

#すべてのimgタグを検索し、リンクを取得する。
pic_urls = []
pic_names = []
for element in soup.find_all("img"):
    src = element.get("src")

    img_url = urllib.parse.urljoin(load_url, src)
    pic_urls.append(img_url)
    filename = img_url.split("/")[-1]
    pic_names.append(filename)

print(pic_urls)
print(pic_names)

for i in range(3):
    print(i)
    pic = requests.get(pic_urls[i])
    filename = folder.joinpath(pic_names[i])

    with open(filename, "wb") as f:
        f.write(pic.content)

    #ループの終了処理　1秒待つ
    i += 1
    time.sleep(1)
