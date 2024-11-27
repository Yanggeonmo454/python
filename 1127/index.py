"""
class Car:
    model = ""
    cc = 0

    # 함수 추가
    def info(self):
        print(f"모델명: {self.model} 배기량: {self.cc}cc")


car1 = Car()  # 인스턴스 생성
car1.model = "싼타페"
car1.cc = 2000

# print(f"모델명: {car1.model}")
# print(f"배기량: {car1.cc}cc")

car1.info()



class Car:
    def __init__(self, model, cc):
        self.model = model
        self.cc = cc

    def info(self):
        print(f"모델명: {self.model}, 배기량은 {self.cc}cc 다.")

    def __str__(self):
        return (f"모델명: {self.model}, 배기량은 {self.cc}cc 다.")


car1 = Car("싼타페", 2000)
car2 = Car("bmw", 2000)

car1.info()
car2.info()

print(car1)
print(car2)
print("====== 승용차 리스트 ======")

cars = [
    Car("쏘나타", 2000),
    Car("쏘렌토", 3000),
    Car("아반떼", 1600)
]

for car in cars:
    print(car)


class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 == 0:
            return self.num1 / self.num2


nums = Calc(3, 4)
print(nums.add())
print(nums.sub())
print(nums.mul())
print(nums.div())

# 클래스 변수와 인스턴스 변수


class Dog:
    kind = "진돗개"  # 클래스 변수

    def __init__(self, name):
        self.name = name  # 인스턴스 변수


# 인스턴스 변수 접근
dog1 = Dog("백구")
dog2 = Dog("초코")

print(dog2.name)

# 클래스 변수 접근
print(dog1.kind)  # 사용 안함
print(Dog.kind)


class Example:
    shared = "공유 변수"

    def __init__(self, name):
        self.name = name  # 인스턴스변수


e1 = Example("a")
e2 = Example("b")

Example.shared = "변경된 공유 변수"

print(e1.shared)
print(e2.shared)


# 사번 자동 발급


class Employee:
    serial_num = 1000  # 클래스 변수

    def __init__(self, name):
        Employee.serial_num += 1  # 1씩 증가
        self.id = Employee.serial_num  # 사번

        self.name = name

    def __str__(self):
        return f"사번: {self.id}, 이름: {self.name}"


e1 = Employee("홍길동")
print(e1)

e2 = Employee("김지원")
print(e2)

employees = [Employee("이몽룡"), Employee("김"), Employee(
    "이"), Employee("박"), Employee("최"), Employee("양"), Employee("강")]

for employee in employees:
    print(employee)



class Supermarket:
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self):
        print(f"위치: {self.location}")

    def change_category(self, new_product):
        self.product = new_product
        print(f"새 상품: {self.product}")

    def show_list(self):
        print(f"상품: {self.product}")

    def enter_customer(self):
        self.customer += 1

    def show_info(self):
        print(f"위치: {self.location}, 이름: {self.name}, 상품: {
              self.product}, 고객수: {self.customer}")


s1 = Supermarket("마포구 염리동", "마켓온", "음료", 12)

s1.show_info()

s1.enter_customer()

s1.show_info()

s1.change_category("ee")

s1.show_info()

s1.print_location()

# 실습 2, 리더 코드


class Supermarket:
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self):
        print(f"위치: {self.location}")

    def change_category(self, new_product):
        self.product = new_product

    def show_list(self):
        print(f"상품: {self.product}")

    def enter_customer(self):
        self.customer += 1

    def show_info(self):
        print(f"위치: {self.location}, 이름: {self.name}, 상품: {
              self.product}, 고객 수: {self.customer}")


s1 = Supermarket("마포구 염리동", "마켓온", "음료", 12)
s2 = Supermarket("은평구 응암동","응암마켓", "과자", 9)
s1.print_location()

s1.show_list()

s1.show_info()



class Person:
    def __init__(self):
        self._name = ""
        self._age = 0

    def setname(self, name):
        self._name = name

    def getname(self):
        return self._name

    def setage(self, age):
        self._age = age

    def getage(self):
        return self._age


p1 = Person()
p1.setname("홍길동")

print(p1.getname())
"""


class Health:
    def __init__(self):

        self.__name = ""

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def sethp(self, hp):
        self.__hp = hp

    def gethp(self):
        return self.__hp

    def exercise(self, hours):
        self.__hp += hours
        print(f"{hours}시간 동안 운동하다.")

    def drink_alcohol(self, cup):
        self.__hp -= cup
        print(f"술을 {cup}잔 마시다.")

    def show_status(self):
        print(f"{self.__name} - hp: {self.__hp}")
        print("================")


p1 = Health()
p1.setname("나몸짱")
p1.sethp(100)
p1.exercise(5)
p1.drink_alcohol(2)
p1.show_status()
