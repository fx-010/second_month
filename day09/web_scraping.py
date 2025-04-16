import requests
from bs4 import BeautifulSoup
import pandas as pd

# 获取信息
url = "http://quotes.toscrape.com/"
respone = requests.get(url)
html = respone.text

# 解析网页
soup = BeautifulSoup(html,"html.parser")
quotes = soup.find_all('span',class_="text")
authors = soup.find_all('small',class_="author")

# 提取文本数据
quotes_list = [q.get_text() for q in quotes]
authors_list = [a.get_text() for a in authors]

# 合成 DataFrame 并保存 CSV
df = pd.DataFrame({'quotes':quotes_list,'authors':authors_list})
df.to_csv("quotes_scraped.csv")
print("已保存数据到 quotes_scraped.csv")