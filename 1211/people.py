import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager

path = "C:\\Windows\\Fonts\\LG_Smart_UI-Light.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

file_name = "./1211/연령별인구현황.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")

# print(data.head())

region_name = input("검색하고 싶은 지역명을 입력하세요: ")
data = data.rename(columns={"행정구역": "지역명"})  # 지역으로 검색하기 위해서

age_columns = [col for col in data.columns if "세" in col]

# 숫자로 변환
for col in age_columns:
    data[col] = data[col].str.replace(",", "").astype(int)

# 지역별 필터링
# contains 문자열 데이터 필터링, 특정 패턴을 찾을때
region_data = data[data["지역명"].str.contains(region_name, na=False)]

# na 결측값을 추가할 지 묻는것, 기본이 True. case 영문의 대소문자 구분, 기본값은 True, 한글이니 생략.

# 데이터 추출

if region_data.empty:
    print(f"{region_data} 의 지역은 존재하지 않습니다. ")

age_groups = [col.split("_계_")[1] for col in age_columns]
result = region_data[age_columns].iloc[0]

# 그래프

plt.figure(figsize=(10, 8))
plt.plot(age_groups, result, marker="o", label=region_name)
plt.title(f"{region_name}의 연령별 인구수", fontsize=16, pad=10)
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
