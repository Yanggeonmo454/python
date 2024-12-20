import folium
import requests
import cv2
from folium.plugins import HeatMap
from geojson import Feature, FeatureCollection, Point
from folium.features import GeoJsonTooltip

# api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
# params = {
#     "category": "wildfires",
#     "status": "open"

# response = requests.get(api_url, params=params)
# heatmap = []

# if response.status_code == 200:
#     data = response.json()
#     events = data.get('events', [])

#     for event in events:
#         coordinates = event.get('geometry', [{}])[0].get('coordinates')

#         if coordinates:
#             longitude = coordinates[0]
#             latitude = coordinates[1]
#             heatmap.append([latitude, longitude])

# map = folium.Map(location=[0, 0], zoom_start=2)
# HeatMap(heatmap, radius=15).add_to(map)
# map.save("./1218/heatmap.html")

# fire 데이터터


def get_fire_data():
    features = []

    api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    params = {
        "category": "wildfires",
        "status": "open",
        "limit": 30
    }

    res = requests.get(api_url, params=params)
    api_data = res.json()
    events = api_data["events"]

    for event in events:
        title = event["title"]
        geometry = event['geometry']
        date = geometry[0]["date"]
        magnitude = geometry[0]["magnitudeValue"] if geometry and "magnitudeValue" in geometry[0] else "0.0"

        # 좌표 추출
        coordinates = geometry[0]["coordinates"]

        # geojson 데이터로 변환
        features.append(
            Feature(
                geometry=Point(coordinates[0], coordinates[1]),
                properties={"name": title,
                            "magnitude": magnitude, "date": date}
            )
        )

    geojson_data = FeatureCollection(features)
    return geojson_data


# 지도 시각화 함수
def fire_map():
    m = folium.Map(location=[0, 0], zoom_start=5)

    # geojson 데이터 가져오기
    fire_data = get_fire_data()

    # GeoJson 추가
    folium.GeoJson(
        fire_data,
        name="화재 데이터",
        tooltip=GeoJsonTooltip(
            fields=["name", "magnitude", "date"],
            aliases=["지역명", "면적", "날짜"]
        )
    ).add_to(m)

    heat_data = [
                [feature["geometry"]["coordinates"][1], feature["geometry"]
                    ["coordinates"][0]]  # [위도, 경도] 순으로 설정
        for feature in fire_data["features"]
        if feature['properties']['magnitude'] != None
    ]

    HeatMap(heat_data).add_to(m)

    # 지도 저장
    m.save('fire_map.html')


def download_img():
    api_url = "https://wvs.earthdata.nasa.gov/api/v1/snapshot"
    params = {
        "REQUEST": "GetSnapshot",
        "BBOX": "-90,-180,90,180",
        "WIDTH": "1920",
        "HEIGHT": "1080",
        "FORMAT": "image/png",
        "LAYERS": "VIIRS_SNPP_CorrectedReflectance_TrueColor",
        "CRS": "EPSG:4326",
        "TIME": "2024-11-01"
    }

    res = requests.get(api_url, params=params, stream=True)
    print(res.iter_content(1024))
    with open("./1218/test.png", "wb") as file:
        for chunk in res.iter_content(1024):
            file.write(chunk)


def fire_result():
    image = cv2.imread("./1218/test.png")
    if image is None:
        return


# 함수 실행
fire_map()
