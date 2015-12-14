import webbrowser
import os, sys, random
import pygame, pygame.image
from pygame.locals import *
from pymsgbox import *

Hand0 = os.path.join('images', 'Hand0.png')
Hand1 = os.path.join('images', 'Hand1.png')
Hand2 = os.path.join('images', 'Hand2.png')

def Main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 800), HWSURFACE | DOUBLEBUF)
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))

    turn = 0
    xLeftPos = 10
    yLeftPos = 10
    xRightPos = 200
    yRightPos = 10
    MyLeft = pygame.image.load(Hand0)
    MyLeft_Pos = MyLeft.get_rect()
    MyLeft_Pos.top = yLeftPos
    MyLeft_Pos.left = xLeftPos
    MyRight = pygame.image.load(Hand0)
    MyRight_Pos = MyLeft.get_rect()
    MyRight_Pos.top = yRightPos
    MyRight_Pos.left = xRightPos

    xLeftPos2 = 10
    yLeftPos2 = 1000
    xRightPos2 = 200
    yRightPos2 = 1000
    MyLeft2 = pygame.image.load(Hand0)
    MyLeft_Pos2 = MyLeft2.get_rect()
    MyLeft_Pos2.top = yLeftPos2
    MyLeft_Pos2.left = xLeftPos2
    MyRight2 = pygame.image.load(Hand0)
    MyRight_Pos2 = MyLeft2.get_rect()
    MyRight_Pos2.top = yRightPos2
    MyRight_Pos2.left = xRightPos2

    screen.blit(background, (0, 0))
    screen.blit(MyLeft, MyLeft_Pos)
    screen.blit(MyRight, MyRight_Pos)
    screen.blit(MyLeft2, MyLeft_Pos2)
    screen.blit(MyRight2, MyRight_Pos2)
    pygame.display.flip()

    while True:
        pygame.event.pump()

        keyinput = pygame.key.get_pressed()
        if keyinput[K_ESCAPE] or pygame.event.peek(QUIT):
            break

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if turn == 0:
                    if event.key == K_q:
                        MyLeft = pygame.image.load(Hand0)
                    if event.key == K_w:
                        MyLeft = pygame.image.load(Hand1)
                    if event.key == K_e:
                        MyLeft = pygame.image.load(Hand2)

                    if event.key == K_a:
                        MyRight = pygame.image.load(Hand0)
                    if event.key == K_s:
                        MyRight = pygame.image.load(Hand1)
                    if event.key == K_d:
                        MyRight = pygame.image.load(Hand2)
                elif turn == 2:
                    if event.key == K_1:
                        yLeftPos = 50
                        yRightPos = 10
                    if event.key == K_2:
                        yLeftPos = 10
                        yRightPos = 50

                elif turn == 4:
                    print('End')
                    alert(text='승리', title='결과', button='확인')
                    turn = 5

                if event.key == K_r:
                    turn = 0
                    MyLeft = pygame.image.load(Hand0)
                    MyRight = pygame.image.load(Hand0)
                    xLeftPos = 10
                    yLeftPos = 10
                    xRightPos = 200
                    yRightPos = 10
                    yLeftPos2 = 1000
                    yRightPos2 = 1000
                    xLeftPos2 = 10
                    xRightPos2 = 200
                if event.key == K_t:
                    turn += 1


        if turn == 1:
            turn = 2
            yLeftPos2 = 300
            yRightPos2 = 300
            xLeftPos2 = 10
            xRightPos2 = 200
            ran = random.randint(0, 2)
            if ran == 0:
                MyLeft2 = pygame.image.load(Hand0)
            elif ran == 1:
                MyLeft2 = pygame.image.load(Hand1)
            elif ran == 2:
                MyLeft2 = pygame.image.load(Hand2)
            ran = random.randint(0, 2)
            if ran == 0:
                MyRight2 = pygame.image.load(Hand0)
            elif ran == 1:
                MyRight2 = pygame.image.load(Hand1)
            elif ran == 2:
                MyRight2 = pygame.image.load(Hand2)
        elif turn == 3:
            turn = 4
            ran = random.randint(0, 1)
            if ran == 0:
                yLeftPos2 = 300
                yRightPos2 = 250
            elif ran == 1:
                yLeftPos2 = 250
                yRightPos2 = 300

        MyLeft_Pos.top = yLeftPos
        MyLeft_Pos.left = xLeftPos
        MyRight_Pos.top = yRightPos
        MyRight_Pos.left = xRightPos

        MyLeft_Pos2.top = yLeftPos2
        MyLeft_Pos2.left = xLeftPos2
        MyRight_Pos2.top = yRightPos2
        MyRight_Pos2.left = xRightPos2

        screen.blit(background, (0, 0))
        screen.blit(MyLeft, MyLeft_Pos)
        screen.blit(MyRight, MyRight_Pos)
        screen.blit(MyLeft2, MyLeft_Pos2)
        screen.blit(MyRight2, MyRight_Pos2)
        pygame.display.flip()

# if __name__ == '__main__':
Main()
