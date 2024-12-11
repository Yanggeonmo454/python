import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data

mtcars = data('mtcars')

# 1. 실린더 수에 따른 평균 연비
cyl_mpg = mtcars.groupby('cyl')['mpg'].mean().reset_index()

# print(cyl_mpg)

sns.barplot(data=cyl_mpg, x='cyl', y='mpg')
plt.show()


# 2. 변속기 유형별 평균 마력
am_hp = mtcars.groupby('am')['hp'].mean().reset_index()

sns.barplot(data=am_hp, x='am', y='hp')
plt.show()

# 3. 히트맵, 실린더수 기준
pivot = mtcars.pivot_table(values='mpg', index='cyl',
                           columns='gear', aggfunc='mean')

sns.heatmap(pivot, annot=True, fmt=".2f", cmap="coolwarm",)
plt.show()

# 4. 연비, 마력, 무게 간의 상간관계 히트맵

df = mtcars[['mpg', 'hp', 'wt']]
matrix = df.corr()

sns.heatmap(matrix, annot=True, fmt=".2f", cmap="coolwarm",)
plt.show()
