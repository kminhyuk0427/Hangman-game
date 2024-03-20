word='man' #정답
word=word.upper() #정답 대분자 변환
print(word)

word_show="_"*len(word)#단어의 글자 수만큼 밑줄
print(word_show)
try_num=0 #시도횟수
ok_list=[] #정답리스트
no_list=[] #오답리스트
while True:
    ans=input().upper()#단어에 포함될 것 같은 알파벳을 하나씩 말함
    print(ans)
    result=word.find(ans)#find는 word변수 안에 ans값이 몇번째에 있는지 (없으면 -1)
    print(result)
    if result == -1: #없음
        print("오답")
        try_num+=1#시도횟수 +1
        no_list.append(ans) #오답리스트에 추가
    else: #있음
        print('정답')
        ok_list.append(ans) #정답리스트에 추가
        for i in range(len(word)): #정답 글자 수 만큼 반복
            if word[i]==ans: #ans가 word n번째에 있으면
                word_show= word_show[:i] + ans    + word_show[i+1:]
                         # as(word_show) + D(ans) + fg(word_show)
        print(word_show)
    # 그림이 먼저 완성되면 출제자가 이김(a)
    if try_num==7 : break
    # 단어가 먼저 완성되면 단어를 맞힌 사람이 이김(b)
    if word_show.find('_')==-1:break
    