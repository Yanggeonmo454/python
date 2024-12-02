"""
import time
import random

lotto = random.sample(range(1, 46), 6)
lotto.sort

print(lotto)
"""

import time

words = ["mountain", "river", "forest", "ocean", "desert",
         "tree", "flower", "cloud", "rain", "sunlight"]

print("타자 연습 게임을 시작합니다!")
input("시작하려면 아무키나 입력하세요.")

start_time = time.time()
score = 0

while True:
    if score >= len(words):
        print("모든 단어를 입력했습니다. 게임을 종료합니다!")
        break

    current_word = words[score]
    print(f"다음 단어: {current_word}")
    print("종료하려면 '종료'를 입력하세요.")

    user_input = input("타이핑하세요: ")

    if user_input == '종료':
        print("게임을 종료합니다.")
        break

    if user_input == current_word:
        print("통과!")
        score += 1
    else:
        print("오타가 있습니다. 다시 시도하세요.")

end_time = time.time()
total_time = end_time - start_time


average_time = total_time / score if score > 0 else 0

print(f"게임 종료! 총 {score}개의 단어를 입력하셨습니다.")
print(f"총 걸린 시간: {total_time:.2f}초")
print(f"평균 단어당 걸린 시간: {average_time:.2f}초")
