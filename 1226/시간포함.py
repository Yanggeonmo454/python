import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
file_path = './1224/휴일포함_수정_재정렬.csv'
data = pd.read_csv(file_path, encoding='euc-kr')

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'])

# 필요한 컬럼 추출
data['Temperature'] = data['기온(°C)']  # 기온 컬럼 이름이 다를 경우 수정 필요
data['Power Demand'] = data['발전수요량']  # 발전수요량 컬럼 이름이 다를 경우 수정 필요

# 기간 설정 (예시: 2023년 1월 1일부터 2023년 12월 31일까지)
start_date = '2023-01-01'
end_date = '2023-01-31'
mask = (data['일시'] >= start_date) & (data['일시'] <= end_date)
filtered_data = data[mask]

# 사용자 설정 기온 범위
min_temp = 10  # 사용자가 입력한 최소 기온
max_temp = 11  # 사용자가 입력한 최대 기온

# 설정한 기온 범위에 해당하는 데이터 필터링
filtered_temp_data = filtered_data[(filtered_data['Temperature'] >= min_temp) & (
    filtered_data['Temperature'] <= max_temp)]

# '휴일' 컬럼이 'O'인 데이터 필터링 추가
filtered_temp_data_holiday = filtered_temp_data[filtered_temp_data['휴일'] == 'O']
filtered_temp_data_non_holiday = filtered_temp_data[filtered_temp_data['휴일'] != 'O']

# 시작 시간과 종료 시간을 설정하여 시간 범위 필터링
start_hour = 0  # 예시: 9시부터
end_hour = 1   # 예시: 17시까지

# 시간 범위 필터링: '일시'의 시간 정보가 start_hour와 end_hour 사이에 해당하는 데이터만 추출
filtered_temp_data_holiday_hours = filtered_temp_data_holiday[(filtered_temp_data_holiday['일시'].dt.hour >= start_hour) &
                                                              (filtered_temp_data_holiday['일시'].dt.hour < end_hour)]
filtered_temp_data_non_holiday_hours = filtered_temp_data_non_holiday[(filtered_temp_data_non_holiday['일시'].dt.hour >= start_hour) &
                                                                      (filtered_temp_data_non_holiday['일시'].dt.hour < end_hour)]

# 각 그룹의 평균 발전수요량 계산
avg_demand_holiday = filtered_temp_data_holiday_hours['Power Demand'].mean()
avg_demand_non_holiday = filtered_temp_data_non_holiday_hours['Power Demand'].mean(
)

# 기온과 발전수요량 시각화 (휴일은 점, 비휴일은 X로 표시)
plt.figure(figsize=(10, 6))

# 휴일 데이터는 점으로 표시
plt.plot(filtered_temp_data_holiday_hours['일시'], filtered_temp_data_holiday_hours['Power Demand'],
         marker='o', linestyle=' ', color='b', label=f'Holiday ({start_hour}:00 to {end_hour}:00)')

# 비휴일 데이터는 X로 표시
plt.plot(filtered_temp_data_non_holiday_hours['일시'], filtered_temp_data_non_holiday_hours['Power Demand'],
         marker='x', linestyle=' ', color='r', label=f'Non-Holiday ({start_hour}:00 to {end_hour}:00)')

# 휴일과 비휴일의 평균선 추가
plt.axhline(y=avg_demand_holiday, color='b', linestyle='--',
            label=f'Holiday Average: {avg_demand_holiday:.2f}')
plt.axhline(y=avg_demand_non_holiday, color='r', linestyle='--',
            label=f'Non-Holiday Average: {avg_demand_non_holiday:.2f}')

# 그래프 타이틀 및 레이블 설정
plt.title('Power Demand by Temperature Range (Holiday vs Non-Holiday)')
plt.xlabel('Date')
plt.ylabel('Power Demand (kWh)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.legend()

plt.show()
