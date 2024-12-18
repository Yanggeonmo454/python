import folium
import requests
import pandas as pd
from folium.plugins import HeatMap

API_KEY = "347624de9c4ee8ab325446ce279950e1"


def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={
        lat}&lon={lon}&appid={API_KEY}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return None


cities = [
    {"name": "서울", "lat": 37.543593, "lon": 126.981818},
    {"name": "부산", "lat": 35.138495, "lon": 129.053420},
    {"name": "대전", "lat": 36.340024, "lon": 127.400705},
    {"name": "대구", "lat": 35.858680, "lon": 128.589845}
]

weather_data = []

for city in cities:
    data = get_weather_data(city["lat"], city["lon"])
    if data:
        weather_data.append(
            {"city": city["name"],
             "temperature": data["main"]["temp"],
             "weather": data["weather"][0]["description"],
             "lat": city["lat"],  # 'Latitude' → 'lat'
             "lon": city["lon"]   # 'longtitude' → 'lon'
             })

weather_df = pd.DataFrame(weather_data)
print(weather_df)

# 지도 생성
my_map = folium.Map(location=[36.841375, 127.930471], zoom_start=7)

# 마커 추가
for _, row in weather_df.iterrows():
    popup_info = f"""
    <b>도시:</b> {row["city"]}<br />
    <b>온도:</b> {row["temperature"] - 273.15:.2f}°C<br />
    <b>날씨:</b> {row["weather"]}
    """

    # 날씨에 따라서 마커 색상 설정
    icon_color = "blue" if row["temperature"] - 273.15 < 0 else "orange"

    # 마커 생성
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=folium.Popup(popup_info),
        icon=folium.Icon(color=icon_color, icon="cloud")
    ).add_to(my_map)

# HTML 파일로 저장
my_map.save("./1217/my_map.html")
