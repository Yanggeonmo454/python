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
"""

# 유효범위
quantity = 10


def price_sum(price):
    quantity = 7
    return price * quantity


print(price_sum(2000))
