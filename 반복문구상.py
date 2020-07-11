'''
df.iloc[0,0] = text.[0]
df.iloc[0,1] = text.[1]
df.iloc[0,2] = text.[2]

df.iloc[1,0] = text.[3]
df.iloc[1,1] = text.[4]
df.iloc[1,2] = text.[5]

df.iloc[2,0] = text.[6]
df.iloc[2,1] = text.[7]
df.iloc[2,2] = text.[8]

k=0
for i in range(720) :
    for j in range(3) :
        df.iloc[i,j] = text.[k]
        k+=1
'''
# ㄹㅇ 문교수님 참교수님

'''
kanji.append(letters[1].text)
kanji.append(letters[4].text)
kanji.append(letters[7].text)
kanji.append(letters[10].text)

for i in range(720) :
    kanji.append(letters[i*3+1].text)
'''

'''
for i in range(720) :
    for j in range(len(hiragana[i])) :
        if hiragana[i][j] == '\u3000' :
            hiragana[i] = hiragana[i][0:j]
'''
