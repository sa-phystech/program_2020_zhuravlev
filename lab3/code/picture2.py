import pygame
from pygame.draw import *
import random
from random import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((2000, 800))


def house(k, x0, housecolor, windowtype, rooftype, roofcolor):
    polygon(screen, housecolor, [(x0, y0-40*k), (x0+40*k, y0-40*k),
                                 (x0+40*k, y0), (x0, y0)])
    window(k, windowtype, x0)
    roof(k, rooftype, x0, roofcolor)

def roof(k, a, x0, roofcolor):
    if (a==1):
        polygon(screen, roofcolor, [(x0, y0-40*k), (x0+40*k, y0-40*k), (x0+20*k, y0-60*k)])
    else: 
        polygon(screen, roofcolor,[(x0, y0-40*k), (x0+10*k, y0-60*k), (x0+30*k, y0-60*k), (x0+40*k, y0-40*k)])

def window(k, windowtype, x0):
    if (windowtype==1):
        polygon(screen, (183, 251, 227), [(x0+10*k, y0-30*k), (x0+30*k, y0-30*k),
                                          (x0+30*k, y0-10*k), (x0+10*k, y0-10*k)])
    elif (windowtype==2):
        circle(screen, (183, 251, 227), (x0+20*k, y0-20*k), 10*k)
    else:
        ellipse(screen, (183, 251, 227), [x0+10*k, y0-25*k, 20*k, 10*k])     

    
def tree(k, x0):
    polygon(screen, (94, 37, 0), [(x0+50*k, y0), (x0+55*k, y0),
                                  (x0+55*k, y0-40*k), (x0+50*k, y0-40*k)])
    circle(screen, (0, 255, 0), (x0+52*k, y0-40*k), 10*k)
    circle(screen, (0, 255, 0), (x0+48*k, y0-50*k), 10*k)
    circle(screen, (0, 255, 0), (x0+55*k, y0-50*k), 10*k)

def cloud(x, y):
    circle(screen, (255, 255, 255), (x+50, y+150), 50)
    circle(screen, (255, 255, 255), (x+100, y+100), 50)
    circle(screen, (255, 255, 255), (x, y+100), 50)
    circle(screen, (255, 255, 255), (x+125, y+150), 50)
    

def draw(k, x0, housecolor, windowtype, rooftype, roofcolor):
    house(k, x0, housecolor, windowtype, rooftype, roofcolor)
    tree(k, x0)
    
frames = []
x0 = 20
y0 = 700
x = 200
y=50
k1 = [0, 0, 0, 0, 0, 0]
rooftype = [0, 0, 0, 0, 0, 0]
windowtype = [0, 0, 0, 0, 0, 0]
roofcolor = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
housecolor = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range (0, 6, 1):
    k1[i] = int(input('Размер дома (от 1 до 8) '))
    windowtype[i] = randint(1, 3)
    rooftype[i] = randint(1, 2)
    for j in range(3):
        roofcolor[i][j] = randint(0,255)
        housecolor[i][j] = randint(0,255)
 

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    polygon(screen, (20, 193, 224), [(0, 0), (2000, 0), (2000, 1000), (0, 1000)])
    polygon(screen, (48, 140, 9), [(0, 500), (2000, 500), (2000, 1000), (0, 1000)])
    circle(screen, (255, 255, 0), (110, 120), 100)
    cloud(x+300, y)
    cloud(x+600, y+100)
    cloud(x+900, y-40)
    x = x + 1
    for i in range (0, 6, 1):
        draw(k1[i], x0, housecolor[i], windowtype[i], rooftype[i], roofcolor[i])
        x0 = x0 + 70*k1[i]
    x0 = 20



    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()