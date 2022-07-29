# 숭실대 학사 공지사항 가지고 오기 
import requests
from bs4 import BeautifulSoup
import re

count = 0 # 진행중인거 파밍한거 
num = 2 # 2페이지  ~ 5 페이지 
status_list = []
t_list = []
l_list = []
ele_list = []

url = "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%ED%95%99%EC%82%AC&keyword"
url2 = "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/page/{}/?f&category=%ED%95%99%EC%82%AC&keyword".format(num) # 2번째 페이지 
myheaders = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"}

res = requests.get(url , headers=myheaders)
res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")
# 일단 테스트로 1페이지만 

notilist = soup.find("ul" , attrs = {"class" : "notice-lists"}).find_all("li")


for li in notilist:
    listname = li["class"]
    if listname == "notice_head":
        print("여기는 헤드입니다")
    else:
        status = li.select_one(".notice_col2")
        if status.span == None:
            status_list.append("None")
            pass
        else:
            status_list.append(status.span.string)
# print(status_list)
# string 과 get_text()는 약간 다름 전자는 span에 후자는 a태크에 씀 

for a in notilist:
    notice = a.select_one(".notice_col3")
    if notice.a == None:
        t_list.append("None1")
        l_list.append("None")
        pass
    else:
        title = notice.a.get_text()
        link = notice.a["href"]

        t_list.append(title)
        l_list.append(link)

# 필터적용 적용된거는 DB에 넣을거임 dic에 안넣음 보류 
for i in len(notilist):



            
