from datetime import datetime, timedelta
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import pandas as pd


# 데이터 불러오기
file_path = './1224/휴일포함_수정_재정렬.csv'
data = pd.read_csv(file_path, encoding='euc-kr')

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'])

# 필요한 컬럼 추출
data['Temperature'] = data['기온(°C)']  # 기온 컬럼 이름이 다를 경우 수정 필요
data['Power Demand'] = data['발전수요량']  # 발전수요량 컬럼 이름이 다를 경우 수정 필요


def clicked():
    selected_date = calendar.get_date()  # 선택된 날짜 가져오기
    time = time_combobox.get()

    selected_datetime = datetime.strptime(
        f"{selected_date} {time}", "%Y-%m-%d %H:%M")

    label2.config(text=f"선택한 날짜: {selected_datetime}")
    calculate_expecting_energy(selected_datetime)


def duration(selected_datetime):
    if selected_datetime < datetime(2024, 9, 30):
        start_date = selected_datetime - timedelta(days=30)
        end_date = selected_datetime - timedelta(hours=1)
        start_time = selected_datetime.replace(
            minute=0, second=0, microsecond=0) - timedelta(days=0)
        end_time = selected_datetime.replace(
            minute=59, second=59, microsecond=999999) - timedelta(days=0)
    else:
        start_date = selected_datetime - timedelta(days=365)
        end_date = selected_datetime - timedelta(days=335)
        start_time = selected_datetime.replace(
            minute=0, second=0, microsecond=0) - timedelta(days=365)
        end_time = selected_datetime.replace(
            minute=59, second=59, microsecond=999999) - timedelta(days=365)

    return start_date, end_date, start_time, end_time


def calculate_expecting_energy(selected_datetime):
    # 기간 설정 (예시: 2023년 1월 1일의 30일 전부터 하루 전까지)
    start_date, end_date, start_time, end_time = duration(selected_datetime)
    date_data = data[(data['일시'] >= start_date) & (data['일시'] <= end_date)]
    filtered_data = date_data
    # 사용자 설정 기온 범위
    time_data_in_range = data[(data['일시'] >= start_time) & (
        data['일시'] <= end_time)].reset_index(drop=True)

    avg_temp = time_data_in_range['기온(°C)'].mean()  # 사용자가 입력한 최소 기온
    min_temp = avg_temp - 0.5  # 단일 값으로 min_temp 설정
    max_temp = avg_temp + 0.5  # 단일 값으로 max_temp 설정

    # 설정한 기온 범위에 해당하는 데이터 필터링
    filtered_temp_data = filtered_data[(filtered_data['Temperature'] >= min_temp) &
                                       (filtered_data['Temperature'] <= max_temp)].reset_index(drop=True)

    # 일사 컬럼 범위 필터링: 예를 들어, 0 이상 1 미만, 1 이상 2 미만 등
    if time_data_in_range['일사(MJ/m2)'].between(0, 1).any():
        filtered_temp_data = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            0, 1)]
    elif time_data_in_range['일사(MJ/m2)'].between(1, 2).any():
        filtered_temp_data = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            1, 2)]
    elif time_data_in_range['일사(MJ/m2)'].between(2, 3).any():
        filtered_temp_data = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            2, 3)]

    # '휴일' 컬럼이 'O'인 데이터 필터링 추가
    filtered_temp_data_holiday = filtered_temp_data[filtered_temp_data['휴일'] == 'O']
    filtered_temp_data_non_holiday = filtered_temp_data[filtered_temp_data['휴일'] != 'O']

    # 각 그룹의 평균 발전수요량 계산
    avg_demand_holiday = filtered_temp_data_holiday['Power Demand'].mean()
    avg_demand_non_holiday = filtered_temp_data_non_holiday['Power Demand'].mean(
    )

    if (date_data['휴일'] == 'O').any():
        text.insert(END, f" \n {selected_datetime}의 예상 전력수요량 : {
                    avg_demand_holiday:.2f}")
    else:
        text.insert(END, f" \n {selected_datetime}의 예상 전력수요량 : {
                    avg_demand_non_holiday:.2f}")

    # 예측값 설정 (휴일: 휴일 평균, 비휴일: 비휴일 평균)
    filtered_temp_data_holiday = filtered_temp_data_holiday.copy()
    filtered_temp_data_non_holiday = filtered_temp_data_non_holiday.copy()

    filtered_temp_data_holiday['Predicted'] = avg_demand_holiday
    filtered_temp_data_non_holiday['Predicted'] = avg_demand_non_holiday
    today_demand = time_data_in_range['발전수요량'][0]

    # MAPE 계산 함수
    def calculate_mape(actual, predicted):
        return abs((actual - predicted) / actual) * 100

    # 휴일과 비휴일 각각의 MAPE 계산
    holiday_mape = calculate_mape(today_demand, avg_demand_holiday)
    non_holiday_mape = calculate_mape(today_demand, avg_demand_non_holiday)

    if selected_datetime < datetime(2024, 9, 30) and (date_data['휴일'] == 'O').any():
        text.insert(END, f" \n {selected_datetime}의 실제 전력수요량 : {
                    today_demand:.2f} MAPE : {holiday_mape:.2f}%")
        text.insert(END, f" \n")

    elif selected_datetime < datetime(2024, 9, 30) and (date_data['휴일'] != 'O').any():
        text.insert(END, f" \n {selected_datetime}의 실제 전력수요량 : {
                    today_demand:.2f} MAPE : {non_holiday_mape:.2f}%")
        text.insert(END, f" \n")

    else:
        text.insert(END, f" \n {selected_datetime}의 실시간 데이터가 아직 집계되지 않았습니다")
        text.insert(END, f" \n")


def erased():
    label2.config(text="선택한 날짜: ")
    text.delete("1.0", END)


root = Tk()
root.title('전력수요량 예측')
root.geometry('640x520')

label1 = Label(
    root, text='전력수요량 예측하고 싶은 날짜를 입력하세요(YYYY-MM-DD)', bg='lightgray')
label1.grid(row=0, column=0, padx=40, pady=10, sticky='n', columnspan=2)

calendar = DateEntry(root, width=40)
calendar.grid(row=1, column=0, padx=40, pady=0, sticky='n', columnspan=2)

# 시간 선택용 Combobox 위젯
time_values = [f"{i}:00" for i in range(24)]  # 24시간 형식
time_combobox = ttk.Combobox(root, values=time_values, state="readonly")
time_combobox.set("시간을 입력해주세요")
time_combobox.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

button1 = Button(root, text='입력', command=clicked)
button1.grid(row=4, column=0, padx=0, pady=10, sticky='n')

button2 = Button(root, text='삭제', command=erased)
button2.grid(row=4, column=1, padx=0, pady=10, sticky='n')

label2 = Label(root, text="선택한 날짜: ", bg='lightgray')
label2.grid(row=5, column=0, padx=10, pady=10, sticky='n', columnspan=2)

text = Text(root, width=80, height=20)
text.grid(row=6, column=0, padx=40, pady=20, sticky='n', columnspan=2)

root.mainloop()
