"""
from bs4 import BeautifulSoup
import requests

html_url = "https://www.museum.go.kr/site/main/home"

res = requests.get(html_url)

soup = BeautifulSoup(res.text, "html.parser")

time = soup.select('li.info')

for i in time:
    print(i.text.strip())


from bs4 import BeautifulSoup
import requests

html_url = "https://m.etnews.com/20241203000250"

res = requests.get(html_url)

soup = BeautifulSoup(res.text, "html.parser")

title = soup.select('#article_title_h2')

date = soup.select('div.time > time')

article = soup.select('div.article_body p')

print(title[0].text)
print(date)
for i in article:
    print(i.text)


from bs4 import BeautifulSoup
import requests

html_url = "https://quotes.toscrape.com/page/2"

res = requests.get(html_url)

soup = BeautifulSoup(res.text, "html.parser")
quote = soup.select(".quote > .text")

# for i in quote:
#   print(i.text.strip())

text = [i.text.strip() for i in quote]
# print(text)

speak = soup.select(".author")
author = [i.text.strip() for i in speak]
# print(author)

zipped = list(zip(text, author))
print(zipped)
"""

from bs4 import BeautifulSoup
import requests

html_url = "https://finance.naver.com/marketindex/"

res = requests.get(html_url)

soup = BeautifulSoup(res.text, "html.parser")
data_div = soup.find('div', class_='market1')  # 'data' 클래스를 가진 div 찾기

print(data_div)
