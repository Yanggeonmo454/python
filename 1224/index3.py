import pandas as pd
import matplotlib.pyplot as plt

# '휴일포함.csv' 파일 경로 설정
file_path = "C:\\Users\\didrj\\documents\\workspace\\python\\1224\\휴일포함_수정_재정렬.csv"

# CSV 파일 읽기
data = pd.read_csv(file_path, encoding='EUC-KR')

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'], errors='coerce')

# '년', '월' 컬럼 생성 (월별 그룹화를 위해)
data['년'] = data['일시'].dt.year
data['월'] = data['일시'].dt.month

# 각 월별로 그룹화하여 휴일과 비휴일의 발전 수요량 비교
monthly_comparison = []

for year in data['년'].unique():  # 연도별로 처리
    for month in data[data['년'] == year]['월'].unique():  # 월별로 처리
        # 해당 년월의 데이터 추출
        monthly_data = data[(data['년'] == year) & (data['월'] == month)]

        # 휴일과 비휴일 데이터 분리
        holiday_data = monthly_data[monthly_data['휴일'] == 'O']  # 휴일인 데이터
        # 휴일이 아닌 데이터
        non_holiday_data = monthly_data[monthly_data['휴일'] == 'X']

        # 발전 수요량의 평균값 계산
        holiday_demand_avg = holiday_data['발전수요량'].mean(
        ) if not holiday_data.empty else 0
        non_holiday_demand_avg = non_holiday_data['발전수요량'].mean(
        ) if not non_holiday_data.empty else 0

        # 발전 수요량 차이 계산
        demand_diff = holiday_demand_avg - non_holiday_demand_avg

        # 결과 저장
        monthly_comparison.append({
            '년': year,
            '월': month,
            '일시': pd.to_datetime(f"{year}-{month:02d}-01"),  # 날짜 형식으로 저장
            '휴일 평균 발전 수요량': holiday_demand_avg,
            '비휴일 평균 발전 수요량': non_holiday_demand_avg,
            '발전 수요량 차이': demand_diff  # 발전 수요량 차이 컬럼 추가
        })

# 결과를 DataFrame으로 변환
comparison_df = pd.DataFrame(monthly_comparison)

# 출력
print(comparison_df)

# 그래프 시각화 (하나의 그래프에 두 선을 겹쳐서 표시)
plt.figure(figsize=(12, 6))

# 휴일 평균 발전 수요량 그래프
plt.plot(comparison_df['일시'], comparison_df['휴일 평균 발전 수요량'],
         marker='o', color='b', label='Holiday Avg Demand')

# 비휴일 평균 발전 수요량 그래프
plt.plot(comparison_df['일시'], comparison_df['비휴일 평균 발전 수요량'],
         marker='o', color='r', label='Non-Holiday Avg Demand')

# 제목과 라벨 설정 (영어로 변경)
plt.title(
    'Holiday vs Non-Holiday Average Power Demand (2023-01 to 2024-09)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Power Demand', fontsize=12)

# x축 날짜 포맷
plt.xticks(rotation=45)

# 그리드 추가
plt.grid(True)

# 범례 추가
plt.legend()

# 레이아웃 조정
plt.tight_layout()

# 그래프 출력
plt.show()
