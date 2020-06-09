import pygame, sys, math
from time import sleep
from pygame.locals import *
from random import randint


BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((900,900))
window.fill(BLACK)
myBigFont = pygame.font.SysFont('Helvetica', 100)
window.blit(myBigFont.render('Choose Difficulty 1-9',False,WHITE),(50,400))
myFont = pygame.font.SysFont('Helvetica', 30)

def memory(boxCount, difficulty):
    window.fill(BLACK)
    step = 0
    x = []
    y = []
    for i in range(boxCount):
        same = True
        while same == True:
            same = False
            tempX = randint(0,8)*100
            tempY = randint(0,8)*100
            if len(x) != 0:
                for s in range(len(x)):
                    if x[s] == tempX and y[s] == tempY:
                        same = True
        x.append(tempX)
        y.append(tempY)
        pygame.draw.rect(window, WHITE,(x[i],y[i],100,100),1)
        window.blit(myFont.render(str(i + 1),False,WHITE),(x[i]+40,y[i]+30))
    pygame.display.update()
    sleep(5-difficulty/2)
    for i in range(boxCount):
        pygame.draw.rect(window, BLACK, (x[i]+10,y[i]+10,80,80))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                rectangle = pygame.Rect(x[step],y[step],100,100)
                if rectangle.collidepoint(event.pos):
                    window.blit(myFont.render(str(step + 1),False,WHITE),(x[step]+40,y[step]+30))
                    step = step + 1
                    if boxCount == step:
                        memory(boxCount + 1, difficulty)
                        return
                else:
                    for i in range(boxCount):
                        window.blit(myFont.render(str(i + 1),False,WHITE),(x[i]+40,y[i]+30))
                    pygame.display.update()
                    sleep(2)
                    return
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

while True:
    window.fill(BLACK)
    window.blit(myBigFont.render('Choose Difficulty 1-9',False,WHITE),(50,400))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                memory(2, 1)
            if event.key == pygame.K_2:
                memory(2, 2)
            if event.key == pygame.K_3:
                memory(2, 3)
            if event.key == pygame.K_4:
                memory(2, 4)
            if event.key == pygame.K_5:
                memory(2, 5)
            if event.key == pygame.K_6:
                memory(2, 6)
            if event.key == pygame.K_7:
                memory(2, 7)
            if event.key == pygame.K_8:
                memory(2, 8)
            if event.key == pygame.K_9:
                memory(2, 9)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
