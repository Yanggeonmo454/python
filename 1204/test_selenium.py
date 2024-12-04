from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# 옵션 개체
options = Options()
# 옵션 추가
options.add_argument("--start-maxmized")
# options.add_argument("--headless")

# WebDriverManager로 자동으로 Chromedriver 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 웹페이지 열기
driver.get("https://google.com")
print(driver.title)
# 무한 스크롤 페이지 스크롤 내리기
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(5)

search_input = driver.find_element(By.NAME, "q")
print(search_input)


search_input.send_keys("파이썬코딩연습")

"""

email_text = driver.find_element(
    By.XPATH, '//*[@id="gb"]/div[2]/div[3]/div[1]/div/div[1]/a')
href = email_text.get_attribute("href")

print(href)
"""
search_input.send_keys(Keys.ENTER)

time.sleep(2)

driver.save_screenshot("save.png")
