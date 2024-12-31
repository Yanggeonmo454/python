import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
file_path = './1224/휴일포함_수정_재정렬.csv'
data = pd.read_csv(file_path, encoding='euc-kr')

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'])

# 필요한 컬럼 추출 및 이름 설정
data['Temperature'] = data['기온(°C)']  # 기온 컬럼 이름이 다를 경우 수정 필요
data['Power Demand'] = data['발전수요량']  # 발전수요량 컬럼 이름이 다를 경우 수정 필요
data['Solar Radiation'] = data['일사(MJ/m2)']  # 일사량 컬럼 이름

# 기간 설정 (예시: 2023년 1월 1일부터 2023년 1월 31일까지)
start_date = '2023-12-01'
end_date = '2023-12-30'
mask = (data['일시'] >= start_date) & (data['일시'] <= end_date)
filtered_data = data[mask]

# 사용자 설정 기온 및 일사 범위
min_temp = 3.5  # 사용자가 입력한 최소 기온
max_temp = 4.5  # 사용자가 입력한 최대 기온
min_solar = 0  # 사용자가 입력한 최소 일사
max_solar = 0.5  # 사용자가 입력한 최대 일사

# 기온과 일사량 모두 기준을 만족하는 데이터 필터링
filtered_data = filtered_data[
    (filtered_data['Temperature'] >= min_temp) &
    (filtered_data['Temperature'] <= max_temp) &
    (filtered_data['Solar Radiation'] >= min_solar) &
    (filtered_data['Solar Radiation'] <= max_solar)
]

# 휴일/비휴일별 데이터 분리
holiday_data = filtered_data[filtered_data['휴일'] == 'O'].copy()  # .copy() 추가
# .copy() 추가
non_holiday_data = filtered_data[filtered_data['휴일'] != 'O'].copy()

# 휴일/비휴일별 평균 발전수요량 계산
holiday_avg_demand = holiday_data['Power Demand'].mean()
non_holiday_avg_demand = non_holiday_data['Power Demand'].mean()

# 예측값을 데이터에 추가 (여기서 .loc을 사용하여 수정)
holiday_data.loc[:, 'Predicted'] = holiday_avg_demand
non_holiday_data.loc[:, 'Predicted'] = non_holiday_avg_demand

# 실제값과 예측값의 차이, MAPE 계산
holiday_data.loc[:, 'Actual - Predicted'] = holiday_data['Power Demand'] - \
    holiday_data['Predicted']
non_holiday_data.loc[:, 'Actual - Predicted'] = non_holiday_data['Power Demand'] - \
    non_holiday_data['Predicted']

holiday_data.loc[:, 'MAPE'] = (
    abs(holiday_data['Actual - Predicted']) / holiday_data['Power Demand']) * 100
non_holiday_data.loc[:, 'MAPE'] = (abs(
    non_holiday_data['Actual - Predicted']) / non_holiday_data['Power Demand']) * 100

# 데이터프레임 합치기 (휴일 데이터와 비휴일 데이터를 합침)
final_data = pd.concat([holiday_data[['일시', 'Power Demand', 'Predicted', 'Actual - Predicted', 'MAPE']],
                        non_holiday_data[['일시', 'Power Demand', 'Predicted', 'Actual - Predicted', 'MAPE']]])

# MAPE 컬럼이 높은 값 순으로 정렬된 새로운 데이터프레임 생성
final_data_sorted = final_data.sort_values(by='MAPE', ascending=False)

# 정렬된 데이터를 CSV 파일로 저장
final_data_sorted.to_csv('./final_data_sorted.csv',
                         index=False, encoding='euc-kr')

print("CSV 파일이 MAPE 순으로 정렬되어 저장되었습니다.")

print(final_data)

# 평균 MAPE 계산
holiday_avg_mape = holiday_data['MAPE'].mean()
non_holiday_avg_mape = non_holiday_data['MAPE'].mean()
overall_avg_mape = final_data['MAPE'].mean()

# 결과 출력
print(f"휴일 평균 MAPE: {holiday_avg_mape:.2f}%")
print(f"비휴일 평균 MAPE: {non_holiday_avg_mape:.2f}%")
print(f"전체 평균 MAPE: {overall_avg_mape:.2f}%")

# 시각화
plt.figure(figsize=(10, 6))

# Plot holiday data
plt.plot(holiday_data['일시'], holiday_data['Power Demand'],
         'o', label='Holiday Actual')

# Plot non-holiday data
plt.plot(non_holiday_data['일시'], non_holiday_data['Power Demand'],
         'x', label='Non-Holiday Actual')

# Add average prediction lines
plt.axhline(y=holiday_avg_demand, color='blue', linestyle='--',
            label=f'Holiday Predicted Average: {holiday_avg_demand:.2f}')
plt.axhline(y=non_holiday_avg_demand, color='red', linestyle='--',
            label=f'Non-Holiday Predicted Average: {non_holiday_avg_demand:.2f}')

# Add title and labels
plt.title('Power Demand by Temperature and Solar Radiation (Holiday vs Non-Holiday)')
plt.xlabel('Date')
plt.ylabel('Power Demand (kWh)')

# Add legend and grid
plt.legend()
plt.grid()
plt.tight_layout()

# Show plot
plt.show()
