import matplotlib.pyplot as plt
from matplotlib import font_manager

font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
print(font_list)

path = "C:\\Windows\\Fonts\\LG_Smart_UI-Light.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc('font', family=font)

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y, color="red", linestyle="--", linewidth=3, label="샘플 그래프")
# plt.title("그래프", pad=30, fontsize=20, color="#ff0000", backgroundcolor="green")
# plt.legend()
# plt.show()

"""
# 데이터
labels = ['Apple', 'Banana', 'Melon', 'Grape']
sizes = [34, 32, 16, 18]
colors = ['red', 'yellow', 'green', 'purple']
explode = [0.1, 0.1, 0.1, 0.1]  # 항목 간 간격

# 도넛형 그래프
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.6}  # 도넛형으로 설정 (두께 조정)
)

plt.title('Donut Chart Example')
plt.show()
"""
# 그래프 선이 여러개
# x = [1, 2, 3, 4]
# y1 = [1, 2, 3, 4]
# y2 = [2, 4, 6, 8]
# y3 = [3, 6, 9, 12]
# y4 = [4, 8, 12, 16]

# # 각 선 그래프 플롯
# plt.plot(x, y1, label="y = x", color="red")
# plt.plot(x, y2, label="y = 2x", color="orange")
# plt.plot(x, y3, label="y = 3x", color="green")
# plt.plot(x, y4, label="y = 4x", color="blue")

# # 그래프에 범례 추가
# plt.legend(loc="upper center", title="4개 연습", ncol=4)

# # 그래프에 제목 및 축 이름 설정
# plt.title("Linear Functions")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")

# # 그래프 보여주기
# plt.show()

# 그래프가 여러개

# x = [1, 2, 3, 4]
# y1 = [1, 2, 3, 4]
# y2 = [2, 4, 6, 8]
# y3 = [3, 6, 9, 12]
# y4 = [4, 8, 12, 16]

# # 첫 번째 서브플롯
# plt.subplot(2, 2, 1)
# plt.plot(x, y1)
# plt.title("y = x")

# # 두 번째 서브플롯
# plt.subplot(2, 2, 2)
# plt.plot(x, y2)
# plt.title("y = 2x")

# # 세 번째 서브플롯
# plt.subplot(2, 2, 3)
# plt.plot(x, y3)
# plt.title("y = 3x")

# # 네 번째 서브플롯
# plt.subplot(2, 2, 4)
# plt.plot(x, y4)
# plt.title("y = 4x")

# # 전체 레이아웃 조정
# plt.tight_layout()

# # 그래프 보여주기
# plt.show()

# colors = ['red', 'yellow', 'green', 'blue']  # 막대의 색상 설정

# 막대그래프 생성
# plt.bar(categories, values, color=colors, edgecolor='black',
#         linewidth=0.5, width=0.5)  # width는 막대 굵기
# # color: 각 막대의 색상 설정
# # edgecolor: 막대 테두리 색상 설정
# # linewidth: 막대 테두리 두께 조절

# # 그래프 제목 및 축 레이블 추가
# plt.title('Category vs Value')
# plt.xlabel('Category')
# plt.ylabel('Value')

# # 그래프 표시
# plt.show()


categories = ['Apple', 'Banana', 'Melon', 'Grape']
values = [34, 32, 16, 18]
plt.barh(categories, values, color="blue")
plt.show()

#저장
#plt.savefig("./1209/graph.jpg", format = "jpg")