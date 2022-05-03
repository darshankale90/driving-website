import json
import requests
headers = {"Authorization": "Bearer ya29.A0ARrdaM-wy0HeUa0KJIGVMTSgtJsvZKO3FJMuBs089WFipIMUdupYjEBeA-uzeGqtXVDF194zEkyRmutvhWJ_ISdTWe0K21svAK7ZuN_Cf5BDuREtglQKitzrRkAXaPv_bzH2G6MIUGGWVeLedJu0RY5TMwLi"}
para = {
    "name": "a.pdf",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("templates/logo_dark.png", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)