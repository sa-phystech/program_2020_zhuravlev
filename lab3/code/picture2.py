import pygame
from pygame.draw import *
import random
from random import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((2000, 800))
polygon(screen, (20, 193, 224), [(0, 0), (2000, 0), (2000, 1000), (0, 1000)])
polygon(screen, (48, 140, 9), [(0, 500), (2000, 500), (2000, 1000), (0, 1000)])
circle(screen, (255, 255, 0), (110, 120), 100)

def house(k):
    polygon(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), [(x0, y0-40*k), (x0+40*k, y0-40*k),
                                                                         (x0+40*k, y0), (x0, y0)])

    polygon(screen, (183, 251, 227), [(x0+10*k, y0-30*k), (x0+30*k, y0-30*k),
                                      (x0+30*k, y0-10*k), (x0+10*k, y0-10*k)])

    polygon(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), [(x0, y0-40*k), (x0+40*k, y0-40*k), (x0+20*k, y0-60*k)])

def tree(k):
    polygon(screen, (94, 37, 0), [(x0+50*k, y0), (x0+55*k, y0),
                                  (x0+55*k, y0-40*k), (x0+50*k, y0-40*k)])
    circle(screen, (0, 255, 0), (x0+52*k, y0-40*k), 10*k)
    circle(screen, (0, 255, 0), (x0+48*k, y0-50*k), 10*k)
    circle(screen, (0, 255, 0), (x0+55*k, y0-50*k), 10*k)

def cloud():
    circle(screen, (255, 255, 255), (x0+20*k, 400-40*k), 10*k)
    circle(screen, (255, 255, 255), (x0+30*k, 400-50*k), 10*k)
    circle(screen, (255, 255, 255), (x0+10*k, 400-50*k), 10*k)
    circle(screen, (255, 255, 255), (x0+35*k, 400-40*k), 10*k)
    

def draw(k):
    house(k)
    tree(k)
    cloud()

x0=20
y0=700

for i in range (1,8,1):
    k=i
    draw(k)
    x0=x0+70*i
 

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()