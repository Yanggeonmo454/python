"""
s1 = {1, 2, 3, 3, 4}

print(s1)
s1.add(5)
print(s1)
s1.update({6, 7, 8, 9, 10})
print(s1)
s1.remove(3)
print(s1)
s1.discard(9)
print(s1)
#remove는 없는 요소를 입력하면 에러, discard는 아무일도 일어나지 않는다.


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 합집합
s3 = s1 | s2
print(s3)
# s3 = s1.union(s2)

# 교집합
s3 = s1 & s2
print(s3)
# s3 = s1.intersection(s2)

# 차집합
s3 = s2 - s1
print(s3)

# s3 = s2.difference(s1)

# dict

dict1 = {}

print(dict1)

dict1 = {
    "name": "홍길동",
    "age": 20,
    "city": "서울시",
    "hobby": ["런닝", "등산", "헬스"]
}

print(dict1)
dict2 = dict(name="geonmo", age=20)

print(dict2)

print(dict1["name"])
print(dict1["hobby"][2])
# 값 수정

dict1["age"] = 21
print(dict1)

# 값 추가
dict1["birthday"] = 20000101
print(dict1)
dict1["hobby"] = ['런닝', '등산', '헬스', "캠핑"]

print(dict1)

del dict1["birthday"]
print(dict1)

fruits = {"apple": "사과",
          "banana": " 바나나"
          }

print(fruits.get("apple"))

fruits.update({
    "grape": "포도",
    "melon": "멜론"
})

print(fruits)
print(fruits.keys())
print(fruits.values())
print(fruits.items())
fruits.clear()
print(fruits)


scores = {}

scores = {"Alice": 85,
          "Bob": 90,
          "Charlie": 95
          }

scores.update({"David": 80})

scores["Alice"] = 88

del scores["Bob"]

print(scores)

# 내장함수

numbers = [1, 2, 3, 4, 5, 6]
print(sum(numbers))

scores = {"국어": 90, "수학": 80, "영어": 60}
print(sum(scores.values()))


names = ["Alice", "Bob", "Chrarlie", "David"]
scores = [85, 90, 88, 95]
zipped = (zip(names, scores))

print(list(zipped))
"""
