"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('고양이')
image_tab = driver.find_element(
    By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div')

time.sleep(3)

image_list = driver.find_elements(
    By.XPATH, "//img[@class='rg_i Q4LuWd']")  # 이미지 SRC 찾기
image_srcs = [img.get_attribute('src')
              for img in image_list if img.get_attribute('src')]


image_count = 0
for src in image_srcs:
    if image_count < 10:
        if src:
            img_data = requests.get(src).content

            img_name = f"image_{image_count + 1}.jpg"
            with open(img_name, 'wb') as file:
                file.write(img_data)
            image_count += 1
    else:
        break

print(f"이미지 {image_count}개 저장완료")

driver.quit()
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os
