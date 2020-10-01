import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1500, 2000))

x=150
y=150
x0=0
y0=0
pi=3.14

def mouth(i):
    if (i % 2 ==0):
        y1=0
        polygon(screen, (0, 0, 0), [(x0+60, y0+225+y1), (x0+240, y0+225+y1),
                                  (x0+240,y0+250+y1), (x0+60, y0+250+y1)])
    else:
        y1=100
        arc(screen, (0, 0, 0), (75+x0, 175+y0+y1, 150, 100), pi, 2*pi, 3)

def eyebrows(i):
    if (i % 2 == 0):
        y1=0
        polygon(screen, (0, 0, 0), [(x0+40,y0+60+y1), (x0+125,y0+80+y1),
                                    (x0+125,y0+100+y1), (x0+40,y0+80+y1)])
        polygon(screen, (0, 0, 0), [(x0+260,y0+60+y1), (x0+175,y0+80+y1),
                                    (x0+175,y0+100+y1), (x0+260,y0+80+y1)])
    else:
        y1=100
        polygon(screen, (0, 0, 0), [(x0+40,y0+80+y1), (x0+125,y0+60+y1),
                                    (x0+125,y0+80+y1), (x0+40,y0+100+y1)])
        polygon(screen, (0, 0, 0), [(x0+260,y0+80+y1), (x0+175,y0+60+y1),
                                    (x0+175,y0+80+y1), (x0+260,y0+100+y1)])
def smile(i):
    if (i % 2 == 0):
        R1=255
        G1=0
        B1=0
        y1=0
    else:
        R1=0
        G1=240
        B1=0
        y1=100
    circle(screen, (255, 240, 0), (x+x0, y+y0+y1), 150)
    circle(screen, (R1, G1, B1), (x0+75, y0+120+y1), 20)
    circle(screen, (R1, G1, B1), (x0+225, y0+120+y1), 20)
    circle(screen, (0, 0, 0), (x0+75, y0+120+y1), 10)
    circle(screen, (0, 0, 0), (x0+225, y0+120+y1), 10)
    eyebrows(i)
    mouth(i)


for i in range(0,8,1):
    if (i % 4 == 0) and (i !=0 ):
        y0=y0+500
        x0=0
    smile(i)
    x0=x0+400
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()