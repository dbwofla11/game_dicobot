#본격적인 스크랩핑 연습 
#beautifulsoup4로 네이버 웹툰 불러오기 
import requests
from bs4 import BeautifulSoup # 이거랑 내 파일의 이름이랑 같으면 안됨 
url = "https://comic.naver.com/webtoon/weekday"


res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")
# print(soup.title) # 제목의 양식을 가져오기 
# print(soup.title.get_text()) # 태그를 불러오면 처음에 뜨는 태그를 갸지고온다 
# print(soup.a["href"]) # 이러면 요소를 가져옴 .attrs을 쓰면 속성을 다 가지고 옴 

rank1 = soup.find("li" , attrs={"class":"rank01"})
print(rank1.a.get_text()) # 1등 웹툰의 제목 추출 





