import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
# print(font_list)

path = "C:\\Windows\\Fonts\\LG_Smart_UI-Light.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

# data = [1, 2, 2, 2, 3, 4, 3, 4, 5, 5, 5, 5, 5, 5, 6]

# plt.hist(data, bins=5)
# plt.title("title")
# plt.xlabel("값")
# plt.ylabel("빈도")
# plt.show()


# data1 = [1, 2, 2, 3, 3, 3, 4]
# data2 = [2, 3, 3, 4, 4, 5, 6]

# # 수정된 코드
# plt.hist([data1, data2], bins=5, color=["green", "purple"],
#          alpha=0.5, label=['data1', 'data2'])

# plt.title("여러개 히스토그램")
# plt.xlabel("값")
# plt.ylabel("빈도수")
# plt.legend()
# plt.show()


# n = 50
# x = np.random.rand(n)
# y = np.random.rand(n)

# print(x, y)


# sizes = [25, 25, 20, 20]
# labels = ['a', 'b', 'c', 'd']

# plt.pie(sizes, labels=labels)
# plt.show()

# sizes = [15, 30, 45, 10]
# labels = ["사과", "바나나", "포도", "체리"]
# explode = [0, 0.1, 0, 0]


# plt.pie(sizes, labels=labels, explode=explode,
#         autopct="%1.1f%%", shadow=True, startangle=140)
# plt.show()


# sizes = [10, 20, 30, 40]
# labels = ['a', 'b', 'c', 'd']
# colors = ["gold", "lightblue", "lightgreen", "pink"]

# plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", textprops={
#         "fontsize": 15, "color": "darkblue"}, wedgeprops={"edgecolor": "black"})
# plt.show()

# sizes = [40, 30, 20, 10]
# labels = ["x", "y", "z", "w"]

# plt.pie(sizes, labels=labels, wedgeprops={"width": 0.4})
# plt.show()


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2019 = [100, 120, 140, 110, 130, 150, 160, 170, 180, 200, 190, 210]
sales_2020 = [90, 110, 130, 120, 140, 160, 170, 160, 150, 180, 200, 190]

plt.plot(months, sales_2019, label='2019')
plt.plot(months, sales_2020, label='2020')

plt.title('Monthly Sales Comparison 2019-2020')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()

plt.show()


categories = ['Category 1', 'Category 2',
              'Category 3', 'Category 4', 'Category 5']
data = [20, 35, 15, 27, 45]

plt.figure(figsize=(10, 10))
plt.bar(categories, data)

plt.grid(True)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.xticks(rotation=45)

plt.show()

labels = ['Apple', 'Banana', 'Melon', 'Grape']
sizes = [34, 32, 16, 18]
colors = ['red', 'yellow', 'green', 'purple']
explode = [0.1, 0.1, 0.1, 0.1]

plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    wedgeprops={'width': 0.6, "edgecolor": "black"}
)

plt.show()
