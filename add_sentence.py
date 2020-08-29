import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/wlsdu/Desktop/대학/jlpt/jlpt단어장/word_test.csv")

import time

from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() 
# options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
options.add_argument('disable-gpu')    # GPU 사용 안함

driver = webdriver.Chrome('C:/Users/wlsdu/Desktop/대학/jlpt/jlpt단어장/chromedriver_win32/chromedriver', options=options) 

def at_most_5(n) :
    if n > 5 :
        return 5
    return n

# 진짜 완성본
for a in range(len(df)) :
    url = 'https://ja.dict.naver.com/#/search?query='
    word = df.iloc[a, 0]
    url = url + word + '&range=example'
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    letters_japanese = soup.select('div#searchPage_example > div.component_example > div.row > div.origin.is-audible > span')
    letters_korean = soup.select('div#searchPage_example > div.component_example > div.row > div.translate > p')
    
    korean_text = []
    for i in range(len(letters_korean)) :
        korean_text.append(letters_korean[i].text)
    
    print( int( len(letters_japanese)/2) )
    japanese_text = []
    for i in range(int( len(letters_japanese)/2) ) :
        japanese_text.append(letters_japanese[i*2].text)
    
    korean_text_revised = []
    for k in range(len(korean_text)) :
        bf = ''
        i=0
        l = len(korean_text[k])
        while i < l :
            if korean_text[k][i] == '\n' or korean_text[k][i] == '\t' :
                j=i+1
                while j < l :
                    if korean_text[k][j] != '\n' and korean_text[k][j] != '\t' : # 옳바른 글자일경우 bf에 추가
                        bf = bf + korean_text[k][j]
                        i=j+1
                        break
                    j+=1 # \n \t 일경우 j+=1
                if not(j<l) :
                    break
            elif korean_text[k][i] != '\n' and korean_text[k][i] != '\t' :
                bf = bf + korean_text[k][i]
                i+=1
        korean_text_revised.append(bf)
    
    japanese_text_revised = []
    for k in range(len(japanese_text)) :
        print(k)
        bf = ''
        i=0
        l = len(japanese_text[k])
        while i < l :
            if japanese_text[k][i] == '\n' or japanese_text[k][i] == '\t' :
                j=i+1
                while j < l :
                    if japanese_text[k][j] != '\n' and japanese_text[k][j] != '\t' : # 옳바른 글자일경우 bf에 추가
                        bf = bf + japanese_text[k][j]
                        i=j+1
                        break
                    j+=1 # \n \t 일경우 j+=1
                if not(j<l) :
                    break
            elif japanese_text[k][i] != '\n' and japanese_text[k][i] != '\t' :
                bf = bf + japanese_text[k][i]
                i+=1
        japanese_text_revised.append(bf)
    i = 0
    
    len1 = at_most_5( len(japanese_text) )
    len2 = at_most_5( len(korean_text) )
    
    while i < len1 :
        df.iloc[a,3+i*2] = japanese_text_revised[i]
        i+=1
    i = 0
    while i < len2 :
        df.iloc[a,4+i*2] = korean_text_revised[i]
        i+=1
        
df.to_csv('C:/Users/wlsdu/Desktop/대학/jlpt/jlpt단어장/jlpt_word.csv', index = False)
# revise
