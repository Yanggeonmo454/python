import pandas as pd

# 새 파일 경로 설정
file_path = r"C:\Users\didrj\documents\workspace\python\1224\제주도 시간별 기상자료 및 발전수요량(20230101_20240930) (1).csv"

# 데이터 불러오기
data = pd.read_csv(file_path, encoding='EUC-KR')

# '일시' 컬럼을 datetime 형식으로 변환 (형식 지정)
data['일시'] = pd.to_datetime(data['일시'].astype(str))

# 공휴일 데이터 추가 (예시로 설정)
public_holidays = pd.to_datetime([
    '2023-01-01', '2023-01-21', '2023-01-22', '2023-01-23', '2023-03-01', '2023-05-05', '2023-06-06', '2023-08-15',
    '2023-09-28', '2023-09-29', '2023-09-30', '2023-10-03', '2023-12-25', '2024-01-01', '2024-02-09', '2024-02-10',
    '2024-02-11', '2024-02-12', '2024-03-01', '2024-04-10', '2024-05-01', '2024-05-05', '2024-05-06', '2024-05-15',
    '2024-06-06', '2024-08-15', '2024-09-16', '2024-09-17', '2024-09-18'
])

# 공휴일을 datetime.date 형식으로 변환
public_holidays = public_holidays.date

# 먼저 공휴일 처리: 공휴일은 'O'로 설정
data['휴일'] = data['일시'].dt.date.apply(
    lambda x: 'O' if x in public_holidays else 'X')

# 주말 처리: 주말(토요일, 일요일)을 'O'로 설정 (공휴일이 이미 'O'로 설정된 경우는 그대로 두고, 아닌 경우만 'O'로 설정)
for index, row in data.iterrows():
    if row['휴일'] == 'X':  # 공휴일이 아닌 경우만
        if row['일시'].weekday() in [5, 6]:  # 토요일(5), 일요일(6)
            data.at[index, '휴일'] = 'O'

# 결과 확인
print(data[['일시', '휴일']].head())

# 수정된 DataFrame을 다시 CSV 파일로 저장
output_file_path = 'C:/Users/didrj/documents/workspace/python/1224/휴일포함_수정.csv'
data.to_csv(output_file_path, index=False, encoding='EUC-KR')


# 컬럼 순서를 변경: '일시', '휴일', '발전수요량' 순으로 정렬
columns_order = ['일시', '휴일'] + \
    [col for col in data.columns if col not in ['일시', '휴일']]

# 데이터프레임의 컬럼 순서를 재정렬
data = data[columns_order]

# 결과 확인
print(data[['일시', '휴일', '발전수요량']].head())

# 수정된 DataFrame을 다시 CSV 파일로 저장
output_file_path = 'C:/Users/didrj/documents/workspace/python/1224/휴일포함_수정_재정렬.csv'
data.to_csv(output_file_path, index=False, encoding='EUC-KR')
