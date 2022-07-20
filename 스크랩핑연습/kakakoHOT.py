# 숭실대 BEST10 공지사항 가지고 오기 
import requests
from bs4 import BeautifulSoup 

url = "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&category=%EC%BD%94%EB%A1%9C%EB%82%9819%EA%B4%80%EB%A0%A8%EC%86%8C%EC%8B%9D&slug=%ED%95%99%EC%83%9D%EC%84%9C%EB%B9%84%EC%8A%A4%ED%8C%80-%EC%BD%94%EB%A1%9C%EB%82%9819-%ED%99%95%EC%A7%84-%EC%9E%90%EA%B0%80-%EC%8B%A0%EA%B3%A0-%EB%B0%A9%EB%B2%95-%EC%95%88%EB%82%B4&keyword"
myheaders = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"}

res = requests.get(url , headers=myheaders)
res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")

def best_notice():
    rank = []
    for i in range(1,11):
        save = soup.find("li" , attrs={"title" : str(i)})
        rank.append(save)
    return [rank[0] , rank[1] , rank[2] , rank[3] , rank[4] , rank[5] , rank[6] , rank[7] , rank[8] , rank[9]]
    

# print("지금부터 시작 ~!!!!!!!!")
# print(rank)

# print("이건 for문 확인용인것이 에요유 ~~~~~~~~~~~~~~~")
# for i in range(10):
#     print(rank[i].a.get_text() , rank[i].a["href"])
# print(rank[0].a.get_text() , rank[0].a["href"] )
