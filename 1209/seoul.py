import pandas as pd

file_name = "./1209/서울특별시_공원 내 운동기구 설치 현황_20201231.csv"
df = pd.read_csv(file_name, encoding="cp949")

# df.columns = df.columns.str.strip()

# result_1 = df.groupby('구분')['운동기구 수량'].sum()
# print(result_1)
# #result_1.to_csv('공원별 총 운동기구 설치 수.csv', encoding='utf-8')  # 저장

# result_2 = df.groupby('운동기구 기종명')['운동기구 수량'].sum()
# print(result_2)

# result_3 = df.groupby('관리기관')['운동기구 수량'].sum()
# print(result_3)

# df['구분'] = df['구분'].str.strip()
# namsan = df[df['구분'] == '남산공원(회현)']
# print(namsan)

# df['운동기구 기종명'] = df['운동기구 기종명'].str.strip()
# stepcycle = df[df['운동기구 기종명'] == '스텝사이클']
# print(stepcycle)

# df_sorted = df.sort_values(by='운동기구 수량', ascending=False)
# print(df_sorted)

# print(df.info())
# print(df.isnull().sum)

df.columns = df.columns.str.strip()
print(df.columns)
