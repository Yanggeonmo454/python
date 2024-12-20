import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox


def lotto(when):
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={
        when}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    numbers = soup.select("div.winning_number span.ball")
    lotto_numbers = [num.text for num in numbers]

    bonus_number = soup.select_one("div.bonus_number span.ball").text

    return lotto_numbers, bonus_number


def search():
    when = entry.get()
    if when:
        lotto_result, bonus_result = lotto(when)
        result_label.config(text=f"당첨 번호: {lotto_result}")
        bonus_label.config(text=f"보너스 번호: {bonus_result}")


window = tk.Tk()
window.title("로또 당첨 확인")

label = tk.Label(window, text="당첨 회차 입력")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="당첨번호 확인", command=search)
button.pack()

result_label = tk.Label(window)
result_label.pack()

bonus_label = tk.Label(window)
bonus_label.pack()

window.mainloop()
