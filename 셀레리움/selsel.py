#셀레리움 스크랩핑 (프레임웤)
from selenium import webdriver
import os 
import charset_normalizer as AutoChrome # 자동정지 방지 
import shutil

def selenium_test():
    chrome_ver = AutoChrome.get_chrome_version().split('.')[0]
    path = os.path.join(os.getcwd(),chrome_ver)
    path = os.path.join(path,'chromedriver.exe')
    print(path)
    URL = 'https://www.google.co.kr/'
    driver = webdriver.Chrome(str(path))
    driver.get(url=URL)
    
    while(True):
    	pass


selenium_test()
