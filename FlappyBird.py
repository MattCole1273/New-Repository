import pygame, sys, math
from pygame.locals import *
from random import randint
from time import sleep

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((480,640))
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
PIPEGREEN = (0,128,0)
RED = (255,0,0)
myFont = pygame.font.SysFont('Helvetica', 75)
window.fill(BLUE)
pygame.draw.rect(window,GREEN,(0,565,480,75))
pygame.display.flip()
clock = pygame.time.Clock()



class bird:
    def __init__(self,rect):
        self.rect = rect
        self.fall = True
        self.jumpLength = 0
    def draw(self):
        if self.fall == True:
            pygame.draw.rect(window, BLUE,(190,self.rect.top,50,1))
            if self.rect.bottom < 565:
                self.rect.move_ip(0,1)
        if self.fall == False:
            if self.rect.bottom != 565:
                pygame.draw.rect(window, BLUE,(190,self.rect.bottom,50,1))
            self.rect.move_ip(0,-1)
            self.jumpLength -= 1
            if self.jumpLength == 0:
                self.fall = True
        pygame.draw.rect(window,RED,self.rect)
                
    def click(self):
        self.fall = False
        self.jumpLength = 75

class pipe:
    def __init__(self,height,start):
        self.rectTop = pygame.Rect(start,0,75,height)
        self.rectBottom = pygame.Rect(start,height+150,75,415-height)
    def draw(self):
        pygame.draw.rect(window,BLUE,(self.rectTop.right,0,1,self.rectTop.height))
        pygame.draw.rect(window,BLUE,(self.rectBottom.right,self.rectBottom.top,1,self.rectBottom.height))
        self.rectTop.move_ip(-1,0)
        self.rectBottom.move_ip(-1,0)
        if self.rectTop.right == 0:
            newHeight = randint(100,315)
            self.rectTop.left = 480
            self.rectTop.height = newHeight
            self.rectTop.top = 0
            self.rectBottom.left = 480
            self.rectBottom.top = newHeight + 150
            self.rectBottom.height = 415 - newHeight
        pygame.draw.rect(window,PIPEGREEN,self.rectTop)
        pygame.draw.rect(window,PIPEGREEN,self.rectBottom)
        
b = bird(pygame.Rect(190,340,50,40))
pipeOne = pipe(randint(100,315),480)
pipeTwo = pipe(randint(100,315),755)
count = 0
pipeCount = 0
window.blit(myFont.render(str(pipeCount),False,BLACK),(230,565))
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            b.click()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if count % 10 == 0:
        b.draw()
    if count % 15 == 0:
        pipeOne.draw()
        pipeTwo.draw()
        if pipeOne.rectTop.right == 190 or pipeTwo.rectTop.right == 190:
            pipeCount += 1
            pygame.draw.rect(window,GREEN,(0,565,480,75))
            window.blit(myFont.render(str(pipeCount),False,BLACK),(230,565))
    pygame.display.update()
    count += 1
    if (pipeOne.rectTop.left < 240 and pipeOne.rectTop.right > 190 and (b.rect.top < pipeOne.rectTop.bottom or b.rect.bottom > pipeOne.rectBottom.top)) or \
       (pipeTwo.rectTop.left < 240 and pipeTwo.rectTop.right > 190 and (b.rect.top < pipeTwo.rectTop.bottom or b.rect.bottom > pipeTwo.rectBottom.top)):
        window.blit(myFont.render('Game Over',False,BLACK),(90,0))
        pygame.display.update()
        b = bird(pygame.Rect(190,340,50,40))
        pipeOne = pipe(randint(100,315),480)
        pipeTwo = pipe(randint(100,315),755)
        count = 0
        pipeCount = 0
        gameOver = True
        sleep(.5)
        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    window.fill(BLUE)
                    pygame.draw.rect(window,GREEN,(0,565,480,75))
                    window.blit(myFont.render(str(pipeCount),False,BLACK),(230,565))
                    pygame.display.update()
                    gameOver = False
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    
