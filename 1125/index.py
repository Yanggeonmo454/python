"""
fruits = ["사과", "포도", "바나나", "복숭아"]
for fruit in fruits:
    print("과일은 :", fruit)

number = [10, 20, 30, 40, 50]
total = 0
for num in number:
    total += num
print(f"리스트 값의 합계는 {total}입니다.")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in number:
    if num % 2 == 0:
        print(num, end=" ")


squares = [i ** 2 for i in range(1, 20) if i != 0]
print(squares)


even_squares = [i ** 2 for i in range(1, 10) if i % 2 == 0]
print(even_squares)


my_dict = {
    "name": "홍길동",
    "address": "서울시 은평구",
    "gender": "남자",
    "hobby": ["런닝", "헬스", "낚시"]
}

# 키값만 순회
for i in my_dict:
    [print(i)]

for i in my_dict.keys():
    print(i)

for i in my_dict.values():
    print(i)

my_dict = {
    "name": "홍길동",
    "address": "서울시 은평구",
    "gender": "남자",
    "hobby": ["런닝", "헬스", "낚시"]
}

for i, j in my_dict.items():
    print(i, j)
    print(f"{i}: {j}")


num = int(input("몇단을 입력할까요? "))

for i in range(1, 10):
    print(f"{num} * {i} = {num * i}")


n = int(input("어디까지 계산할까요?: "))
total = 0
for i in range(1, n+1):
    if i % 2 != 0:
        total += i

print(f"1부터 {n}까지의 홀수의 합: {total}")


students = {
    "학생1": {"국어": 83, "영어": 92, "수학": 88},
    "학생2": {"국어": 90, "영어": 79, "수학": 86},
    "학생3": {"국어": 88, "영어": 86, "수학": 94},
}


for student, scores in students.items():
    total = sum(scores.values())
    avg = total / len(scores)
    print(f"{student} 평균: {avg:.3f}")


# 실습 구구단 만들기

n = int(input("몇단을 출력할까요? "))

for i in range(1, 10):
    print(f"{n} * {i} = {n*i}")


# 실습. 정수 합 계산
n = int(input("어디까지 계산할까요?"))

total = 0

for i in range(1, n+1):
    if i % 2 != 0:
        total += n

print(f"1부터 {n} 까지의 홀수의 합 {total} ")


# 실습, 평균값 구하기

students = {
    "학생1": {"국어": 83, "영어": 92, "수학": 88},
    "학생2": {"국어": 90, "영어": 79, "수학": 86},
    "학생3": {"국어": 88, "영어": 86, "수학": 94},
}


for student, scores in students.items():
    total = sum(scores.values())
    avg = total / len(scores)
    print(f"{student} 평균: {avg:.3f}")



for i in range(5):
    for j in range(3):
        print(f"i :{i} j :{j}")
    print()


# 2차원 리스트와 for문

matrix = [
    [3, 6, 9, 12],
    [2, 4, 6, 8],
    [10, 20, 30, 40],
    [11, 12, 13, 14]
]

for row in matrix:
    for elem in row:
        if elem % 3 == 0:
            print(elem, end=" ")



for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}*{j} = {i * j} ")
    print()
"""

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

while True:
    print(f"남은 음료수: {vending_machine}")

    user_input = input("사용자 종류를 입력하세요. (소비자 또는 주인), 종료하려면 '종료' 입력: ")

    if user_input == "종료":
        print("프로그램을 종료합니다.")
        break

    if user_input == "소비자":
        cust_input = input("마시고 싶은 음료?: ")

        if cust_input in vending_machine:
            vending_machine.remove(cust_input)
            print(f"{cust_input} 드릴게요.\n 남은 음료수: {vending_machine}")
        else:
            print("해당 음료는 없습니다.")

    elif user_input == "주인":
        ad_input = input("할일 선택 (추가 또는 삭제를 입력하세요): ")

        if ad_input == "추가":
            new_drink = input("추가할 음료?: ")
            vending_machine.append(new_drink)
            print(f"추가완료.\n 현재 음료 목록: {vending_machine}")

        elif ad_input == "삭제":
            delete_drink = input("삭제할 음료?: ")
            if delete_drink in vending_machine:
                vending_machine.remove(delete_drink)
                print(f"삭제완료. \n 현재 음료 목록: {vending_machine}")
            else:
                print(f"{delete_drink}는 없네요.")
        else:
            print("추가 또는 삭제를 입력하세요.")

    else:
        print("소비자 또는 주인을 입력하세요.")
