import pygame

#1. 초기화
pygame.init()

#2. 창 옵션
size= [500,900]
screen=pygame.display.set_mode(size) #size를 display 함수를 이용하여 screen에 저장
title="HANGMAN"
pygame.display.set_caption(title) #창 이름

#3. 게임 기본설정
clock=pygame.time.Clock()
black=(0,0,0)
white=(255,255,255)

def tup_r(tup): #소수를 정수로 바꿔주는 함수  
    temp_list=[] 
    for a in tup: #tup에 들어간 죄표값들 돌림
        temp_list.append(round(a)) #하나씩 정수로 바꾸고 리스트에 추가
    return tuple(temp_list) #리스트를 튜플로 바꿔서 리턴

exit=False #나중에 종료할때 True로 바꿔줌

#4. 메인 이벤트
while not exit:
#4-1, FPS
    clock.tick(60)
#4-2, 입력 감지
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#이벤트가 퀵 이면
            exit=True
#4-3 입력, 시간에 따른 변화
#4-4 그리기
        screen.fill(white) #배경
        #A=왼쪽 밑 B=오른쪽 밑 C=A와B사이의 1/6 D=정사각형 AC거리와 같음 
        A=tup_r((0,size[1]*2/3)) #함수를 부르면서 튜플(0,600)을 값으로 줌   (2/3)은 삼분의 이
        B=(size[0],A[1]) #(size[0],size[1]*2/3) A의 y값과 B의 y값이 같음
        C=(size[0]/6,A[1]) #나누기6과 1/6이 같음
        D=(C[0],C[0])             #C의 x값과 모두 같음
        E=tup_r((size[0]/2,D[1])) #D와 y값이 같고 x값이 늘어남

        pygame.draw.line(screen, black,A,B,3)
        pygame.draw.line(screen, black,C,D,3)
        pygame.draw.line(screen, black,D,E,3)
#4-5 업데이트
        pygame.display.flip()

#5 게임 종료
pygame.QUIT()



