import pygame, sys, math
from time import sleep
from pygame.locals import *
from random import randint

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
ORANGE = (255,128,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((900,900))
window.fill(BLACK)
myBigFont = pygame.font.SysFont('Helvetica', 100)
myFont = pygame.font.SysFont('Helvetica', 30)

class Player:
    def __init__(self, name):
        self.name = name
        self.block = True
        self.counter = True
        self.opponent = True
        self.own = True
        self.die = randint(1,6)
        self.blockRect = pygame.Rect(0,100,450,500)
        self.counterRect = pygame.Rect(450,100,900,500)
        self.opponentRect = pygame.Rect(0,500,450,900)
        self.ownRect = pygame.Rect(450,500,900,900)

    def reroll(self):
        self.die = randint(1,6)

p1 = Player("Player 1")
p2 = Player("Player 2")

def intro(currentP, nextP):
    window.fill(BLACK)
    window.blit(myFont.render(currentP.name + ': ' + str(currentP.die),False,WHITE),(0,0))
    window.blit(myFont.render(nextP.name + ': ' + str(nextP.die),False,WHITE),(0,40))
    window.blit(myBigFont.render(current.name + "'s Turn",False,WHITE),(150,350))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                choose(currentp, nextp)
                return
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

def choose(currentP, nextP)
    window.fill(BLACK)
    window.blit(myFont.render(currentP.name + ': ' + str(currentP.die),False,WHITE),(0,0))
    window.blit(myFont.render(p2.name + ': ' + str(nextP.die),False,WHITE),(0,40))
    if currentP.block == True:
        pygame.draw.rect(window,RED,currentP.blockRect)
        window.blit(myBigFont.render("BLOCK",False,BLACK),(100,250))
    if currentP.counter == True:
        pygame.draw.rect(window,RED,currentP.counterRect)
        window.blit(myBigFont.render("COUNTER",False,BLACK),(500,250))
    if currentP.opponent == True:
        pygame.draw.rect(window,RED,currentP.opponentRect)
        window.blit(myBigFont.render("OPPONENT",False,BLACK),(100,650))
    if currentP.own == True:
        pygame.draw.rect(window,RED,currentP.ownRect)
        window.blit(myBigFont.render("OWN",False,BLACK),(550,650))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if counter == True and currentP.collidepoint(event.pos):

            if event.type == QUIT:
                pygame.quit()
                sys.exit()



while True:
    window.fill(BLACK)
    window.blit(myBigFont.render(p1.name + ': ' + str(p1.die),False,WHITE),(250,300))
    window.blit(myBigFont.render(p2.name + ': ' + str(p2.die),False,WHITE),(250,400))
    window.blit(myFont.render("Press Mouse Button",False,WHITE),(325,510))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            intro(p1, p2)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()




#Move die results to caption
#Change rect sizes
