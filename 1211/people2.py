# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from matplotlib import font_manager

# 폰트 설정
from matplotlib import font_manager
import pandas as pd
import matplotlib.pyplot as plt
path = "C:\\Windows\\Fonts\\LG_Smart_UI-Light.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

# # 파일 로드
# file_name = "./1211/연령별인구현황.csv"
# data = pd.read_csv(file_name, encoding="EUC-KR")

# region_name = input("지역명을 입력하세요: ")
# region_data = data[data["행정구역"]].str.contains(region_name, na=False)

# if region_data.empty:
#     print(f"{region_name} 존재하지 않음 ")

# male_columns = [
#     col for col in region_data.columns if '남' in col and '세' in col]
# female_columns = [
#     col for col in region_data.columns if '여' in col and '세' in col]

# print(male_columns)


# path = "C:\\Users\\shg02\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Medium.ttf"
# path = "Pretendard-Medium.ttf"
# font = font_manager.FontProperties(fname=path).get_name()
# plt.rc('font', family=font)

file_name = "./1211/연령별인구현황.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")
region_name = input("검색하고 싶은 지역명을 입력하세요: ")

# 지역검색
region_data = data[data["행정구역"].str.contains(region_name, na=False)]
if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

# male_columns = [ col for col in region_data.columns if "남" in col and "세" in col ]
female_columns = [
    col for col in region_data.columns if "여" in col and "세" in col]
male_columns = [col for col in region_data.filter(
    like="남_").columns if "총인구수" not in col and "연령구간인구수" not in col]
# filter() items=["2024년11월_남_40~49세", "2024년11월_남_70~79세"]

# for col in male_columns:
#     region_data[col] = region_data[col].astype(str).str.replace(",", "").astype(int)

# for col in female_columns:
#     region_data[col] = region_data[col].astype(str).str.replace(",", "").astype(int)

male_result = region_data[male_columns].iloc[0].astype(
    str).str.replace(",", "").astype(int)
# female_result =  region_data[female_columns].iloc[0].astype(str).str.replace(",", "").astype(int)
female_result = region_data[female_columns].iloc[0].apply(
    lambda x: int(str(x).replace(",", "")))
# apply(): 사용자 함수 정의

age_groups = [col.split("_남_")[1] for col in male_columns]


plt.figure(figsize=(10, 8))
plt.plot(age_groups, male_result, marker='o', label="남성", color="blue")
plt.plot(age_groups, female_result, marker='o', label="여성", color="red")


plt.title(f"{region_name}의 연령별 인구 수", fontsize=16, pad=10)
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.legend()
plt.show()
