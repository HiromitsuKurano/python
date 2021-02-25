import requests
from bs4 import BeautifulSoup

load_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

tags = soup.find_all(class_= "topics")
print(tags)

tags2 = tags[0].find_all("a")
print(tags2)
for tag in tags2:
    print(tag.text)
