
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = "yanggeonmo454"
password = "gtsang0409!"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://github.com/login")


driver.find_element(By.ID, "login_field").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.NAME, "commit").click()

time.sleep(2)

driver.get("https://github.com/" + username)

user_name = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[1]/header/div[1]/div[1]/div/div[2]/nav/ul/li/a/span").text
print("사용자 이름:", user_name)

repositories = driver.find_element(
    By.XPATH, '//*[@id="repositories-tab"]/span[2]')
print("repositories:", repositories.text)

repos = driver.find_elements(By.CSS_SELECTOR, '.repo')
for repos in repos:
    print("repository_name", repos.text)
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 첫 번째 페이지 열기
driver.get("https://www.coupang.com/")
time.sleep(3)  # 페이지 로딩 대기

try:
    # 검색창 찾기 및 검색어 입력
    search_box = driver.find_element(By.ID, "headerSearchKeyword")
    search_box.send_keys("노트북")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)  # 검색 결과 로딩 대기

    # 첫 번째 페이지에서 상품명과 가격 정보 추출
    products = driver.find_elements(By.CLASS_NAME, "name")
    prices = driver.find_elements(By.CLASS_NAME, "price-value")

    for product, price in zip(products, prices):
        product_name = product.text
        price_value = int(price.text.replace(",", ""))

        if price_value >= 500000:
            print(f"상품명: {product_name}, 가격: {price_value}원")

except Exception as e:
    print(f"첫 번째 페이지에서 문제가 발생했습니다: {e}")
    # 두 번째 페이지로 이동
    print("두 번째 페이지로 이동합니다...")
    driver.get(
        "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user")
    time.sleep(5)  # 두 번째 페이지 로딩 대기

    # 두 번째 페이지에서 상품명과 가격 정보 추출
    products = driver.find_elements(By.CLASS_NAME, "name")
    prices = driver.find_elements(By.CLASS_NAME, "price-value")

    for product, price in zip(products, prices):
        product_name = product.text
        price_value = int(price.text.replace(",", ""))

        if price_value >= 500000:
            print(f"상품명: {product_name}, 가격: {price_value}원")

# 브라우저 종료
driver.quit()
