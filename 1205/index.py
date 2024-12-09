from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.agoda.com/ko-kr/?cid=1844104&ds=jfUj2STUAQf8j5wq")

time.sleep(10)

driver.find_element(By.XPATH, "//*[@id='textInput']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='destination_suggestion_card']").click()
time.sleep(3)

driver.find_element(
    By.XPATH, "//*[@id='DatePicker__Accessible']/div/div[2]/div[1]/div[3]/div[3]/div[6]/div/div/div/span").click()
time.sleep(3)

driver.find_element(
    By.XPATH, "//*[@id='DatePicker__Accessible']/div/div[2]/div[2]/div[3]/div[4]/div[1]/div/div/div").click()
time.sleep(3)

driver.find_element(
    By.XPATH, "//*[@id='Tabs-Container']/button/div/div/span").click()
time.sleep(3)

original_window = driver.current_window_handle
all_windows = driver.window_handles

# 새 탭으로 전환
# driver.switch_to.window(driver.window_handles) #최근에 열린 탭으로 전환

for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break

try:

    hotel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@data-selenium='hotel-name']"))
    )
    print("호텔:", hotel.text)

    price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@data-selenium='display-price']"))
    )
    print("가격:", price.text)
except Exception as e:
    print("에러 발생:", e)

"""
products = driver.find_elements(
    By.XPATH, '//*[@id="mainAdReader"]/ul/li/div/div[2]/p[2]/a')
prices = driver.find_elements(
    By.XPATH, '//*[@id="mainAdReader"]/ul/li/div/div[3]/div/a/div[2]/div/span[2]')

product_texts = [product.text for product in products]
price_texts = [price.text for price in prices]

for product, price in zip(product_texts, price_texts):
    print(f"제품명: {product}, 가격: {price}")

driver.quit()
"""
