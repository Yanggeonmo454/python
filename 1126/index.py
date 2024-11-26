"""
# 전역변수

quantity = 10


def get_price(price):
    price = price * quantity
    return price


print(f"{quantity} 개의 가격은 {get_price(2000)}원 입니다. ")

# 지역변수


def oneUp():
    x = 0
    x += 1
    return x


print(oneUp())


# 유효범위
quantity = 10


def price_sum(price):
    quantity = 7
    return price * quantity


print(price_sum(2000))

x = 0


def one_up():
    global x
    x += 1
    return x


print(one_up())
print(one_up())
print(one_up())


def pr_str(txt="안녕하세요", count=1):
    for _ in range(count):
        print(txt)


pr_str("Hello", 5)

def intro(name, age, city):
    print(f"이름은 {name}이고 나이는 {age}이고 사는곳은 {city}입니다. ")


intro("홍길동", 23, "seoul")
intro(city="서울", name="임꺽정", age=25)
intro("양건모", city="양양", age=25)

# 가변 매개변수


def calc_avg(*args):
    print(args)
    total = 0
    for i in args:
        total += i
    avg = total / len(args)
    return avg


print(calc_avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def text_def(*args):
    print("args :", args)


text_def(1, 2, 3, 4, 5)



def intro(**kwargs):
    for key, values in kwargs.items():
        print(f"{key} : {values}")


intro(name="홍길동", age=20, city="서울", gender="남자")

def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

print(pow(2, 3))


def my_pow(x, y):
    num = 1
    for _ in range(y):
        num *= x
    return num


print(my_pow(3, 4))

def square(x):
    return x ** 3


numbers = [2, 4, 6, 8]

squared = list(map(square, numbers))

print(squared)


def even_number(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(even_number, numbers)))

def func(x):
    num = range(1, 31)

    numbers = [i for i in num if i % x == 0]

    print(numbers)
    print(f"{x}의 배수의 개수: {len(numbers)}")

# 실습 4 여러개


def count(num):
    lists = [i for i in range(1, 31) if i % num == 0]
    counts = len(lists)
    return lists, counts


num = 3
lists, counts = count(3)
print(f"{num}의 배수 {lists}")
print(f"{num}의 개수: {counts}")

# filter


def count(num):
    # 중첩함수, 함수 내에서만 사용 가능
    def check(x):
        return x % num == 0

    lists = list(filter(check, range(1, 31)))
    return lists, len(lists)


num = 4
lists, counts = count(3)
print(f"{num}의 배수 {lists}")
print(f"{num}의 개수: {counts}")

def sos(i):
    print("help me!!")
    if i == 1:
        return ""
    else:
        return sos(i-1)


sos(10)

def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))


def fibonacci(x):
    if x <= 1:
        return x
    elif x >= 2:
        return fibonacci(x-1) + fibonacci(x-2)


print(fibonacci(3))


def add(x, y):
    return x + y


print(add(3, 4))


def add(x, y): return x+y


print(add(4, 5))

def oneup(x): return x+1

print(oneup(3))

def square(x): return x ** 2


print(square(4))
print((lambda x: x**2)(5))


def minus(x, y): return x - y


print(minus(10, 2))
print((lambda x, y: x-y)(7, 4))



def call(func):
    for _ in range(10):
        func()


def hello():
    print("안녕하세요")


def hello2(): return print("반갑습니다.")


call(hello2)


numbers = [2, 4, 6, 8]
squared = map(lambda x: x**3, numbers)

print(list(squared))

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, numbers2)))

def count(num):

    lists = list(filter(lambda x: x % num == 0, range(1, 31)))
    return lists, len(lists)


num = 3
lists, counts = count(3)
print(f"{num}의 배수 {lists}")
print(f"{num}의 개수: {counts}")
"""

weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0],
]


while True:
    print("[날씨 데이터 분석 프로그램]\n1.평균 기온 계산\n2.최고/최저 기온 찾기\n3.강수량 분석\n4.날씨 데이터 추가\n5.전체 데이터 출력\n6.종료(양건모)")
    user_input = int(input("원하는 기능의 번호를 입력하세요."))

    if user_input == 1:
        city = input("도시 이름을 입력하세요. (서울/부산): ")
        city_data = [data[2] for data in weather_data if data[1] == city]

        if city_data:
            average_temp = sum(city_data) / len(city_data)
            print(f"{city}의 평균 기온: {average_temp:.2f}'C")
        else:
            print(f"{city}에 대한 날씨 데이터가 없습니다.")

    elif user_input == 2:
        city = input("도시 이름을 입력하세요. (서울/부산) ")
        city_data = [data[2] for data in weather_data if data[1] == city]

        if city_data:
            max_temp = max(city_data)
            min_temp = min(city_data)
            print(f"{city}의 최고 기온: {max_temp}'C, 최저 기온: {min_temp}'C")
        else:
            print(f"{city}에 대한 날씨 데이터가 없습니다.")
    elif user_input == 3:
        city = input("도시 이름을 입력하세요. (서울/부산) ")
        city_data = [data[3] for data in weather_data if data[1] == city]

        if city_data:
            print(f"{city}의 총 강수량: {sum(city_data)}mm")
            print(f"{city}의 강수량이 있었던 날: {len(city_data)}일")
        else:
            print(f"{city}에 대한 날씨 데이터가 없습니다.")

    elif user_input == 4:
        day = input("날짜를 입력하세요 (YYYY-MM-DD):")
        city = input("도시 이름을 입력하세요. (서울/부산) ")
        temp = float(input("평균 기온을 입력하세요. ('C): "))
        rain = float(input("강수량을 입력하세요. (mm): "))
        weather_data.append([day, city, temp, rain])
        print(f"{city}의 날씨 데이터가 추가되었습니다.")
    elif user_input == 5:
        print("현재 날씨 데이터: ")
        for data in weather_data:
            print(f"날짜: {data[0]}, 도시: {data[1]}, 평균 기온: {
                  data[2]}°C, 강수량: {[3]}mm")
    elif user_input == 6:
        break
    else:
        print("원하는 기능의 번호를 정확히 입력하세요.")
