import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/wlsdu/Desktop/대학/jlpt/jlpt단어장/jlpt_word.csv")

import time

from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() 
#options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
options.add_argument('disable-gpu')    # GPU 사용 안함

driver = webdriver.Chrome('C:/Users/wlsdu/Desktop/대학/jlpt/jlpt단어장/chromedriver_win32/chromedriver', options=options)

df.fillna(0, inplace = True)
beg = 0
for i in range(len(df)) :
    if df.iloc[i,3] == 0 :
        beg = i
        break
end = len(df)

for i in range(beg, end) :
    url = 'https://ja.dict.naver.com/#/search?query='
    word = df.iloc[i, 0]
    url = url + word + '&range=example'
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    letters = soup.select('div#searchPage_example > div.component_example > div.row > div > p')
    for j in range(10) :
        df.iloc[i, j+3] = letters[j].text

driver.quit()

for i in range(beg, end) :
    for j in range(0,9,2) :
        k=0
        while not(df.iloc[i,j+4][k] != '\n' and df.iloc[i,j+4][k] != '\t')  :
            k+=1
        df.iloc[i,j+4] = df.iloc[i,j+4][k:]

for i in range(beg, end) :
    for j in range(0,9,2) :
        k=0
        while not(df.iloc[i,j+4][k] == '\n' or df.iloc[i,j+4][k] == '\t')  :
            k+=1
        df.iloc[i,j+4] = df.iloc[i,j+4][:k]

df.to_csv('C:/Users/wlsdu/Desktop/대학/jlpt/jlpt단어장/jlpt_word.csv', index = False)
