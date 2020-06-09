import pygame, sys, math
from pygame.locals import *
from random import randint
from time import sleep

pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('Helvetica', 50)
BLACK = (0,0,0)
WHITE = (255,255,255)
window = pygame.display.set_mode((820,520))
box = pygame.image.load(r'C:\Users\Matt\.atom\box.png')

# for x in range(8):
#     for y in range(5):
#         window.blit(box,(20+100*x,20+100*y))

ai1 = pygame.Rect(100,100,260,105)
ai2 = pygame.Rect(460,100,260,105)
ayumu1 = pygame.Rect(100,305,260,105)
ayumu2 = pygame.Rect(460,305,260,105)

def startScreen():
    window.fill(BLACK)
    window.blit(myFont.render("Ai:",False,WHITE),(210,100))
    window.blit(myFont.render("Level 1",False,WHITE),(165,150))
    window.blit(myFont.render("Ai:",False,WHITE),(570,100))
    window.blit(myFont.render("Level 2",False,WHITE),(525,150))
    window.blit(myFont.render("Ayumu:",False,WHITE),(165,305))
    window.blit(myFont.render("Your Pace",False,WHITE),(135,355))
    window.blit(myFont.render("Ayumu:",False,WHITE),(525,305))
    window.blit(myFont.render("Ayumu's Pace",False,WHITE),(460,350))
    pygame.draw.rect(window,WHITE,ai1,1)
    pygame.draw.rect(window,WHITE,ai2,1)
    pygame.draw.rect(window,WHITE,ayumu1,1)
    pygame.draw.rect(window,WHITE,ayumu2,1)

def aiOne():
    window.fill(BLACK)
    numbers = [1,2,3,4,5,6,7,8,9]
    numC = []
    numOrder = []
    for i in range(3):
        randN = randint(0,8-i)
        numOrder.append(numbers[randN])
        del numbers[randN]
        numOrder.sort()
    for x in range(8):
        for y in range(5):
            numC.append((x,y))
    numArr = [[0 for x in range(2)] for y in range(3)]
    for i in range(3):
        randNum = randint(0,8-i)
        randC = randint(0,39-i)
        numArr[i][0] = numOrder[i]
        numArr[i][1] = numC[randC]
        print(numC[randC])
        del numC[randC]
    for i in numC:
        x,y = i
        window.blit(box,(20+100*x,20+100*y))
    for i in range(3):
        x,y = numArr[i][1]
        window.blit(myFont.render(str(numArr[i][0]),False,WHITE),(50+100*x,30+100*y))

    count = 0
    x, y = numArr[count][1]
    rectangle = pygame.Rect(20+100*x,20+100*y,80,80)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rectangle.collidepoint(event.pos):
                    if count == 0:
                        for i in range(3):
                            x,y = numArr[i][1]
                            window.blit(box,(20+100*x,20+100*y))
                    count += 1
                    if count == 3:
                        return
                    x, y = numArr[count][1]
                    rectangle = pygame.Rect(20+100*x,20+100*y,80,80)
                else:
                    return
        pygame.display.update()

def aiTwo():
    stuff
def ayumuOne():
    stuff
def ayumuTwo():
    stuff
startScreen()
while True:
  for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
          if ai1.collidepoint(event.pos):
              aiOne()
              startScreen()
          elif ai2.collidepoint(event.pos):
              aiTwo()
              startScreen()
          elif ayumu1.collidepoint(event.pos):
              ayumuOne()
              startScreen()
          elif ayumu2.collidepoint(event.pos):
              ayumuTwo()
              startScreen()
  pygame.display.update()
