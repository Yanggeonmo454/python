"""
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0],
]


while True:
    print("\n[날씨 데이터 분석 프로그램]\n1.평균 기온 계산\n2.최고/최저 기온 찾기\n3.강수량 분석\n4.날씨 데이터 추가\n5.전체 데이터 출력\n6.종료")

    user_input = int(input("원하는 기능의 번호를 입력하세요."))

    if user_input == 1:
        city = input("도시 이름을 입력하세요. (서울/부산): ")
        city_data = [data[2] for data in weather_data if data[1] == city]

        if city_data:
            average_temp = sum(city_data) / len(city_data)
            print(f"{city}의 평균 기온: {average_temp:.2f}'C")
        else:
            print(f"{city}에 대한 날씨 데이터가 없습니다.")

    elif user_input == 2:
        city = input("도시 이름을 입력하세요. (서울/부산) ")
        city_data = [data[2] for data in weather_data if data[1] == city]

        if city_data:
            max_temp = max(city_data)
            min_temp = min(city_data)
            print(f"{city}의 최고 기온: {max_temp}'C, 최저 기온: {min_temp}'C")
        else:
            print(f"{city}에 대한 날씨 데이터가 없습니다.")
    elif user_input == 3:
        city = input("도시 이름을 입력하세요. (서울/부산) ")
        city_data = [data[3] for data in weather_data if data[1] == city]
        rain_day = len(list(filter(lambda x: x > 0, city_data)))

        if city_data:
            print(f"{city}의 총 강수량: {sum(city_data)}mm")
            print(f"{city}의 강수량이 있었던 날: {(rain_day)}일")
        else:
            print(f"{city}에 대한 날씨 데이터가 없습니다.")

    elif user_input == 4:
        day = input("날짜를 입력하세요 (YYYY-MM-DD):")
        city = input("도시 이름을 입력하세요. (서울/부산) ")
        temp = float(input("평균 기온을 입력하세요. ('C): "))
        rain = float(input("강수량을 입력하세요. (mm): "))
        weather_data.append([day, city, temp, rain])
        print(f"{city}의 날씨 데이터가 추가되었습니다.")
    elif user_input == 5:
        print("현재 날씨 데이터: ")
        for data in weather_data:
            print(f"날짜: {data[0]}, 도시: {data[1]}, 평균 기온: {
                  data[2]}°C, 강수량: {data[3]}mm")
    elif user_input == 6:
        break
    else:
        print("원하는 기능의 번호를 정확히 입력하세요.")
"""
