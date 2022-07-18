import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=641253&weekday=fri"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")
cartoons = soup.find_all("td", attrs={"class" : "title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"] # 이러면 태그의 속성을 가져온다 
# print(title ,"https://comic.naver.com" +link)

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title , link)

     # 제목과 링크 가져오기 