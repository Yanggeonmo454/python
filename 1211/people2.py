import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 폰트 설정
path = "C:\\Windows\\Fonts\\LG_Smart_UI-Light.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

# 파일 로드
file_name = "./1211/연령별인구현황.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")

region_name = input("지역명을 입력하세요: ")
region_data = data[data["행정구역"]].str.contains(region_name, na=False)

if region_data.empty:
    print(f"{region_name} 존재하지 않음 ")

male_columns = [
    col for col in region_data.columns if '남' in col and '세' in col]
female_columns = [
    col for col in region_data.columns if '여' in col and '세' in col]

print(male_columns)
