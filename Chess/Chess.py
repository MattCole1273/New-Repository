import pygame, sys, math
from pygame.locals import *
from setup import *                              

def myRound(x, a, b):
    for i in range(a, b, -60):
        if (x > i):
            x = (i-b-1)/60
            break
    return x

def click(pos):
    test = False
    for p in pieceArr:
        if p.button.collidepoint(pos):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if(x>=400 and x<=880 and y>=120 and y<=600):
                            p.changeLoc(myRound(x, 880, 399), myRound(y, 600, 119))
                            return

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click(event.pos)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

