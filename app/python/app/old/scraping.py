# coding: utf-8
import requests as req
from bs4 import BeautifulSoup

# yahooNewsのトピックをスクレイピング
target = 'https://news.yahoo.co.jp/topics/top-picks'
r = req.get(target)
soup = BeautifulSoup(r.text, 'html.parser')

# li要素のみ取得
# topik_link = soup.find_all("li", class_="newsFeed_item")
# topik_anker = soup.find_all("a", class_="newsFeed_item_link")
topik_text = soup.find_all("div", class_="newsFeed_item_title")


for i in topik_text:
    print(i.getText())
