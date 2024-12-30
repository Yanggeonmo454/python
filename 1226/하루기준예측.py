import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 로딩
file_path = './1226/하루단위_발전수요량_기온.csv'
data = pd.read_csv(file_path, encoding='utf-8')

# 날짜 컬럼을 datetime으로 변환
data['날짜'] = pd.to_datetime(data['날짜'])

# 컬럼명이 '기온(°C)' 형태일 경우 이를 '기온'으로 수정
data.columns = data.columns.str.replace('기온\(°C\)', '기온', regex=True)

# 날짜 범위와 기온 범위 설정 (변수로 설정)
start_date = '2023-01-01'  # 시작 날짜
end_date = '2023-01-31'    # 종료 날짜
min_temperature = 10        # 최소 기온
max_temperature = 20       # 최대 기온

# 날짜 범위로 필터링
data_filtered = data[(data['날짜'] >= start_date) & (data['날짜'] <= end_date)]

# 기온 범위로 필터링
data_filtered = data_filtered[(data_filtered['기온'] >= min_temperature) & (
    data_filtered['기온'] <= max_temperature)]

# 발전수요량의 평균 계산
average_demand = data_filtered['발전수요량'].mean()

# 필터링된 데이터로 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(data_filtered['날짜'], data_filtered['발전수요량'],
         marker='o', linestyle='', color='b')
plt.axhline(y=average_demand, color='r', linestyle='--',
            label=f'Average Power Demand: {average_demand:.2f}')
plt.title(f'Power Demand (Temperature range: {min_temperature} ~ {
          max_temperature}°C, Date range: {start_date} ~ {end_date})')
plt.xlabel('Date')
plt.ylabel('Power Demand')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# 그래프 출력
plt.show()
