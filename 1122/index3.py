
"""
i = 0
while i < 3:
    print("반복문", i)

    i += 1
print("종료")

num = 1
total = 0
while num <= 10:
    total += num  # total = total + num
    num += 1  # num = num+1
print(f"1부터 10까지의 합은 {total}입니다.")
"""

# 입력값 받기
"""
user_input = ""
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. 종료하려면 '종료'를 입력하세요.")
    print(f"입력한 값: {user_input}")
print("프로그램이 종료되었습니다.")


while True:
    dinner = input("오늘 저녁 뭐먹지?")
    if dinner == "제육":
        break
    print(f"오늘 저녁 메뉴는 {dinner}입니다.")
print("저녁 메뉴 완료")



count = 0
while True:
    print(count, end=" ")
    count += 1
    if count == 10:
        break


count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count, end="")

while True:
    user_input = input("숫자를 입력하세요 (종료하려면 '종료'를 입력하세요): ")

    if user_input == "종료":
        print("프로그램을 종료합니다.")
        break

    if not user_input.isdigit() or int(user_input) <= 0:
        print("양수만 입력하세요.")
        continue

    user_input = int(user_input)
    number = 1
    sum = 0

    while number <= user_input:
        sum += number
        number += 1

    print(f"1부터 {user_input}까지의 합은 {sum}입니다.")

"""

while True:

    user_input = input("양수를 입력하세요. ('종료' 입력시 프로그램 종료)")
    if user_input == "종료":
        print("프로그램을 종료합니다.")
        break
    if not user_input.isdigit():
        print("양수를 입력하세요")
        continue

    number = int(user_input)
    if number == 0:
        continue

    total = 0
    num = 1
    while num <= number:
        total += num
        num += 1

    print(f"1부터 {number}까지의 합은 {total}입니다.")
