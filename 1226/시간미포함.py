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

# 기간 설정 (예시: 2023년 7월 1일부터 2023년 7월 31일까지)
start_date = '2023-01-01'
end_date = '2023-01-31'
mask = (data['일시'] >= start_date) & (data['일시'] <= end_date)
filtered_data = data[mask]

# 사용자 설정 기온 범위
min_temp = 27  # 사용자가 입력한 최소 기온
max_temp = 28  # 사용자가 입력한 최대 기온

# 설정한 기온 범위에 해당하는 데이터 필터링
filtered_temp_data = filtered_data[(filtered_data['Temperature'] >= min_temp) & (
    filtered_data['Temperature'] <= max_temp)]

# '휴일' 컬럼이 'O'인 데이터 필터링 추가
filtered_temp_data_holiday = filtered_temp_data[filtered_temp_data['휴일'] == 'O']
filtered_temp_data_non_holiday = filtered_temp_data[filtered_temp_data['휴일'] != 'O']

# 각 그룹의 평균 발전수요량 계산
avg_demand_holiday = filtered_temp_data_holiday['Power Demand'].mean()
avg_demand_non_holiday = filtered_temp_data_non_holiday['Power Demand'].mean()

# 예측값 설정 (휴일: 휴일 평균, 비휴일: 비휴일 평균)
filtered_temp_data_holiday['Predicted'] = avg_demand_holiday
filtered_temp_data_non_holiday['Predicted'] = avg_demand_non_holiday

# MAPE 계산 함수


def calculate_mape(actual, predicted):
    return abs((actual - predicted) / actual) * 100


# 휴일과 비휴일 각각의 MAPE 계산
filtered_temp_data_holiday['MAPE'] = calculate_mape(
    filtered_temp_data_holiday['Power Demand'], filtered_temp_data_holiday['Predicted'])
filtered_temp_data_non_holiday['MAPE'] = calculate_mape(
    filtered_temp_data_non_holiday['Power Demand'], filtered_temp_data_non_holiday['Predicted'])

# 휴일과 비휴일 데이터를 합침
final_data = pd.concat([filtered_temp_data_holiday[['일시', 'Power Demand', 'Predicted', 'MAPE']],
                        filtered_temp_data_non_holiday[['일시', 'Power Demand', 'Predicted', 'MAPE']]])

# MAPE 기준으로 정렬
final_data_sorted = final_data.sort_values(by='MAPE', ascending=False)

# 결과를 CSV로 저장 (파일명에 start_date 사용)
start_date_str = start_date.replace('-', '_')  # 파일명에 사용하기 위해 날짜 형식을 수정
final_data_sorted.to_csv(
    f'./final_data_{start_date_str}.csv', index=False, encoding='euc-kr')

# 전체 MAPE 출력
holiday_mape = filtered_temp_data_holiday['MAPE'].mean()
non_holiday_mape = filtered_temp_data_non_holiday['MAPE'].mean()
overall_mape = pd.concat(
    [filtered_temp_data_holiday['MAPE'], filtered_temp_data_non_holiday['MAPE']]).mean()

print(f"Holiday MAPE: {holiday_mape:.2f}%")
print(f"Non-Holiday MAPE: {non_holiday_mape:.2f}%")
print(f"Overall MAPE: {overall_mape:.2f}%")

# MAPE 출력 (개별 MAPE 값)
print("\nIndividual MAPE values for holiday data:")
print(filtered_temp_data_holiday[['일시', 'Power Demand', 'Predicted', 'MAPE']])

print("\nIndividual MAPE values for non-holiday data:")
print(filtered_temp_data_non_holiday[[
      '일시', 'Power Demand', 'Predicted', 'MAPE']])

# 기온과 발전수요량 시각화 (휴일은 점, 비휴일은 X로 표시)
plt.figure(figsize=(10, 6))

# 휴일 데이터는 점으로 표시
plt.plot(filtered_temp_data_holiday['일시'], filtered_temp_data_holiday['Power Demand'],
         marker='o', linestyle=' ', color='b', label=f'Holiday')

# 비휴일 데이터는 X로 표시
plt.plot(filtered_temp_data_non_holiday['일시'], filtered_temp_data_non_holiday['Power Demand'],
         marker='x', linestyle=' ', color='r', label=f'Non-Holiday')

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
