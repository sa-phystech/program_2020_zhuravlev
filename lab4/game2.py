import pygame
from pygame.draw import *
from random import randint
pygame.init()
import math

scoretable=open('player.txt', 'r')
n1=scoretable.readline()
hp1=scoretable.readline()
scoretable.close()
n=int(n1)
hp=int(hp1)


FPS = 30
screen = pygame.display.set_mode((1500, 1000))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x = 0
xm = 0
ym = 0
x1 = 0
xm1 = 0
ym1 = 0


def healthpoints(hp):
    heart_surf = pygame.image.load('heart.png')
    heart_rect = [heart_surf.get_rect(topleft=(20, 200)), heart_surf.get_rect(topleft=(20, 400)), heart_surf.get_rect(topleft=(20, 600))] 
    if (hp > 0):
        for i in range (hp):
            screen.blit(heart_surf, heart_rect[i])
        


def new_ball():
    global x, y, r, xm, ym
    color = COLORS[randint(0, 5)]
    if x == 0:
        x = randint(300,1000)
        y = randint(300,800)
        r = randint(50,100)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)
        xm = randint(-20, 20)
        ym = randint(-20, 20)
    else:
        circle(screen, color, (x, y), r)
        x = x + xm
        y = y + ym
    if ( x + r > 1500) or ( x - r < 200):
        xm = xm*(-1)
    if ( y + r > 900) or ( y - r < 0):
        ym = ym*(-1)

def new_ellipse(tickcount):
    global x1, y1, a, b, color1
    if x1 == 0:
        x1 = randint(500, 1000)
        y1 = randint(100, 800)
        a = randint(50, 200)
        b = randint(50, 200)
        color1 = COLORS[randint(0, 5)]
        ellipse(screen, color1, (x1 - a//2, y1 - b//2, a, b))
    elif (tickcount % 15 == 0):    
        x1 = randint(500, 1000)
        y1 = randint(100, 800)
        a = randint(50, 200)
        b = randint(50, 200)
        color1 = COLORS[randint(0, 5)]
    ellipse(screen, color1, (x1 - a//2, y1 - b//2, a, b)) 

tickcount = 0

def countstrike(n):
    f = pygame.font.Font('comic.ttf', int(50))
    s = str(n)
    text = f.render('score' +':  ' + s, 0, (255, 255, 255))
    screen.blit(text, (10, 910))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    if (hp > 0):
        rect(screen, (255, 255, 255), (200, 0, 1300, 900), 1) 
        healthpoints(hp)
        new_ball()
        new_ellipse(tickcount)
        countstrike(n)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                scoretable=open('player.txt', 'w')
                scoretable.write(str(n) + '\n')
                scoretable.write(str(hp) + '\n')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                xc = event.pos[0]
                yc = event.pos[1]   
                if (((xc - x)**2 + (yc - y)**2) < r**2):
                    n = n + 1
                    x = 0
                elif ((xc < x1 + a//2) and (xc > x1 - a//2)) and ((yc < y1 + b//2) and (yc > y1 - b//2)):
                    n = n + 2
                    x1 = 0
                else:
                    hp = hp - 1
        tickcount = tickcount + 1
    else:
        scoretable=open('player.txt', 'w')
        scoretable.write('0' + '\n')
        scoretable.write('3' + '\n')
        scoretable.close()
        screen.fill((0, 0, 0))
        rect(screen, (255, 255, 255), (200, 0, 1300, 900), 1)
        countstrike(n)
        f = pygame.font.Font('comic.ttf', int(65))
        text = f.render('Game over', 0, (255, 255, 255))
        screen.blit(text, (650, 450))
    pygame.display.update()
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

