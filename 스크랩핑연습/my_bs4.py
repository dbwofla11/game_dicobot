#본격적인 스크랩핑 연습 
#beautifulsoup4로 네이버 웹툰 불러오기 
import requests
from bs4 import BeautifulSoup # 이거랑 내 파일의 이름이랑 같으면 안됨 
url = "https://comic.naver.com/webtoon/weekday"
myheaders = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"}

res = requests.get(url , headers=myheaders)
res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")
# print(soup.title) # 제목의 양식을 가져오기 
# print(soup.title.get_text()) # 태그를 불러오면 처음에 뜨는 태그를 갸지고온다 
# print(soup.a["href"]) # 이러면 요소를 가져옴 .attrs을 쓰면 속성을 다 가지고 옴 
# get_text()를 하게 되면 next_sibling을 사용못함 

#1등 (네이버 웹툰랭킹 )
def ranklist():
    rank1 = soup.find("li" , attrs={"class":"rank01"}) 
    # print(rank1.a.get_text()) 
    rank2 = rank1.find_next_sibling("li")
    # print(rank2.a.get_text())
    rank3 = rank2.find_next_sibling("li")
    rank4 = rank3.find_next_sibling("li")
    rank5 = rank4.find_next_sibling("li")
    return [rank1, rank2, rank3, rank4, rank5]

    
   
