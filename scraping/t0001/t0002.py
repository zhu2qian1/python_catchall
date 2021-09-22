import requests
from bs4 import BeautifulSoup

# yahooのサイトから情報取得
response = requests.get("https://news.yahoo.co.jp")

# レスポンスを成形
html = BeautifulSoup(response.content, "html.parser")

# 特定のキーワードを抽出
for a in html.select(".topicsList .topicsListItem  a"):
    # 出力処理
    print(a["href"], list(a.strings)[0])
