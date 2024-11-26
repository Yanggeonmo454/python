"""
# 함수

def say_hello(born, name):
    age = 2024 - born
    print(f"{name}님의 나이는 {age}세 입니다.")


say_hello(2000, "건모")



def gugudan(dan, end):
    print(f"{dan}단")
    for i in range(1, end+1):
        print(f"{dan} * {i} = {dan * i}")


gugudan(4, 20)



def calc_sum(num1, num2):
    total = 0
    for i in range(num1, num2 + 1):
        total += i

    return total


result = calc_sum(1, 10)
print(result)



def fruits():
    return ["사과", "바나나", "복숭아"]


print(fruits())


def students():
    return {
        "name": "홍길동",
        "age": "20",
        "major": "컴퓨터공학"
    }


print(students())





def func(num1, num2):
    if num1 == num2:
        return (f"결과(곱) : {num1 * num2}")
    else:
        return (f"결과(합): {num1 + num2}")


print(func(2, 3))


def ship(name, price):
    if price < 20000:
        price += 2500
        return (f"{name} 가격: {price}원")
    else:
        return (f"{name} 가격: {price}원")


print(ship("상품1", 5000))


# 함수 매개변수로 리스트 전달


def times(nums):
    return [i**2 for i in nums]


number = [2, 3, 6, 9]
print(times(number))


vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']


def check_machine():
    return f"남은 음료수: {vending_machine}"


def is_drink(drink):
    return drink in vending_machine


def add_drink(new_drink):
    vending_machine.append(new_drink)


def remove_drink(del_drink):
    vending_machine.remove(del_drink)


while True:
    print(check_machine())

    user_input = input("사용자 종류를 입력하세요. (소비자 또는 주인), 종료하려면 '종료' 입력: ")

    if user_input == "종료":
        print("프로그램을 종료합니다.")
        break

    if user_input == "소비자":
        drink = input("마시고 싶은 음료?: ")

        if is_drink(drink):
            remove_drink(drink)
            print(f"{drink} 드릴게요.")
            print(check_machine())
        else:
            print("해당 음료는 없습니다.")

    elif user_input == "주인":
        ad_input = input("할일 선택 (추가 또는 삭제를 입력하세요): ")

        if ad_input == "추가":
            new_drink = input("추가할 음료?: ")
            add_drink(new_drink)
            print(f"추가완료.\n 현재 음료 목록: {check_machine()}")

        elif ad_input == "삭제":
            del_drink = input("삭제할 음료?: ")
            if is_drink(del_drink):
                remove_drink(del_drink)
                print(f"삭제완료.")
                print(check_machine())
            else:
                print(f"{del_drink}는 없네요.")
        else:
            print("추가 또는 삭제를 입력하세요.")

    else:
        print("소비자 또는 주인을 입력하세요.")
"""
