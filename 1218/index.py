import folium
import requests
from folium.plugins import HeatMap

api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
params = {
    "category": "wildfires",
    "status": "open"
}

response = requests.get(api_url, params=params)
heatmap = []

if response.status_code == 200:
    data = response.json()
    events = data.get('events', [])

    for event in events:
        coordinates = event.get('geometry', [{}])[0].get('coordinates')

        if coordinates:
            longitude = coordinates[0]
            latitude = coordinates[1]
            heatmap.append([latitude, longitude])

map = folium.Map(location=[0, 0], zoom_start=2)
HeatMap(heatmap, radius=15).add_to(map)
map.save("./1218/heatmap.html")
