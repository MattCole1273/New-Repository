import pygame, sys, math
from pygame.locals import *



WIDTH = 1280
HEIGHT = 720
BLACK = (0,0,0)
WHITE = (255,255,255)
blackPawn = pygame.image.load('Black Pawn.png')
blackKing = pygame.image.load('Black King.png')
blackRook = pygame.image.load('Black Rook.png')
blackQueen = pygame.image.load('Black Queen.png')
blackBishop = pygame.image.load('Black Bishop.png')
blackKnight = pygame.image.load('Black Knight.png')
whitePawn = pygame.image.load('White Pawn.png')
whiteKing = pygame.image.load('White King.png')
whiteRook = pygame.image.load('White Rook.png')
whiteQueen = pygame.image.load('White Queen.png')
whiteBishop = pygame.image.load('White Bishop.png')
whiteKnight = pygame.image.load('White Knight.png')

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill((WHITE))

pieceArr = []

class piece:
    def __init__(self, locX, locY, pieceType):
        self.locX = locX
        self.locY = locY
        self.pieceType = pieceType
        pieceArr.append(self)
        self.button = window.blit(pieceType, (400+locX*60, 120+locY*60))

    def changeLoc(self, x, y):
        if(self.locX != x or self.locY != y):
            if (self.locX + self.locY) % 2 == 1:
                pygame.draw.rect(window, BLACK, (400+(self.locX*60),120+(self.locY*60),60,60))
            else:
                pygame.draw.rect(window, WHITE, (400+(self.locX*60),120+(self.locY*60),60,60))
            for p in pieceArr:
                if(p.locX == x and p.locY == y):
                    p.delete()
            self.locX = x
            self.locY = y
            self.button = window.blit(self.pieceType, (400+self.locX*60, 120+self.locY*60))
            pygame.draw.rect(window, BLACK, (400,120,480,480), 1)

    def delete(self):
        del pieceArr[pieceArr.index(self)]

pygame.draw.rect(window, BLACK, (400,120,480,480), 1)

for y in range(8):
    for x in range(8):
        if (x + y) % 2 == 1:
            pygame.draw.rect(window, BLACK, (400+(x*60),120+(y*60),60,60))
        else:
            pygame.draw.rect(window, WHITE, (400+(x*60),120+(y*60),60,60))

pygame.draw.rect(window, BLACK, (400,120,480,480), 1)

bp1 = piece(0, 1, blackPawn)
bp2 = piece(1, 1, blackPawn)
bp3 = piece(2, 1, blackPawn)
bp4 = piece(3, 1, blackPawn)
bp5 = piece(4, 1, blackPawn)
bp6 = piece(5, 1, blackPawn)
bp7 = piece(6, 1, blackPawn)
bp8 = piece(7, 1, blackPawn)
br1 = piece(0, 0, blackRook)
bk1 = piece(1, 0, blackKnight)
bb1 = piece(2, 0, blackBishop)
bq = piece(3, 0, blackQueen)
bk = piece(4, 0, blackKing)
bb2 = piece(5, 0, blackBishop)
bk2 = piece(6, 0, blackKnight)
br2 = piece(7, 0, blackRook)
wp1 = piece(0, 6, whitePawn)
wp2 = piece(1, 6, whitePawn)
wp3 = piece(2, 6, whitePawn)
wp4 = piece(3, 6, whitePawn)
wp5 = piece(4, 6, whitePawn)
wp6 = piece(5, 6, whitePawn)
wp7 = piece(6, 6, whitePawn)
wp8 = piece(7, 6, whitePawn)
wr1 = piece(0, 7, whiteRook)
wk1 = piece(1, 7, whiteKnight)
wb1 = piece(2, 7, whiteBishop)
wq = piece(3, 7, whiteQueen)
wk = piece(4, 7, whiteKing)
wb2 = piece(5, 7, whiteBishop)
wk2 = piece(6, 7, whiteKnight)
wr2 = piece(7, 7, whiteRook)
