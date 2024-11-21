"""
# list basics

number = [1, 2, 3, "Hello", "Python"]
print(number[3])
print(number[0])

text = "Hello", "Python"
text = list(text)

print(text)

# list slicing
shop = ["반팔", "청바지", "이어폰", ["무선키보드", "기계식키보드"]]

print(shop[:2])

print(shop[3])

print(shop[-2])

shop[0] = "긴팔"

print(shop)


# shop[100] = "청바지"
# print(shop)

del shop[1]
print(shop)

a = [1, 2, 3]
b = ["안녕하세요", "반갑습니다."]

print(a+b)
print(a*2)

num_1 = [3, 1, 5, 2]
num_asc = sorted(num_1)
print(num_asc)

num_desc = sorted(num_1, reverse=True)
print(num_desc)

num_1.sort()
print(num_1)

korean = ["강", "이", "박", "최", "김"]

korean.sort(reverse=True)
print(korean)

alphabet = ["b", "C", "a", "d"]
alphabet.reverse()
print(alphabet)
print(alphabet.index('C'))

x = ['a', 'b', 'c', "안녕", "Hi", 'a']
print(x)
x.append("GOOD")

print(x)

x.pop(2)
print(x)

x.remove("Hi")

print(x)

x.clear()
print(x)

q = ['a', 'a', 'b']
print(q.count('a'))
"""
"""
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

print(rainbow[2])

print(sorted(rainbow))

rainbow.append("red")

print(rainbow)

rainbow_1 = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

del rainbow_1[2:6]

print(rainbow_1)
"""
"""
# 2차원 리스트

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[2][0])

# 요소 추가

matrix[1] = matrix[1] + [99]

print(matrix)

matrix = matrix + [[10, 11, 12]]

print(matrix)

# 요소 수정
matrix[0][0] = 100
matrix[1][1] = 5000

print(matrix)

del matrix[2]
print(matrix)

# 행, 열의 갯수
rows = len(matrix)

print(rows)

cols = len(matrix[0])
print(cols)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 요소 추가 메소드
matrix[0].append(10)
print(matrix)

matrix.append([10, 11, 12])
print(matrix)

matrix[1].insert(1, 100)
print(matrix)

matrix.insert(2, ["안녕하세요", "반갑습니다.", "어서오세요"])
print(matrix)

matrix[0].extend([11, 12])
print(matrix)


t1 = (1,)
t2 = (1, 2, 3, 4, 5, 3, 3, 3)
print(t1[0])

print(t2.count(3))

t3 = 1, 2, 3
print(t3.index(2))

t4 = ('a', 'b', 'c', ("안녕", "감사"))
print(t4[3][0])

print(len(t4))

print('c' in t4)
"""

# set

s1 = {1, 1, 1, 1, 1, 1, 2}

print(s1)

s2 = ["안녕", "잘가", "Hi", "안녕"]

print(set(s2))
