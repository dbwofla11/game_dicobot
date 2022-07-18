import requests
from bs4 import BeautifulSoup

#2017 ~ 2021까지의 영화 순위를 가져오기 
for year in range(2017,2022):
    
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text , "lxml")
    images = soup.find_all("img" , attrs={"class" : "thumb_img"})

    for idx , image in enumerate(images): # enumerate함수는 리스트 요소마다 인덱스를 추가해서 private 하게 만드는 것 
        # print(image["src"])
        image_url = image["src"] # 이려면 이미지를 가져오는 것이 가능 
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1) , "wb") as f :
            f.write(image_res.content) # 이미지 만들기 .content
        
        if idx >= 4 : # 상위 5개 까지만 받기 
            break