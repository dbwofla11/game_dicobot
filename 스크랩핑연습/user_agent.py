import requests
res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()

with open("mygoogle.html" , "w" , encoding="utf8") as f:
    f.write(res.text)