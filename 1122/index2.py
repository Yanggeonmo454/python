"""
age = 21

if age < 20:
    print("미성년자 입니다.")
else:
    print("미성년자가 아닙니다.")

print(f"나이는 {age}입니다.")

password = input("비밀번호를 입력하세요.")

if password == "abc123":
    print("비밀번호가 맞습니다.")
else:
    print("비밀번호가 틀렸습니다.")


num = int(input("숫자를 입력하세요."))

if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

    

age = int(input("나이를 입력하세요:"))

if age < 20:
    print("10대입니다.")
elif age < 30:
    print("20대입니다")
elif age < 40:
    print("30대입니다.")
else:
    print("노인입니다.")
    
score = int(input("점수를 입력하세요:"))

if score >= 90:
    print("학점:A")
elif score >= 80:
    print("학점:B")
elif score >= 70:
    print("학점:C")
elif score >= 60:
    print("학점:D")
else:
    print("학점:F")


age = int(input("나이를 숫자로 입력해 주세요:"))
pay = input("결제방법을 입력해 주세요 (현금 또는 카드):")

if pay == "현금":
    if age < 8:
        price = "무료"
    elif age < 14:
        price = "450원"
    elif age < 20:
        price = "1000원"
    elif age < 75:
        price = "1300원"
    else:
        price = "무료"
elif pay == "카드":
    if age < 8:
        price = "무료"
    elif age < 14:
        price = "450원"
    elif age < 20:
        price = "720원"
    elif age < 75:
        price = "1200원"
    else:
        price = "무료"


print(f"{age}세의 {pay} 요금은 {price}입니다.")

# 삼항 연산자
age = int(input("나이를 입력하세요."))
message = "20대 입니다." if age < 30 and age >= 20 else "30대 입니다." if age < 40 and age >= 30 else "20대도 30대도 아닙니다."

print(message)


# in 연산자
fruit = input("과일을 한글로 입력하세요: ")

if fruit in ["사과", "바나나", "복숭아"]:
    print(f"{fruit}는 과일에 포함되어 있습니다.")
else:
    print("존재하지 않는 과일입니다.")
    """

fruit_cal = {
    "apple": 95,
    "banana": 105,
    "cherry": 50
}

fruit = input("과일을 영문으로 입력하세요. ").lower()

if fruit in fruit_cal:
    print(f"{fruit}의 칼로리는 {fruit_cal[fruit]}Kcal 입니다.")

else:
    print("존재하지 않는 과일입니다.")
