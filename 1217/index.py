import folium
import pandas as pd
from geojson import Feature, FeatureCollection, Point

# my_map = folium.Map(location=[37.594306, 126.903542],
#                     zoom_start=12, tiles="https://mt1.google.com/vt/lyrs=s&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", attr="Google")

# folium.Marker([37.604166, 126.955212], popup="학교").add_to(my_map)

# my_map.save("./1217/my_map.html")


# my_map = folium.Map(location=[37.582759, 126.975605],
#                     zoom_start=13, tiles="CartoDB Positron")

# folium.Circle(location=[37.531002, 126.979725],
#               radius=500, color="blue").add_to(my_map)

# 딕셔너리 형태로 여러개 추가

# my_map = folium.Map(location=[37.604412, 126.915485], zoom_start=10)

# map_info = [
#     {"location": [37.612450, 126.9171417], "popup": "구산역"},
#     {"location": [37.608121, 126.924573], "popup": "역촌역"},
#     {"location": [37.601049, 126.917019], "popup": "응암역"},
#     {"location": [37.602409, 126.934014], "popup": "녹번역"},
#     {"location": [37.610840, 126.928864], "popup": "불광역"},
# ]

# subway_df = pd.DataFrame({
#     "latitude": [info["location"][0] for info in map_info],
#     "longitude": [info["location"][1] for info in map_info],
#     "popup": [info["popup"] for info in map_info],
# })

# for info in map_info:
#     folium.Marker(
#         location=info["location"],
#         popup=info["popup"],
#         icon=folium.Icon(color="green", icon="star")
#     ).add_to(my_map)

# my_map.save("./1217/my_map.html")

# subway_df.to_csv("./1217/subway.csv", index=False, encoding="utf-8-sig")

# subway_df.apply(lambda x : folium.Marker(location= x["latitude", x["longtitude"]], popup= x["popup"]))


# GeoJSON Feature 생성
import folium  # 지도 시각화를 위한 라이브러리
from geojson import Feature, FeatureCollection, Polygon  # GeoJSON 데이터를 생성하기 위한 라이브러리

# info = [
#     (126.625298, 37.405437),
#     (126.594733, 37.716833),
#     (126.962670, 37.808503),
#     (127.232491, 37.674486),
#     (127.080856, 37.403954),
#     (126.625298, 37.405437)
# ]

# feature = Feature(geometry=Polygon([info]),
#                   properties={"name": "수도권"}
#                   )
# geojson_data = FeatureCollection([feature])

# my_map = folium.Map(location=[37.5665, 126.9780], zoom_start=10)

# folium.GeoJson(
#     geojson_data,
#     name="Geojson Data",
#     tooltip=folium.GeoJsonTooltip(
#         fields=["name"],
#         aliases=["영역 이름: "]
#     )
# ).add_to(my_map)
# my_map.save("./1217/my_geojson_map.html")
