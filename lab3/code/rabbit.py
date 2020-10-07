import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen=pygame.display.set_mode((1000,1000))

def head(surface, x, y, height, width, color):
    circle(surface, color, (x + width//2, y + 55*height//100), width//3)

def eyes(surface, x, y, height, width):
    circle(surface, (0, 0, 255), (x + 4*width//10, y + 55*height//100 - width//5), 25)
    circle(surface, (0, 0, 255), (x + 6*width//10, y + 55*height//100- width//5), 25)
    circle(surface, (0, 0, 0), (x + 4*width//10, y + 55*height//100 - width//5), 10)
    circle(surface, (0, 0, 0), (x + 6*width//10, y + 55*height//100 - width//5), 10)
    circle(surface, (255, 187, 221), (x + width//2, y + 55*height//100), 10)

def mouth(surface, x, y, height, width):
    ellipse(surface, (255, 0, 0), (x + 4*width//10, y + 55*height//100 + width//5, 2*width//10, 3*height//100))

def ears(surface, x, y, height, width, color):
    ellipse(surface, color, (x + 15*width//100 , y, 15*width//100, 45*height//100))
    ellipse(surface, color, (x + 70*width//100, y, 15*width//100, 45*height//100))
    ellipse(surface, (255, 233, 233), (x + 725*width//1000, y + 10*height//100 , 10*width//100, 25*height//100))
    ellipse(surface, (255, 233, 233), (x + 175*width//1000, y + 10*height//100 , 10*width//100, 25*height//100))

def body(surface, x, y, height, width, color):
    ellipse(surface, color, (x + 17*width//100, y + 55*height//100 + width//3, 2*width//3, 50*height//100))

def paws(surface, x, y, height, width, color):
    circle(surface, color, (x + 17*width//100, y + height + width//3), width//6)
    circle(surface, color, (x + 83*width//100, y + height + width//3), width//6)

def rabbit(surface, x, y, height, width, color):
    ears(surface, x, y, height, width, color)
    head(surface, x, y, height, width, color)
    body(surface, x, y, height, width, color)
    paws(surface, x, y, height, width, color)
    eyes(surface, x, y, height, width)
    mouth(surface, x, y, height, width)


s = screen
x = 300
y = 200
height = 500 
width = 300 
color = (192, 192, 192)

rabbit(s, x, y, height, width, color)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()