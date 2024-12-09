
import pandas as pd
"""
data = {
    "Name": ["홍길동", "임꺽정", "성춘향"],
    "Age": [25, None, 20],
    "City": ["서울", "부산", None]
}

df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())


s = pd.Series(['사과', '바나나', '사과', '바나나', '오렌지'])
print(s.value_counts())

df = pd.DataFrame({
    "과일": ['사과', '바나나', '사과', '바나나', '오렌지'],
    "수량": [1, 2, 3, 4, 5]
})

print(df['과일'].value_counts())


s = pd.Series([1, 2, 3, 4, 5])
result = s.agg(['sum', 'mean', 'max'])

print(result)

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 11, 12]
})

print(df.agg(['sum', 'mean']))
print(df.agg({'A': 'sum', 'B': 'mean'}))
"""

s1 = pd.Series([10, 20, 30])
s2 = pd.Series([5, 15, 25])

# print(s1s2)


data = {
    'group': ['A', 'A', 'B', 'B', 'C'],
    'value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# 그룹화 후 'value' 컬럼에 대해 합계를 구함
# result = df.groupby('group')['value'].sum()

result = df.groupby('group')['value'].agg(['sum', 'mean', 'max'])
print(result)
