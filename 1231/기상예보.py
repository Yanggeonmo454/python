from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# WebDriverManager를 이용한 크롬 드라이버 설치 및 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 기상청 홈페이지로 이동
driver.get("https://www.weather.go.kr/w/weather/forecast/short-term.do?stnId=184")

# 열린 URL 출력
print("현재 열린 URL:", driver.current_url)

# '내일' 클릭하기 - '내일' 날짜를 포함하는 <em> 태그를 클릭
wait = WebDriverWait(driver, 10)
tomorrow_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "h4.todaytomorrow em")))
tomorrow_button.click()

# 열린 URL 출력 (내일 클릭 후 URL 확인)
time.sleep(2)  # 페이지가 전환되도록 잠시 기다림
print("내일 클릭 후 열린 URL:", driver.current_url)

# 24시간 기온 데이터가 로드될 때까지 대기
wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, "text[data-z-index='1']")))

# 모든 기온 정보 가져오기
temperatures = driver.find_elements(By.CSS_SELECTOR, "text[data-z-index='1']")

# 기온 값을 리스트로 저장
temperature_values = [temp.text for temp in temperatures]

# 데이터 출력
print("24시간 기온 데이터:")
for i, temp in enumerate(temperature_values):
    print(f"시간 {i+1}: {temp}")

# 드라이버 종료
driver.quit()
