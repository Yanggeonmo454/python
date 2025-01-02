import pandas as pd
from datetime import datetime, timedelta

# 데이터 불러오기
file_path = './1224/휴일포함_수정_재정렬.csv'
data = pd.read_csv(file_path, encoding='euc-kr')

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'])

# 필요한 컬럼 추출
data['Temperature'] = data['기온(°C)']  # 기온 컬럼 이름이 다를 경우 수정 필요
data['Power Demand'] = data['발전수요량']  # 발전수요량 컬럼 이름이 다를 경우 수정 필요

# 기간 범위 설정 (2023-01-01 00:00부터 2023-12-31 23:00까지)
# 기간 범위 설정 (2023-01-01 00:00부터 2023-12-31 23:00까지)
date_range = pd.date_range(start='2023-01-01 00:00',
                           end='2023-12-31 23:00', freq='h')


# 빈 리스트 준비
results = []

# MAPE 계산 함수


def calculate_mape(actual, predicted):
    return abs((actual - predicted) / actual) * 100

# 기간 설정 함수


def duration(selected_datetime):
    if selected_datetime < datetime(2024, 9, 30):
        start_date = selected_datetime - timedelta(days=30)
        end_date = selected_datetime - timedelta(hours=1)
        start_time = selected_datetime.replace(
            minute=0, second=0, microsecond=0) - timedelta(days=0)
        end_time = selected_datetime.replace(
            minute=59, second=59, microsecond=999999) - timedelta(days=0)
    else:
        start_date = selected_datetime - timedelta(days=365)
        end_date = selected_datetime - timedelta(hours=1)
        start_time = selected_datetime.replace(
            minute=0, second=0, microsecond=0) - timedelta(days=365)
        end_time = selected_datetime.replace(
            minute=59, second=59, microsecond=999999) - timedelta(days=365)

    return start_date, end_date, start_time, end_time

# 예측값 계산 함수


def calculate_expecting_energy_for_all_dates(selected_datetime):
    # 기간 설정
    start_date, end_date, start_time, end_time = duration(selected_datetime)

    # 필터링 데이터
    date_data = data[(data['일시'] >= start_date) & (data['일시'] <= end_date)]
    filtered_data = date_data

    # 사용자 설정 기온 범위
    time_data_in_range = data[(data['일시'] >= start_time) & (
        data['일시'] <= end_time)].reset_index(drop=True)
    avg_temp = time_data_in_range['기온(°C)'].mean()
    min_temp = avg_temp - 30
    max_temp = avg_temp + 30

    # 설정한 기온 범위에 해당하는 데이터 필터링
    filtered_temp_data = filtered_data[(filtered_data['Temperature'] >= min_temp) &
                                       (filtered_data['Temperature'] <= max_temp)].reset_index(drop=True)

    # '휴일' 컬럼이 'O'인 데이터 필터링 추가
    filtered_temp_data_holiday = filtered_temp_data[filtered_temp_data['휴일'] == 'O']
    filtered_temp_data_non_holiday = filtered_temp_data[filtered_temp_data['휴일'] != 'O']

    # 각 그룹의 평균 발전수요량 계산
    avg_demand_holiday = filtered_temp_data_holiday['Power Demand'].mean()
    avg_demand_non_holiday = filtered_temp_data_non_holiday['Power Demand'].mean(
    )

    # 예측값 계산
    if (time_data_in_range['휴일'] == 'O').any():
        predicted_value = avg_demand_holiday
    else:
        predicted_value = avg_demand_non_holiday

    # 실제값과 MAPE 계산
    today_demand = time_data_in_range['발전수요량'][0]
    mape = calculate_mape(today_demand, predicted_value)

    return today_demand, predicted_value, mape


# 각 날짜 및 시간에 대해 실제값, 예측값, MAPE 계산
for current_datetime in date_range:
    actual, predicted, mape = calculate_expecting_energy_for_all_dates(
        current_datetime)
    results.append([current_datetime, actual, predicted, mape])

# 결과를 DataFrame으로 변환
df = pd.DataFrame(results, columns=['Datetime', 'Actual', 'Predicted', 'MAPE'])

# 결과 출력
print(df)

# 결과를 '1년검증.csv' 파일로 저장
df.to_csv('1년검증.csv', index=False, encoding='euc-kr')

print("파일이 성공적으로 저장되었습니다.")
