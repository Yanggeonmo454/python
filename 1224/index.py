from scipy.stats import pearsonr
import pandas as pd
import numpy as np

# CSV 파일 읽기
file_path = "C:\\Users\\didrj\\documents\\workspace\\python\\1224\\제주도 시간별 기상자료 및 발전수요량(20230101_20240930) (1).csv"

data = pd.read_csv(file_path, encoding='EUC-KR')

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'], errors='coerce')

# 결측값을 '일사(MJ/m2)' 0으로 채운 후, 데이터를 필터링
data['일사(MJ/m2)'] = data['일사(MJ/m2)'].fillna(0)

# 2023-05부터 2023-05까지의 데이터만 필터링 (날짜와 시간 모두 포함)
filtered_data = data[(data['일시'] >= '2023-10-01') &
                     (data['일시'] < '2023-11-01')].copy()

# 데이터 확인
print("필터링된 데이터:")
print(filtered_data[['일시', '발전수요량', '기온(°C)', '일사(MJ/m2)']].head())

# 결측값을 각 열의 평균값으로 대체
filtered_data["발전수요량"] = filtered_data["발전수요량"].fillna(
    filtered_data["발전수요량"].mean())
filtered_data["기온(°C)"] = filtered_data["기온(°C)"].fillna(
    filtered_data["기온(°C)"].mean())

# 결측값 처리 후 데이터 확인
print("\n결측값 처리 후 데이터:")
print(filtered_data[['일시', '발전수요량', '기온(°C)', '일사(MJ/m2)']].head())

# '일사(MJ/m2)'가 0인 데이터와 0이 아닌 데이터 분리
sunshine_zero = filtered_data[filtered_data['일사(MJ/m2)'] == 0]
sunshine_non_zero = filtered_data[filtered_data['일사(MJ/m2)'] > 0]

# '일사(MJ/m2)'가 0인 데이터에 대한 피어슨 상관계수
correlation_pearson_sunshine_zero = sunshine_zero["발전수요량"].corr(
    sunshine_zero["일사(MJ/m2)"])

# '일사(MJ/m2)'가 0이 아닌 데이터에 대한 피어슨 상관계수
correlation_pearson_sunshine_non_zero = sunshine_non_zero["발전수요량"].corr(
    sunshine_non_zero["일사(MJ/m2)"])

# 결과 출력
print(f"\n일사(MJ/m2)가 0인 데이터에서 발전수요량과 일사(MJ/m2)의 피어슨 상관계수: {
      correlation_pearson_sunshine_zero:.2f}")
print(f"\n일사(MJ/m2)가 0이 아닌 데이터에서 발전수요량과 일사(MJ/m2)의 피어슨 상관계수: {
      correlation_pearson_sunshine_non_zero:.2f}")

# 필터링된 데이터 (filtered_data)에서 '발전수요량'과 '일사(MJ/m2)' 열을 사용
# 일사(MJ/m2)가 0이 아닌 데이터로 필터링
non_zero_data = filtered_data[filtered_data['일사(MJ/m2)'] > 0]

# 피어슨 상관계수와 p-value 계산
correlation, p_value = pearsonr(
    non_zero_data['발전수요량'], non_zero_data['일사(MJ/m2)'])

# 결과 출력
print(f"피어슨 상관계수: {correlation:.2f}")
print(f"p-value: {p_value:.4f}")
