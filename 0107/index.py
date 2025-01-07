from datetime import datetime, timedelta
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib import font_manager
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import re

html_url = "https://www.kpx.or.kr/powerinfoJeju.es?mid=a10404040000"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

demand_now = soup.select(
    '#contents_body > div > div > table > tbody > tr:nth-child(2) > td')

if demand_now:
    # 텍스트에서 숫자만 추출 (정규 표현식 사용)
    demand_value = demand_now[0].text.strip()  # '889 MW'와 같은 텍스트
    number_only = int(re.sub(r'[^\d]', '', demand_value))  # 숫자만 남기고 제거

demand_now1 = number_only*1000
print(demand_now1)

# 한글 폰트 설정
# 다른 폰트 사용 시 -기호 깨지는 현상이 있어서 natosans폰트를 다운로드 받음
# path = "C:/Windows/Fonts/NotoSansKR-Regular.ttf"
# font = font_manager.FontProperties(fname=path).get_name()
# plt.rc('font', family=font)

# 데이터 불러오기
file_path = './1224/휴일포함_수정.csv'
data = pd.read_csv(file_path, encoding='euc-kr')

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'])

# 필요한 컬럼 추출
data['Temperature'] = data['기온(°C)']  # 기온 컬럼 이름이 다를 경우 수정 필요
data['Power Demand'] = data['발전수요량']  # 발전수요량 컬럼 이름이 다를 경우 수정 필요


def duration(selected_datetime):
    if selected_datetime < datetime(2024, 9, 30):
        start_date = selected_datetime-timedelta(days=30)
        end_date = selected_datetime-timedelta(hours=1)
        start_time = selected_datetime.replace(
            minute=0, second=0, microsecond=0)-timedelta(days=0)
        end_time = selected_datetime.replace(
            minute=59, second=59, microsecond=999999)-timedelta(days=0)
    else:
        start_date = selected_datetime-timedelta(days=365)
        end_date = selected_datetime-timedelta(hours=1)
        start_time = selected_datetime.replace(
            minute=0, second=0, microsecond=0)-timedelta(days=365)
        end_time = selected_datetime.replace(
            minute=59, second=59, microsecond=999999)-timedelta(days=365)

    return start_date, end_date, start_time, end_time


def clicked():
    selected_date = calendar.get_date()  # 선택된 날짜 가져오기
    time = time_combobox.get()

    selected_datetime = datetime.strptime(
        f"{selected_date} {time}", "%Y-%m-%d %H:%M")

    label2.config(text=f"선택한 날짜: {selected_datetime}")

    if selected_datetime < datetime(2024, 9, 30):
        demand_0, holiday_demand_0, non_holiday_demand_0, holiday_mape_0, non_holiday_mape_0 = calculate_expecting_energy(
            selected_datetime)
        demand_1, holiday_demand_1, non_holiday_demand_1, holiday_mape_1, non_holiday_mape_1 = calculate_expecting_energy(
            selected_datetime + timedelta(hours=1))
        demand_2, holiday_demand_2, non_holiday_demand_2, holiday_mape_2, non_holiday_mape_2 = calculate_expecting_energy(
            selected_datetime + timedelta(hours=2))

        plot_graph(selected_datetime, demand_0, holiday_demand_0, non_holiday_demand_0, holiday_mape_0, non_holiday_mape_0,
                   demand_1, holiday_demand_1, non_holiday_demand_1, holiday_mape_1, non_holiday_mape_1,
                   demand_2, holiday_demand_2, non_holiday_demand_2,  holiday_mape_2, non_holiday_mape_2
                   )
    else:
        demand_0, holiday_demand_0, non_holiday_demand_0, holiday_mape_0, non_holiday_mape_0 = calculate_expecting_energy(
            selected_datetime)
        demand_1, holiday_demand_1, non_holiday_demand_1, holiday_mape_1, non_holiday_mape_1 = calculate_expecting_energy1(
            selected_datetime + timedelta(hours=1))
        demand_2, holiday_demand_2, non_holiday_demand_2, holiday_mape_2, non_holiday_mape_2 = calculate_expecting_energy1(
            selected_datetime + timedelta(hours=2))

        demand_0 = demand_now1

        plot_graph(selected_datetime, demand_0, holiday_demand_0, non_holiday_demand_0, holiday_mape_0, non_holiday_mape_0,
                   demand_1, holiday_demand_1, non_holiday_demand_1, holiday_mape_1, non_holiday_mape_1,
                   demand_2, holiday_demand_2, non_holiday_demand_2,  holiday_mape_2, non_holiday_mape_2
                   )


def plot_graph(selected_datetime, demand_0, holiday_demand_0, non_holiday_demand_0, holiday_mape_0, non_holiday_mape_0,
               demand_1, holiday_demand_1, non_holiday_demand_1, holiday_mape_1, non_holiday_mape_1,
               demand_2, holiday_demand_2, non_holiday_demand_2,  holiday_mape_2, non_holiday_mape_2):

    days = ['현재 시간', '1시간 뒤', '2시간 뒤']

    # 전력수요량 데이터
    demand = [demand_0, demand_1, demand_2]

    # 휴일 전력수요량
    holiday_demand = [holiday_demand_0, holiday_demand_1, holiday_demand_2]

    # 비휴일 전력수요량
    non_holiday_demand = [non_holiday_demand_0,
                          non_holiday_demand_1, non_holiday_demand_2]

    # 전체 전력수요량
    total_demand = [holiday_demand_0 + non_holiday_demand_0,
                    holiday_demand_1 + non_holiday_demand_1,
                    holiday_demand_2 + non_holiday_demand_2]

    # holiday_mape = [holiday_mape_yesterday,
    #                 holiday_mape_today, holiday_mape_tomorrow]

    # non_holiday_mape = [non_holiday_mape_yesterday,
    #                     non_holiday_mape_today, non_holiday_mape_tomorrow]

    # total_mape = [holiday_mape_yesterday + non_holiday_mape_yesterday,
    #               holiday_mape_today + non_holiday_mape_today,
    #               holiday_mape_tomorrow + non_holiday_mape_tomorrow]

    # Matplotlib 그래프 생성
    fig, ax = plt.subplots()
    x = np.arange(len(days))  # ['어제', '오늘', '내일']

    # 막대 너비
    bar_width = 0.35

    # 'demand'와 'total_demand'에 대한 막대 그래프 생성
    if selected_datetime < datetime(2024, 9, 30):
        bars = ax.bar(x - bar_width/2, demand, bar_width,
                      color='g', label='실제값 (Real Demand)')
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2,  # x 위치는 막대의 중앙으로 설정
                     bar.get_height() + 0.5,             # y 위치는 막대 높이에 0.5를 더한 곳
                     f'{int(bar.get_height())}',        # 소수점 없이 정수로 출력
                     ha='center',                       # 텍스트 수평 정렬
                     va='bottom',                       # 텍스트 수직 정렬
                     fontsize=10,                       # 글꼴 크기
                     color="k")                         # 텍스트 색상

        bars1 = ax.bar(x + bar_width/2, total_demand, bar_width,
                       color='r', label='예측값 (Expect Demand)')

        for bar in bars1:
            plt.text(bar.get_x() + bar.get_width() / 2,  # x 위치는 막대의 중앙으로 설정
                     bar.get_height() + 0.5,             # y 위치는 막대 높이에 0.5를 더한 곳
                     f'{int(bar.get_height())}',        # 소수점 없이 정수로 출력
                     ha='center',                       # 텍스트 수평 정렬
                     va='bottom',                       # 텍스트 수직 정렬
                     fontsize=10,                       # 글꼴 크기
                     color="k")                         # 텍스트 색상
    else:
        # 첫 번째 막대만 label을 지정하고 나머지는 label을 지정하지 않음
        bars = ax.bar(x - bar_width / 2, demand, bar_width,
                      color=['g'], label='실제값 (Real Demand)')

        # 두 번째와 세 번째 막대에는 label을 지정하지 않음 (중복 방지)
        ax.bar(x[1] - bar_width / 2, demand[1], bar_width, label='참고데이터(Reference Data)',
               color='b')  # 참고데이터(Reference Data)
        ax.bar(x[2] - bar_width / 2, demand[2], bar_width,
               color='b')  # 참고데이터(Reference Data)

        # 범례 추가 (중복 항목 자동으로 제거)
        ax.legend()

        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2,  # x 위치는 막대의 중앙으로 설정
                     bar.get_height() + 0.5,             # y 위치는 막대 높이에 0.5를 더한 곳
                     f'{int(bar.get_height())}',        # 소수점 없이 정수로 출력
                     ha='center',                       # 텍스트 수평 정렬
                     va='bottom',                       # 텍스트 수직 정렬
                     fontsize=10,                       # 글꼴 크기
                     color="k")                         # 텍스트 색상

        bars1 = ax.bar(x + bar_width/2, total_demand, bar_width,
                       color='r', label='예측값 (Expect Demand)')
        for bar in bars1:
            plt.text(bar.get_x() + bar.get_width() / 2,  # x 위치는 막대의 중앙으로 설정
                     bar.get_height() + 0.5,             # y 위치는 막대 높이에 0.5를 더한 곳
                     f'{int(bar.get_height())}',        # 소수점 없이 정수로 출력
                     ha='center',                       # 텍스트 수평 정렬
                     va='bottom',                       # 텍스트 수직 정렬
                     fontsize=10,                       # 글꼴 크기
                     color="k")                         # 텍스트 색상

    ax.yaxis.set_major_locator(MultipleLocator(100000))
    # 레이블과 제목 설정
    ax.set_title('선택된 날짜 기간 동안의 전력수요량 비교')
    ax.set_xlabel('날짜')
    ax.set_ylabel('전력수요량(kW)')
    ax.set_xticks(x)
    ax.set_xticklabels(days)
    ax.legend(loc='lower center')

    # 그래프 여백 조정
    plt.tight_layout()  # 자동으로 레이아웃 조정

    # 그래프를 Tkinter Canvas에 표시
    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame은 Tkinter 위젯입니다
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, padx=40, pady=5)


def duration(selected_datetime):
    if selected_datetime < datetime(2024, 9, 30):
        start_date = selected_datetime-timedelta(days=30)
        end_date = selected_datetime-timedelta(hours=1)
        start_time = selected_datetime.replace(
            minute=0, second=0, microsecond=0)-timedelta(days=0)
        end_time = selected_datetime.replace(
            minute=59, second=59, microsecond=999999)-timedelta(days=0)
    else:
        start_date = selected_datetime-timedelta(days=365)
        end_date = selected_datetime-timedelta(hours=1)
        start_time = selected_datetime.replace(
            minute=0, second=0, microsecond=0)-timedelta(days=365)
        end_time = selected_datetime.replace(
            minute=59, second=59, microsecond=999999)-timedelta(days=365)

    return start_date, end_date, start_time, end_time


def calculate_expecting_energy(selected_datetime):

    # 기간 설정 (예시: 2023년 1월 1일의의 30일 전부터 하루 전까지지)
    # 날짜 입력 받기 (형식: YYYY-MM-DD)
    start_date, end_date, start_time, end_time = duration(selected_datetime)
    date_data = data[(data['일시'] >= start_date) & (data['일시'] <= end_date)]
    filtered_data = date_data
    # 사용자 설정 기온 범위
    time_data_in_range = data[(data['일시'] >= start_time)
                              & (data['일시'] <= end_time)].reset_index(drop=True)

    avg_temp = time_data_in_range['기온(°C)'].mean()  # 사용자가 입력한 최소 기온
    min_temp = avg_temp - 0.5  # 단일 값으로 min_temp 설정
    max_temp = avg_temp + 0.5  # 단일 값으로 max_temp 설정

    # 설정한 기온 범위에 해당하는 데이터 필터링
    filtered_temp_data = filtered_data[(filtered_data['Temperature'] >= min_temp) &
                                       (filtered_data['Temperature'] <= max_temp)].reset_index(drop=True)

    # 일사 컬럼 범위 필터링: 예를 들어, 0 이상 1 미만, 1 이상 2 미만 등
    time_data_in_range['일사(MJ/m2)'] = time_data_in_range['일사(MJ/m2)'].fillna(0)
    filtered_temp_data['일사(MJ/m2)'] = filtered_temp_data['일사(MJ/m2)'].fillna(0)

    filtered_temp_data1 = []
    if time_data_in_range['일사(MJ/m2)'].between(0, 0.5).any():
        filtered_temp_data1 = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            0, 0.5)].reset_index(drop=True)
    elif time_data_in_range['일사(MJ/m2)'].between(0.5, 1).any():
        filtered_temp_data1 = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            0.5, 1)].reset_index(drop=True)
    elif time_data_in_range['일사(MJ/m2)'].between(1, 2).any():
        filtered_temp_data1 = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            1, 2)].reset_index(drop=True)
    elif time_data_in_range['일사(MJ/m2)'].between(2, 3).any():
        filtered_temp_data1 = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            2, 3)].reset_index(drop=True)

    if len(filtered_temp_data1) == 0:
        filtered_temp_data1 = filtered_temp_data

    # '휴일' 컬럼이 'O'인 데이터 필터링

    filtered_temp_data_holiday = filtered_temp_data1[filtered_temp_data1['휴일'] == 'O']
    filtered_temp_data_non_holiday = filtered_temp_data1[filtered_temp_data1['휴일'] != 'O']
    if filtered_temp_data_holiday.empty:
        filtered_temp_data_holiday = filtered_temp_data1
    if filtered_temp_data_non_holiday.empty:
        filtered_temp_data_non_holiday = filtered_temp_data1

    # 각 그룹의 평균 발전수요량 계산(계산 알고리즘)
    avg_demand_holiday = filtered_temp_data_holiday['Power Demand'].mean()
    avg_demand_non_holiday = filtered_temp_data_non_holiday['Power Demand'].mean(
    )

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
    # holiday_mape = calculate_mape(today_demand, avg_demand_holiday)
    # non_holiday_mape = calculate_mape(today_demand, avg_demand_non_holiday)

    if selected_datetime < datetime(2024, 9, 30) and (time_data_in_range['휴일'] == 'O').any():
        holiday_mape = calculate_mape(today_demand, avg_demand_holiday)
        avg_demand_non_holiday = 0
        non_holiday_mape = 0
        text.insert(END, f" \n {selected_datetime}의 예상 전력수요량 : {
                    avg_demand_holiday:.2f} ")
        text.insert(END, f" \n {selected_datetime}의 실제 전력수요량 : {
                    today_demand:.2f} 오차율 : {holiday_mape:.2f}%")
        text.insert(END, f" \n")

    elif selected_datetime < datetime(2024, 9, 30) and (time_data_in_range['휴일'] != 'O').any():
        non_holiday_mape = calculate_mape(today_demand, avg_demand_non_holiday)
        avg_demand_holiday = 0
        holiday_mape = 0
        text.insert(END, f" \n {selected_datetime}의 예상 전력수요량 : {
                    avg_demand_non_holiday:.2f}")
        text.insert(END, f" \n {selected_datetime}의 실제 전력수요량 : {
                    today_demand:.2f} 오차율 : {non_holiday_mape:.2f}%")
        text.insert(END, f" \n")

    else:
        non_holiday_mape = calculate_mape(demand_now1, avg_demand_non_holiday)
        text.insert(END, f" \n {selected_datetime}의 예상 전력수요량 : {
                    avg_demand_non_holiday:.2f}")
        text.insert(END, f" \n 과거데이터를 사용하여 예측한 전력수요량 : {
                    demand_now1:.2f} 오차율 : {non_holiday_mape:.2f}%")
        text.insert(END, f" \n")
        avg_demand_holiday = 0
        holiday_mape = 0

    return today_demand, avg_demand_holiday, avg_demand_non_holiday, holiday_mape, non_holiday_mape


def calculate_expecting_energy1(selected_datetime):

    # 기간 설정 (예시: 2023년 1월 1일의의 30일 전부터 하루 전까지지)
    # 날짜 입력 받기 (형식: YYYY-MM-DD)
    start_date, end_date, start_time, end_time = duration(selected_datetime)
    date_data = data[(data['일시'] >= start_date) & (data['일시'] <= end_date)]
    filtered_data = date_data
    # 사용자 설정 기온 범위
    time_data_in_range = data[(data['일시'] >= start_time)
                              & (data['일시'] <= end_time)].reset_index(drop=True)

    avg_temp = time_data_in_range['기온(°C)'].mean()  # 사용자가 입력한 최소 기온
    min_temp = avg_temp - 0.5  # 단일 값으로 min_temp 설정
    max_temp = avg_temp + 0.5  # 단일 값으로 max_temp 설정

    # 설정한 기온 범위에 해당하는 데이터 필터링
    filtered_temp_data = filtered_data[(filtered_data['Temperature'] >= min_temp) &
                                       (filtered_data['Temperature'] <= max_temp)].reset_index(drop=True)

    # 일사 컬럼 범위 필터링: 예를 들어, 0 이상 1 미만, 1 이상 2 미만 등
    time_data_in_range['일사(MJ/m2)'] = time_data_in_range['일사(MJ/m2)'].fillna(0)
    filtered_temp_data['일사(MJ/m2)'] = filtered_temp_data['일사(MJ/m2)'].fillna(0)

    filtered_temp_data1 = []
    if time_data_in_range['일사(MJ/m2)'].between(0, 0.5).any():
        filtered_temp_data1 = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            0, 0.5)].reset_index(drop=True)
    elif time_data_in_range['일사(MJ/m2)'].between(0.5, 1).any():
        filtered_temp_data1 = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            0.5, 1)].reset_index(drop=True)
    elif time_data_in_range['일사(MJ/m2)'].between(1, 2).any():
        filtered_temp_data1 = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            1, 2)].reset_index(drop=True)
    elif time_data_in_range['일사(MJ/m2)'].between(2, 3).any():
        filtered_temp_data1 = filtered_temp_data[filtered_temp_data['일사(MJ/m2)'].between(
            2, 3)].reset_index(drop=True)

    if len(filtered_temp_data1) == 0:
        filtered_temp_data1 = filtered_temp_data

    # '휴일' 컬럼이 'O'인 데이터 필터링

    filtered_temp_data_holiday = filtered_temp_data1[filtered_temp_data1['휴일'] == 'O']
    filtered_temp_data_non_holiday = filtered_temp_data1[filtered_temp_data1['휴일'] != 'O']
    if filtered_temp_data_holiday.empty:
        filtered_temp_data_holiday = filtered_temp_data1
    if filtered_temp_data_non_holiday.empty:
        filtered_temp_data_non_holiday = filtered_temp_data1

    # 각 그룹의 평균 발전수요량 계산(계산 알고리즘)
    avg_demand_holiday = filtered_temp_data_holiday['Power Demand'].mean()
    avg_demand_non_holiday = filtered_temp_data_non_holiday['Power Demand'].mean(
    )

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
    # holiday_mape = calculate_mape(today_demand, avg_demand_holiday)
    # non_holiday_mape = calculate_mape(today_demand, avg_demand_non_holiday)

    if selected_datetime < datetime(2024, 9, 30) and (time_data_in_range['휴일'] == 'O').any():
        holiday_mape = calculate_mape(today_demand, avg_demand_holiday)
        avg_demand_non_holiday = 0
        non_holiday_mape = 0
        text.insert(END, f" \n {selected_datetime}의 예상 전력수요량 : {
                    avg_demand_holiday:.2f} ")
        text.insert(END, f" \n {selected_datetime}의 실제 전력수요량 : {
                    today_demand:.2f} 오차율 : {holiday_mape:.2f}%")
        text.insert(END, f" \n")

    elif selected_datetime < datetime(2024, 9, 30) and (time_data_in_range['휴일'] != 'O').any():
        non_holiday_mape = calculate_mape(today_demand, avg_demand_non_holiday)
        avg_demand_holiday = 0
        holiday_mape = 0
        text.insert(END, f" \n {selected_datetime}의 예상 전력수요량 : {
                    avg_demand_non_holiday:.2f}")
        text.insert(END, f" \n {selected_datetime}의 실제 전력수요량 : {
                    today_demand:.2f} 오차율 : {non_holiday_mape:.2f}%")
        text.insert(END, f" \n")

    else:
        non_holiday_mape = calculate_mape(today_demand, avg_demand_non_holiday)
        text.insert(END, f" \n {selected_datetime}의 예상 전력수요량 : {
                    avg_demand_non_holiday:.2f}")
        text.insert(END, f" \n 과거데이터를 사용하여 예측한 전력수요량 : {
                    today_demand:.2f} 오차율 : {non_holiday_mape:.2f}%")
        text.insert(END, f" \n")
        avg_demand_holiday = 0
        holiday_mape = 0

    return today_demand, avg_demand_holiday, avg_demand_non_holiday, holiday_mape, non_holiday_mape


def erased():
    label2.config(text="선택한 날짜: ")
    text.delete("1.0", END)


def display_average_mape():
    messagebox.showinfo("현재 모델 MAPE 평균 값 : 8.77%",
                        f"적용한 파라미터 : 일시, 기온, 일사량, 휴일유무 ")


root = Tk()
root.title('전력수요량 예측')
root.geometry('1000x800')

# 그리드에 비율 설정
root.grid_columnconfigure(0, weight=1, uniform="equal")
root.grid_columnconfigure(1, weight=1, uniform="equal")
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=0)
root.grid_rowconfigure(5, weight=0)
root.grid_rowconfigure(6, weight=1, uniform="equal")  # 텍스트와 그래프가 있는 부분
root.grid_rowconfigure(7, weight=3, uniform="equal")  # 그래프가 들어갈 프레임

label1 = Label(
    root, text='전력수요량 예측하고 싶은 날짜를 입력하세요(YYYY-MM-DD)', bg='lightgray')
label1.grid(row=0, column=0, padx=40, pady=0, sticky='n', columnspan=2)

calendar = DateEntry(root, width=40)
calendar.grid(row=1, column=0, padx=40, pady=0, sticky='n', columnspan=2)

# 시간 선택용 Combobox 위젯
time_values = [f"{i}:00" for i in range(24)]  # 24시간 형식
time_combobox = ttk.Combobox(root, values=time_values, state="readonly")
time_combobox.set("시간을 입력해주세요")
time_combobox.grid(row=2, column=0, padx=10, pady=0, columnspan=2)

button1 = Button(root, text='입력', command=clicked)
button1.grid(row=4, column=0, padx=0, pady=0, sticky='n')

button2 = Button(root, text='삭제', command=erased)
button2.grid(row=4, column=1, padx=0, pady=0, sticky='n')

label2 = Label(root, text="선택한 날짜: ", bg='lightgray')
label2.grid(row=5, column=0, padx=10, pady=0, sticky='n', columnspan=2)

text = Text(root, width=80, height=10)
text.grid(row=6, column=0, padx=20, pady=5, sticky='n', columnspan=2)

# 그래프를 표시할 프레임 생성
frame = ttk.Frame(root)
frame.grid(row=7, column=0, padx=140, pady=5, columnspan=2, sticky='nsew')

display_average_mape()
root.mainloop()
