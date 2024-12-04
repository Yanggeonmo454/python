""""
from bs4 import BeautifulSoup
import requests

html_url = ("https://finance.naver.com/marketindex/")

res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

USD = soup.select_one("#exchangeList .usd .value")
print("USD: ", USD.text)

JPY = soup.select_one("#exchangeList .jpy .value")
print("JPY :", JPY. text)

EUR = soup.select_one("#exchangeList .eur .value")
print("EUR: ", EUR. text)

CNY = soup.select_one("#exchangeList .cny .value")
print("CNY: ", CNY. text)


def stock(code):
    from bs4 import BeautifulSoup
    import requests

    # f-string 사용
    html_url = f"https://finance.naver.com/item/main.naver?code={code}"

    res = requests.get(html_url)
    soup = BeautifulSoup(res.text, "html.parser")

    company = soup.select_one(".wrap_company > h2 > a")

    price = soup.select_one(".today > .no_today .blind")

    dprice = soup.select_one(".today > .no_exday .blind")

    print(company.text if company else "Company name not found")
    print(price.text if price else "Price not found")
    print(dprice.text if dprice else "Price difference not found")


stock("035720")
"""
