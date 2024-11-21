"""
# 변수의 사이즈 알아보는 방법

from sys import getsizeof

print(getsizeof(1))
print(getsizeof("1"))

#변수의 자료형 알아보는 방법


print(type("11111"))
print(type(True))
print(type(None))


num = int(input("숫자를 입력하세요."))
a = (num % 2)

print("True면 짝수, False면 홀수:", a == 0)


print(int(5.5))
a = "10"
print(type(int(a)))
print(type(a))

num = 10
print(type(str(num)))

# 문자열 연산
a = input("이름을 입력하세요.")
print("안녕하세요 " + a + "님, 반갑습니다.")



동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세



print("'오늘저녁뭐먹지'")

# 이스케이프
print("Hello\"World")
"""
"""
# 문자열 포매팅
print("올해는 2024년 용띠의 해이다.")

year = "올해는 %d년 %s의 해이다." % (2024, "용띠")
year = "올해는 %d년 %s의 해이다." % (2025, "뱀띠")

print(year)



# 포맷코드 활용
number = "저는 올해 %d살 입니다." % 20
print(number)
calc = "20 나누기 3은 %.3f" % 6.666
print(calc)
text = "저는 %-10s에서 살고 있습니다." % "서울"
print(text)
char = "이모티콘은 %c 로 할게요." % "😊"
print(char)
"""
"""
# 포매팅 예문

country = "대한민국"
city = "서울"
people = "한국인"
text = "저는 올해 {0}살 입니다." .format(20)

print(text)
text = "저는 {0} 사람이며 {1}에 살고 있습니다." .format(country, city)

print(text)

text = "제가 사는 {0}은 {a}에 있습니다." .format(city, a="한국")
print(text)

text = "중괄호 출력하고 싶을때 {{ 중괄호 }}".format()
print(text)

a = "[{0:#^10}]" .format("hey")
print(a)
"""
"""
name = "양건모"
age = 20
print(f"내이름은 [{name:^10}]입니다. 나이는 {age+1} 입니다.")

"""

# print('|\_/|\n|q p|   /}\n( 0 )"""\ \n|"^"`   |\n||_/=\\__|')

"""
name = "양건모"
print(f"[{name:=^20}]")

print(f"문자열 실습입니다. {{중괄호}}를 출력해보세요")
"""

# print(a[7]+a[8]+a[9]+a[10]+a[11]+a[12])
"""
date = "20240930"
year = date[:4]
month = date[4:6]
day = date[6:]

print(year+"년", month+"월", day+"일")

print(len(date))

print(a.count("l"))
"""
"""
a = "Hello, Python"
print(a.find("o"))

first_o = a.find('o')

second_o = a.find('o', first_o + 1)

print(second_o)

print(a.index("P"))

print(a.replace("Python", "파이썬"))

print(a.split("l"))
"""
"""
a = "Hello, World"

print(a.upper())
print(a.lower())

b = "          hey          "

print(f"[{b.rstrip()}]")
print(f"[{b.lstrip()}]")
print(f"[{b.strip()}]")
"""


# print("1234".isnumeric())

name = input("이름을 입력하세요.")
age = input("나이를 입력하세요.")

print(f"안녕하세요! {name}님 ({age}세)")

"""
name = input("이름을 입력하세요.")
year_b = int(input("태어난 년도를 입력하세요."))
year_t = int(input("올해 년도를 입력하세요."))

print(f"올해는{year_t}, {name}님의 나이는{year_t - year_b + 1}세 입니다.")
"""
