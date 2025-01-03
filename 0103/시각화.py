import matplotlib.pyplot as plt

# 예시로 정해진 값들
a = 100
b = None  # b가 없을 경우를 가정
c = 150
d = None  # d가 없을 경우를 가정
e = 200

# x축 항목과 y축 데이터 준비
x_labels = ['a', 'b' if b is not None else 'c', 'd' if d is not None else 'e']
y_values = [a, b if b is not None else c, d if d is not None else e]

# 그래프 그리기
fig, ax = plt.subplots()

# 바 플롯 그리기
ax.bar(x_labels, y_values, color=['blue', 'green', 'red'])

# 그래프 제목과 라벨 설정
ax.set_title('Bar Plot for a, b, c, d (or e if b or d is absent)')
ax.set_xlabel('Labels')
ax.set_ylabel('Values')

# 그래프 표시
plt.show()
