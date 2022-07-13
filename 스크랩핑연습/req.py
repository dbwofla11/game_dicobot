import requests
res = requests.get("http://www.google.com")
print("응답코드 :" , res.status_code) # 200 이면 정상 

# 오류처리 get
if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드 %s ]" , res.status_code )

res.raise_for_status() # 웹 스크랩핑 진행 
print("웹 스크랩핑을 진행합니다.") # 일단 get이 되면 스크랩핑이 된다 한다.

# 구글의 프론트 파일 불러오기 불러온 것을 새로운 파일로 만들어줌 (배포판으로 가지고 옴)
with open("mygoogle.html" , 'w' , encoding="utf8") as f :
    f.write(res.text)


