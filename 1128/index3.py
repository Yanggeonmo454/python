"""
# 클래스 메서드

class Converter:
    conversion_rate = 1.60934

    @classmethod
    def miles_to_kilometer(cls, mile):
        return mile * cls.conversion_rate


print(Converter.miles_to_kilometer(10))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)


p1 = Person.from_birth_year("홍길동", 1990)
print(p1. name, p1.age)


class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


Counter.increment()
Counter.increment()
Counter.increment()

print(Counter.get_count())


class Animal:
    species = "동물"

    @classmethod
    def get_species(cls):
        return cls.species


class Dog(Animal):
    species = "진돗개"


print(Animal.get_species())
print(Dog.get_species())

# 정적 메서드


class MathUtils:
    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def minus(a, b):
        return a-b


print(MathUtils.add(30, 40))
print(MathUtils.minus(10, 20))
"""

from abc import ABC, abstractmethod
electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]


class ElectricityData(ABC):
    def __init__(self, usage_data):
        self.usage_data = usage_data
        self._total_usage = self.calculate_total_usage()

    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):

        pass

    @property
    def total_usage(self):
        return self._total_usage


class HomeElectricityData(ElectricityData):
    def calculate_total_usage(self):
        return sum(data["usage"] for data in self.usage_data

    def get_usage_on_date(self, date):
        for data in self.usage_data:
            if data["date"] == date:
                return data["usage"]
        return "데이터가 없습니다."
