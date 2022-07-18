import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")
cartoons = soup.find_all("a" , attrs={"class" : "title"}) # all 을 이용하면 최상의 1개 뿐만 아니라 다 가져옴 
# attrs은 ~~가 ~~일때 가져온다 함 
for cartoon in cartoons:
    print(cartoon.get_text())

#웹툰목록 다 가져오기 