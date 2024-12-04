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

html_url = "https://finance.naver.com/item/main.naver?code=000660"

res = requests.get(html_url)

soup = BeautifulSoup(res.text, "html.parser")

company = soup.select('.wrap_company h2 a')

values = soup.select('.rate_info dd')

print(f"회사: {company[0].text.strip()}")
print(f"현재 시세: {values[0].text.strip()}")
print(f"가격 변화: {values[1].text.strip()}")
print(f"변동률: {values[2].text.strip()}")
