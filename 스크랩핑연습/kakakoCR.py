# 숭실대 학사 공지사항 가지고 오기 
import requests
from bs4 import BeautifulSoup 

num = 2 # 2페이지  
url = "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%ED%95%99%EC%82%AC&keyword"
url2 = "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/page/{}/?f&category=%ED%95%99%EC%82%AC&keyword".format(num) # 2번째 페이지 
myheaders = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"}

res = requests.get(url , headers=myheaders)
res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")
tags = soup.find_all("span", attrs={"class" : "tag ing"})

title = soup.find_all("div" , attrs={"class" : "row no-gutters align-items-center"} )

status = []
for tag in tags:
    status.append(tag.get_text()) 
# 인덱스 0 부터 시작하는 진행도 상태  # 상태가 진행이여야만 웹 스크랩핑이 가능하게끔 할거임 
# ["진행" , "진행" , "진행" , "진행" , "진행"] # 이렇게 진행인 a 태그만 스크랩핑 설계

# rank = s


# def best_notice():
