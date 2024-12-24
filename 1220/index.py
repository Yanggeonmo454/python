# # 상관관계 분석 코드, 기간, 컬럼 변경하면서 분석하면 되겠습니다.

# import pandas as pd
# import numpy as np

# # CSV 파일 읽기
# file_path = "./1220/기상자료 및 발전수요량 데이터 _ 2023년.csv"
# data = pd.read_csv(file_path, encoding='EUC-KR')

# # '일시' 컬럼을 datetime 형식으로 변환
# data['일시'] = pd.to_datetime(data['일시'], errors='coerce')

# # 2021-06부터 2021-08까지의 데이터만 필터링 (날짜와 시간 모두 포함)
# filtered_data = data[(data['일시'] >= '2023-06-01') &
#                      (data['일시'] < '2023-09-01')].copy()

# # 데이터 확인
# print("필터링된 데이터:")
# print(filtered_data[['일시', '발전수요량', '기온(°C)']].head())

# # 결측값을 각 열의 평균값으로 대체
# filtered_data["발전수요량"] = filtered_data["발전수요량"].fillna(
#     filtered_data["발전수요량"].mean())
# filtered_data["기온(°C)"] = filtered_data["기온(°C)"].fillna(
#     filtered_data["기온(°C)"].mean())

# # 결측값 처리 후 데이터 확인
# print("\n결측값 처리 후 데이터:")
# print(filtered_data[['일시', '발전수요량', '기온(°C)']].head())

# # 피어슨 상관계수 계산
# correlation_pearson = filtered_data["발전수요량"].corr(filtered_data["기온(°C)"])

# # 결과 출력
# print(
#     f"\n2023-06부터 2023-08까지 발전수요량과 기온(°C)의 피어슨 상관계수: {correlation_pearson:.2f}")
import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

# CSV 파일 읽기
file_path = "./1220/기상자료 및 발전수요량 데이터 _ 2023년.csv"
data = pd.read_csv(file_path, encoding='EUC-KR')

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'], errors='coerce')

# 날짜를 YYYYMMDD 형식으로 변환한 새로운 컬럼 추가
data['날짜'] = data['일시'].dt.strftime('%Y%m%d')
data['시간'] = data['일시'].dt.hour  # 시간 정보를 따로 추출

# 발전수요량 예측 함수


def predict_demand_for_date(target_date_str):
    # 입력 받은 날짜를 datetime 형식으로 변환
    target_date = pd.to_datetime(target_date_str, format='%Y%m%d')

    # 예측할 날짜의 전날, 전전날, 전전전날 찾기
    date_range = [target_date - pd.Timedelta(days=i) for i in range(1, 4)]
    date_range_str = [d.strftime('%Y%m%d') for d in date_range]

    # 예측값과 실제값 저장 리스트
    predicted_values = []
    actual_values = []

    # 시간별 예측값 계산
    for hour in range(24):  # 0시부터 23시까지
        # 전날, 전전날, 전전전날의 같은 시간대 발전수요량 가져오기
        hourly_values = []
        for date in date_range_str:
            hourly_data = data[(data['날짜'] == date) & (data['시간'] == hour)]
            if not hourly_data.empty:
                hourly_values.append(hourly_data['발전수요량'].values[0])

        # 3일치 값이 모두 있을 경우 평균 계산
        if len(hourly_values) == 3:
            predicted_values.append(np.mean(hourly_values))
        else:
            return None, None  # 3일치 데이터 부족 시 None 반환

        # 실제값 가져오기
        actual_data = data[(data['날짜'] == target_date_str)
                           & (data['시간'] == hour)]
        if not actual_data.empty:
            actual_values.append(actual_data['발전수요량'].values[0])
        else:
            return None, None  # 실제 데이터 부족 시 None 반환

    # MAPE 계산
    actual_values = np.array(actual_values)
    predicted_values = np.array(predicted_values)
    hourly_mape = np.mean(
        np.abs((actual_values - predicted_values) / actual_values)) * 100

    # 하루 평균 MAPE 계산
    total_actual = np.sum(actual_values)
    total_predicted = np.sum(predicted_values)
    daily_mape = np.abs((total_actual - total_predicted) / total_actual) * 100

    return predicted_values, actual_values, hourly_mape, daily_mape


# 2023년 전체 데이터를 처리
unique_dates = sorted(data['날짜'].unique())
results = []

for date in unique_dates:
    result = predict_demand_for_date(date)
    if result[0] is not None:  # 결과가 유효한 경우만 저장
        predicted, actual, hourly_mape, daily_mape = result
        results.append({
            "날짜": date,
            "시간별 예측값": predicted.tolist(),
            "시간별 실제값": actual.tolist(),
            "시간별 MAPE 평균 (%)": hourly_mape,
            "하루 평균 MAPE (%)": daily_mape
        })

# 결과를 DataFrame으로 변환
results_df = pd.DataFrame(results)

# 결과를 CSV로 저장
results_df.to_csv("predicted_results_2023.csv",
                  index=False, encoding="utf-8-sig")

print("2023년 전체 예측 결과가 'predicted_results_2023.csv' 파일로 저장되었습니다.")
