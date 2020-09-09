import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/wlsdu/Desktop/대학/jlpt/jlpt단어장/word_test.csv")

def printBoundary() :
    for i in range(70) :
        print('-', end='')
    print()

def printWord(word, nSpace) :
    d = len(word) - 2
    w = d*2
    print(word+' '*(nSpace-w), end='')

def printOneLine(l) :
    printWord(l[0], 5)
    printWord(l[1], 7)
    printWord(l[2], 0)
    print()

def printNum(i) :
    if i < 9 :
        print('0' + str(i+1), end=' ')
    else :
        print(i+1, end=' ')
        
def test(df) :
    while (True) :
        print('날짜 선택 : 0')
        print('EXIT : 1')
        l = input("Select a mode >> ")
        if l == '1' :
            return
        elif l == '0' :
            while True :
                m = input("날짜를 선택해주세요 >> ")
                if m != '' :
                    m = int(m)
                    r = len(df)%30
                    if r != 0 :
                        limit = len(df)//30 + 1
                    else :
                        limit = len(df)//30
                    if m < 1 or m > limit :
                        print(str(limit)+'일차까지 있습니다')
                    else :
                        break
            print(str(m)+'일차를 선택하셨습니다.')
            if m == limit and r != 0 :
                m = (m-1)*30
                df2 = df.iloc[m:m+r, :]
            else :
                m = (m-1)*30
                df2 = df.iloc[m:m+30, :]
            while True :
                df2 = df2.sample(frac=1).reset_index(drop=True)
                print()
                print('뜻 보기 : 0')
                print('히라가나 보기 : 1')
                print('한자 보기 : 2')
                print('한자, 히라가나 보기 : 3')
                print('단어 데이터 셋 보기 : 4')
                print('뒤로 가기 : 5')
                print('EXIT : 6')
                n = input("Select a mode >> ")
                print()
                if n == '6' :
                    return
                elif n == '0' :
                    i = 0
                    while i<len(df2) :
                        print(i+1, end=' ')
                        print(df2.iloc[i,2])
                        c = input()
                        if c == '' :
                            i += 1
                elif n == '1' :
                    i = 0
                    while i<len(df2) :
                        print(i+1, end=' ')
                        print(df2.iloc[i,1])
                        c = input()
                        if c == '' :
                            i += 1
                elif n == '2' :
                    i = 0
                    while i<len(df2) :
                        print(i+1, end=' ')
                        print(df2.iloc[i, 0])
                        c = input()
                        if c == '' :
                            i += 1
                elif n == '3' :
                    i = 0
                    while i<len(df2) :
                        printNum(i)
                        if df2.iloc[i,0] == df2.iloc[i,1] :
                            print(df2.iloc[i,0], end='')
                        else :
                            printWord(df2.iloc[i,0], 5) # 줄 띄움 없음
                            printWord(df2.iloc[i,1], 7)
                        c = input() # 여기서 ENTER누르면 줄 띄워짐
                        if c == '' :
                            i += 1
                elif n == '4' :
                    i = 0
                    while i<len(df2) :
                        printNum(i)
                        printOneLine(df2.iloc[i].values.tolist())
                        i += 1
                    printBoundary()
                    while True :
                        o = input('예문 볼 번호 선택(뒤로가기 : -1, 단어 보기 : 0) >> ')
                        printBoundary()
                        if o == '0' :
                            i = 0
                            while i<len(df2) :
                                print(i+1, df2.iloc[i,0], df2.iloc[i,1], df2.iloc[i,2])
                                i += 1                            
                        if o == '-1' :
                            break
                        j = 1
                        while j <= 30 :
                            if str(j) == o :
                                p = 1
                                for k in range(10) :
                                    if k%2 == 0 :
                                        print(p,' ', sep = '', end = '')
                                        print(df2.iloc[j-1,k+3])
                                        p += 1
                                    else :
                                        print(' ' + df2.iloc[j-1,k+3])
                                break
                            j += 1
                        printBoundary()
                elif n == '5' :
                    break
                else :
                    continue
test(df)
