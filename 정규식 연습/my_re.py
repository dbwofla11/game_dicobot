#정규식 
# ==> 그냥 사회에서 쓰이는 일반적인 규칙 
#ex) 주민등록번호 , 이메일 주소 , 차량번호 같은거 

#웹 스크랩핑에 필요한 기본 정규식 알아보기 

import re # 정규식 라이브러리 
p = re.compile("ca.e")  # 필터(정규식 정의) # 안에 원하는 형태를 적용 아래에 정리 
# . : 하나의 문자를 의미 (cafe , case , care) caffe (x)
# ^ : 문자열의 시작 (de^) 얘는 de로 시작 하면 다 됨 
# $ : 문자열의 끝   (se$) case , base | face (x)

#print(m.group()) # 매치되지 않으면 에러가 생김 

def print_match(m):
    if m:
        print("m.group() :", m.group()) # 일치하는 문자열을 반환함
        print("m.string : "  , m.string) # 입력받은 문자열을 반환 
        print("m.start() : " , m.start()) # 일치하는 문자열의 시작 index
        print("m.end()" , m.end()) #  일치하는 문자열의 끝 index 
        print("m.span()" , m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음 ")

# m = p.match("case") # match : 주어진 문자열의 처음부터 일치하는지 
# m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인 

lst = p.findall("good care") # findall : 일치하는 모든것을 리스트로 변환  
print(lst)
# print_match(m)
