
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

driver.get("https://danawa.com/")

search_box = driver.find_element(By.ID, "AKCSearch")
search_box.send_keys("노트북")
search_box.send_keys(Keys.ENTER)
time.sleep(3)

products = driver.find_elements(
    By.XPATH, '//*[@id="mainAdReader"]/ul/li/div/div[2]/p[2]/a')
prices = driver.find_elements(
    By.XPATH, '//*[@id="mainAdReader"]/ul/li/div/div[3]/div/a/div[2]/div/span[2]')

product_texts = [product.text for product in products]
price_texts = [price.text for price in prices]

for product, price in zip(product_texts, price_texts):
    print(f"제품명: {product}, 가격: {price}")

driver.quit()
