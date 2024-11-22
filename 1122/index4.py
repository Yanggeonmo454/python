"""
for i in range(10):
    print(i, end=" ")
print()
for i in range(3, 9):
    print(i, end=" ")
print()

for i in range(1, 100, 12):
    print(i, end=" ")

fruits = ["사과", "바나나", "포도", "체리"]
for fruits in fruits:
    print(fruits, end="|")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for num in numbers:
    total += num
print(f"합계는 {total}입니다.")


"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0:
        print(num, end=" ")
