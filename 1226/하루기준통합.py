import pandas as pd

# CSV 파일 로딩
file_path = './1224/휴일포함_수정_재정렬.csv'
data = pd.read_csv(file_path, encoding='euc-kr')

# '일시' 컬럼을 datetime으로 변환
data['일시'] = pd.to_datetime(data['일시'])

# '일시'를 기준으로 날짜만 추출 (시간 제외)
data['날짜'] = data['일시'].dt.date

# 하루 발전수요량(24시간 평균)과 하루 기온(24시간 평균) 계산
daily_data = data.groupby('날짜').agg({
    '발전수요량': 'mean',  # 하루 발전수요량 평균
    '기온(°C)': 'mean'        # 하루 기온 평균
}).reset_index()

# 새로운 CSV 파일로 저장
daily_data.to_csv('./1226/하루단위_발전수요량_기온.csv', index=False)

print("파일이 성공적으로 저장되었습니다.")
