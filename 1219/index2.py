# # # 쿠폰 추첨기

# # from tkinter import *
# # import random


# # def on_click():
# #     name_list = ["강성연", "김준식", "양건모", "오소정", "임유빈", "정태영", "조우성", "조효정"]

# #     # win = []
# #     # while len(win) < 3:
# #     name = random.sample(name_list, 2)

# #     text.delete(1.0, END)
# #     text.insert(END, name)


# # window = Tk()
# # window.title("쿠폰 추첨기")

# # # label_img = Label(window)
# # # img = PhotoImage(file="./1213/test_image.jpg")
# # # label_img.config(image=img)
# # # label_img.pack()

# # Button(window, text="추첨", command=on_click).pack()

# # text = Text(window, width=40, height=5)
# # text.pack()

# # window.mainloop()

# import requests
# from bs4 import BeautifulSoup
# import tkinter as tk
# from tkinter import messagebox

# # 로또 번호를 가져오는 함수


# def lotto(num):
#     url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={
#         num}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"

#     # 요청 보내기
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     # 로또 번호 추출
#     numbers = soup.select("div.winning_number span.ball")
#     lotto_numbers = [num.text for num in numbers]

#     return lotto_numbers

# # 검색 버튼 클릭 시 실행되는 함수


# def on_search():
#     round_num = entry.get()  # 입력된 회차 번호 가져오기
#     if round_num:
#         lotto_result = lotto(round_num)  # 로또 번호 가져오기
#         result_label.config(text=f"당첨 번호: {', '.join(lotto_result)}")  # 결과 출력


# # tkinter 윈도우 생성
# window = tk.Tk()
# window.title("로또 당첨 확인")

# # 레이아웃
# label = tk.Label(window, text="당첨 회차 입력")
# label.pack()

# entry = tk.Entry(window)
# entry.pack(pady=10)

# search_button = tk.Button(window, text="당첨번호확인", command=on_search)
# search_button.pack(pady=10)

# result_label = tk.Label(window, text="당첨 번호가 여기 나타납니다.")
# result_label.pack(pady=20)

# # GUI 실행
# window.mainloop()
