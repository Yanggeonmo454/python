"""
# 부모 클래스 생성자 없을떄.

class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

    def move(self):
        print("동물이 움직입니다.")


# 자식 클래스

class Cat(Animal):
    def meow(self):
        print("야옹")


cat = Cat()
cat.speak()
cat.move()
cat.meow()



# 부모 클래스에 생성자가 존재할 때:


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}이 움직입니다.")

    def move(self):
        print(f"{self.name}이 움직입니다.")

# 자식클래스


class Cat(Animal):
    def __init__(self, name, sound="야옹"):
        super().__init__(name)
        self.sound = sound

    def meow(self):
        print(f"{self.name}가 {self.sound} 웁니다.")


cat = Cat("장화")

cat.speak()
cat.move()
cat.meow()


# 다중상속


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Wheels:
    def __init__(self, count):
        self.count = count


class Car(Engine, Wheels):
    def __init__(self, horsepower, count):  # 어디에서 가져오는지 명확히 구분
        Engine.__init__(self, horsepower)
        Wheels.__init__(self, count)

    def info(self):
        print(f"이 자동차는 {self.horsepower}마력과 {self.count}개의 바퀴를 가지고 있습니다.")


car = Car(100, 4)
car. info()
print(Car.mro())

class Parent:
    def greet(self):
        print("안녕하세요. 부모 클래스")


class Child(Parent):
    def greet(self):
        super().greet()  # 부모 클래스에 있는걸 가져옴

        print("안녕하세요. 자식 클래스")


p = Parent()
c = Child()

p.greet()
c.greet()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount >
              0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")


class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period=12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    def extend_warranty(self, months):
        self.warranty_period += months
        print(f"보증기간이 {months}개월 연장되었습니다. 현재 보증기간: {self.warranty_period}개월")

    def display_info(self):
        super().display_info()


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def is_expired(self, current_date):

        if current_date > self.expiration_date:
            print(f"{self.name}는 유통기한이 지났습니다.")
        else:
            print(f"{self.name}는 유통기한이 지나지 않았습니다.")

    def display_info(self):
        super().display_info()


tv = Electronic("스마트 TV", 1500000, 10)
tv.display_info()
print()
tv.extend_warranty(6)
tv.display_info()

apple = Food("사과", 3000, 50, "2024-11-30")
apple.display_info()
print()
apple.is_expired("2024-11-28")

milk = Food("서울우유", 3000, 30, "2024-12-10")
milk.display_info()
milk.is_expired("2024-11-28")
"""

from abc import ABC, abstractmethod


class PaymentSystem(ABC):

    # 추상 메소드
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

    def payment_info(self, amount):
        print(f"{amount}원 결제가 완료되었습니다.")


class Kakaopay(PaymentSystem):
    def authenticate(self):
        print("카카오페이 인증완료 되었습니다.")

    def process_payment(self, amount):
        print(f"카카오페이로 {amount}원을 결제합니다.")


pay = 50000
kakao = Kakaopay()
kakao.authenticate()
kakao.process_payment()
kakao.payment_info()
