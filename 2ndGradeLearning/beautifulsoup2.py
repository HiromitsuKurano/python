import requests
from bs4 import BeautifulSoup
import urllib

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
tags = soup.find_all("a")

filename = "linklist.txt"
with open(filename, "w") as f:
    #すべてのaタグを検索し、リンクを絶対URLで書き出す
    for tag in tags:
        url = tag.get("href")
        link_url = urllib.parse.urljoin(load_url, url)
        f.write(tag.text + "\n")
        f.write(link_url + "\n")
        f.write("\n")
