# from tkinter import *
from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("윈도우 프로그래밍 연습")
root.geometry("640x480")


# 기본 창 띄우기기
# label = tk.Label(root, text="안녕하세요")
# label.pack(side="left")

# label1 = tk.Label(root, text="TOP", bg="red", fg="white")
# label1.pack(side="top", fill="x", padx=5, pady=5)

# label2 = tk.Label(root, text="BOTTOM", bg="blue", fg="white")
# label2.pack(side="bottom", fill="x", padx=5, pady=5)

# label3 = tk.Label(root, text="LEFT", bg="green", fg="white")
# label3.pack(side="left", fill="y", padx=5, pady=5)

# label4 = tk.Label(root, text="RIGHT", bg="yellow", fg="black")
# label4.pack(side="right", fill="y", padx=5, pady=5)

# label5 = tk.Label(root, text="CENTER", bg="purple", fg="white")
# label5.pack(side="top", fill="both", expand=True, padx=5, pady=5)

# root.mainloop()

# label1 = tk.Label(root, text="label1", bg="red", fg="white")
# label1.grid(row=0, column=0, padx=10, pady=10)

# label2 = tk.Label(root, text="label2", bg="blue", fg="white")
# label2.grid(row=0, column=1, padx=10, pady=10)

# label3 = tk.Label(root, text="label3", bg="green", fg="white")
# label3.grid(row=1, column=0, padx=10, pady=10)

# label4 = tk.Label(root, text="RIGHT", bg="yellow", fg="black")
# label4.grid(row=1, column=1, padx=10, pady=10)

# label5 = tk.Label(root, text="CENTER", bg="purple", fg="white")
# label5.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

# label = tk.Label(root, text="Hello, tkinkter", font=("Pretendard"), fg="blue")
# label.pack()

# def on_click():
#     print("Button Click")


# button = tk.Button(root, text="Click!", command=on_click)
# button.pack()

# def show_text():
#     # entried = entry.get()
#     # label.config(text=f"입력된 문자는 : {entried}")
#     # entry.delete(0, tk.END)  # 엔트리에 있는 문자열 삭제제
#     print(text.get("1.0", tk.END))


# # entry = tk.Entry(root, width=30)
# # entry.pack()
# text = tk.Text(root, width=40, height=10)
# text.pack()

# button = tk.Button(root, text="버튼 클릭", command=show_text)
# button.pack(side="left")

# label = tk.Label(root, text="")
# label.pack()

# top_frame = tk.Frame(root, bg="lightblue")
# top_frame.pack(fill="x")
# tk.Label(top_frame, text="top frame").pack()

# bottom_frame = tk.Frame(root, bg="lightgreen")
# bottom_frame.pack(fill="both", expand=True)
# tk.Label(bottom_frame, text="botton frame").pack()

# def show_state():
#     print("check는 ", var.get())


# var = tk.IntVar()
# checkbtn = tk.Checkbutton(
#     root, text="동의합니다.", variable=var, command=show_state)
# checkbtn.pack()

# def show_choice():
#     print("선택: ", var.get())


# var = tk.StringVar(value="option1")

# radio1 = tk.Radiobutton(root, text="옵션1", variable=var,
#                         value="option1", command=show_choice)
# radio1.pack(pady=10)


# radio2 = tk.Radiobutton(root, text="옵션2", variable=var,
#                         value="option2", command=show_choice)
# radio2.pack(pady=10)

# def show_select():
#     selection = listbox.curselection()
#     if selection:
#         print(f"선택된 과일은: {listbox.get(selection[0])}")


# listbox = tk.Listbox(root)
# listbox.pack(pady=10)
# for item in ["사과", "바나나", "포도", "체리"]:
#     listbox.insert(tk.END, item)

# button = tk.Button(root, text="선택", command=show_select)
# button.pack(pady=10)


# def show_info():
#     messagebox.showinfo("경고", "메세지창 띄우기")


# button = tk.Button(root, text="show info", command=show_info)
# button.pack(pady=10)


def new_file():
    messagebox.showinfo("메뉴", "파일이 선택되었습니다.")


def exit_app():
    root.quit()


menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_app)

menubar.add_cascade(label="파일", menu=filemenu)
root.config(menu=menubar)

root.mainloop()
