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

#4-5 업데이트
        pygame.display.flip()

#5 게임 종료
pygame.QUIT()



