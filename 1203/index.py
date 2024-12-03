# 웹스크래핑 (크롤링)
from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <div id="content">
            <ul class="industry">
                <li>인공지능</li>
                <li>빅데이터</li>
                <li>신재생에너지</li>
            </ul>
            <ul class="comlang">
                <li>Python</li>
                <li>C++</li>
                <li>javascript</li>
            </ul>
        </div>
    </body>
</html>
"""


soup = BeautifulSoup(html_str, "html.parser")
"""
print(soup.li.text)
first_ul = soup.find('ul')
print(first_ul)
print(first_ul.text)  # 태그없이 텍스트 출력

all_ul = soup.find_all('ul')  # 구버전에서는 findAll
print(all_ul[1].text)

class_ul = soup.find('ul', attrs={'class': "comlang"})
print(class_ul)
"""

first_ul = soup.select_one("ul.industry")
print(first_ul.text)

all_ul = soup.select("div > ul")
print(all_ul)
