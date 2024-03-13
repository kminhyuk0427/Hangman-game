# a가 영ㅇ어단어 1개 생성
word='man'
word=word.upper()
print(word)
#단어의 글자 수만큼 밑줄
word_show="_"*len(word)
print(word_show)
try_num=0
ok_list=[]
no_list=[]
while True:
    #B가 단어에 포함될 것 같은 알파벳을 하나씩 말함
    ans=input().upper()
    print(ans)
    #알파벳이 단어에 포함되면 밑줄에 알파벳을 채워놓고
    #포함되지 않는다면 사람을 1획씩 그림
    result=word.find(ans)
    print(result)
    if result == -1: #없음
        print("오답")
        try_num+=1
        no_list.append(ans)
    else: #있음
        print('정답')
        ok_list.append(ans)
        for i in range(len(word)):
            if word[i]==ans:
                word_show=word_show[:i]+ans+word_show[i+1:]
                #asdfg -> asDfg -> as + D + fg
        print(word_show)
    # 그림이 먼저 완성되면 출제자가 이김(a)
    if try_num==7 : break
    # 단어가 먼저 완성되면 단어를 맞힌 사람이 이김(b)
    if word_show.find('_')==-1:break



