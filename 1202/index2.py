# 예외 처리
"""
try:
    x = int(input("숫자를 입력하세요."))
    result = 10 / x

except (ZeroDivisionError, ValueError) as e:
    print("예외메시지:", e)

else:
    print(f"result: {result}")

finally:
    print("프로그램이 종료됩니다.")
"""


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌수 없습니다.")
    return a / b


try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("예외발생", e)
else:
    with open("result.txt", "w", encoding="utf8") as file:
        file.write(f"결과: {result}")
