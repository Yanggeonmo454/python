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

# 실습. 클래스 종합 프로그래밍

from abc import ABC, abstractmethod

electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]

# 추상클래스


class ElctricityData(ABC):
    def __init__(self, usage_data, total_usage=0):
        self._usage_data = usage_data
        self._total_usage = total_usage

    @property
    def usage_data(self):
        return self._usage_data

    @usage_data.setter
    def usage_data(self, new_data):
        self._usage_data = new_data

    @property
    def total_usage(self):
        return self._total_usage

    @total_usage.setter
    def total_usage(self, new_total):
        self._total_usage = new_total

    # 추상메서드
    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    # 일반메서드
    def add_usage(self, date, usage):
        self._usage_data.append({"date": date, "usage": usage})

    def remove_usage(self, date):
        self._usage_data = [i for i in self._usage_data if i["date"] != date]


# 자식클래스
class HomeElectricityData(ElctricityData):
    # 추상메서드 구현
    def calculate_total_usage(self):
        self.total_usage = sum(i["usage"] for i in self.usage_data)

    def get_usage_on_date(self, date):
        for i in self.usage_data:
            if i["date"] == date:
                return i["usage"]

    # 클래스 메서드
    @classmethod
    def filter_date(cls, usage_data, start_date, end_date):
        filter_data = [i for i in usage_data if start_date <=
                       i["date"] <= end_date]
        return cls(filter_data)

    # 정적 메서드
    @staticmethod
    def max_usage(usage_data):
        return max(usage_data, key=lambda x: x["usage"])


home = HomeElectricityData(electricity_usage)
home.calculate_total_usage()
print("총 전력 사용량", home.total_usage)
print("특정날짜 ", home.get_usage_on_date("2024-11-05"))
home.add_usage("2024-11-29", 11.0)
home.remove_usage("2024-11-02")
print(home.usage_data)

result = HomeElectricityData.filter_date(
    electricity_usage, "2024-11-03", "2024-11-05")
print(result.usage_data)
max_result = HomeElectricityData.max_usage(electricity_usage)
print(max_result)
