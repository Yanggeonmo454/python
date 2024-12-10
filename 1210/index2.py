import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# tips = sns.load_dataset('tips')
# print(tips.head())

# sns.scatterplot(x='total_bill', y='tip', hue='sex',
# style='time', size='size', data=tips)
# sns.stripplot(x="day", y="total_bill", data=tips,
#               jitter=True, hue="size", dodge=True)


# sns.swarmplot(x="day", y="total_bill", data=tips, hue="size", dodge=True)

# sns.relplot(x="total_bill", y="tip", data=tips, style="time", hue="sex")

# sns.catplot(x="day", y="total_bill", data=tips, hue="sex", kind="violin")


# data = np.random.rand(10, 10)
# sns.heatmap(data, annot=True, fmt=".2f", cmap="coolwarm")

# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# penguins = sns.load_dataset('penguins')

# sns.barplot(x='species', y='body_mass_g', data=penguins, hue='species')
# plt.show()


# sns.scatterplot(x='bill_length_mm', y='bill_depth_mm',
#                 hue='species', data=penguins)
# plt.show()

# sns.catplot(x='island', y='body_mass_g', data=penguins,
#             hue='island', kind='violin')
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# import seaborn as sns
# import matplotlib.pyplot as plt


# flights = sns.load_dataset('flights')

# avg = flights.groupby('year')['passengers'].mean()
# plt.plot(avg.index, avg.values)
# plt.xlabel('Year')
# plt.ylabel('Average Passengers')
# plt.title('Average Passengers by Year')
# plt.show()

# flights_pivot = flights.pivot(
#     index='month', columns='year', values='passengers')
# plt.figure(figsize=(10, 10))
# sns.heatmap(flights_pivot, annot=True, fmt=".2f", cmap="coolwarm")
# plt.show()

# flights_1958 = flights[flights['year'] == 1958]
# plt.figure(figsize=(10, 6))
# sns.barplot(x='month', y='passengers', data=flights_1958)
# plt.title('Passengers in 1958')
# plt.show()


# titanic = sns.load_dataset('titanic')
# print(titanic.head())

# sns.catplot(x='class', hue='survived', data=titanic,
#             kind='bar', height=4, aspect=.6)
# plt.show()

# # 2. 나이(age)의 분포를 생존 여부(survived)에 따라 kdeplot으로 시각화
# plt.figure(figsize=(10, 6))
# sns.kdeplot(data=titanic, x='age', hue='survived', multiple='stack')
# plt.title('Age Distribution by Survival Status')
# plt.xlabel('Age')
# plt.ylabel('Density')
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Titanic 데이터셋 로드
titanic = sns.load_dataset('titanic')

# # catplot 수정 (kind='box' 대신 적절한 대안 사용)
# sns.catplot(x='class', hue='survived', data=titanic,
#             kind='count')  # 예: barplot
# plt.title("Survival by Class")
# plt.show()

sns.kdeplot(data=titanic, x='age', hue='survived')
plt.show()
