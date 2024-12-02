import requests
import json


url = "https://koreanjson.com/posts"
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    for i in data:
        print(f"ID: {i['id']}, 제목: {i['title']}")

else:
    print("fail")

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
