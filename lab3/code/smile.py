import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 240, 0), (200, 200), 150)
circle(screen, (255, 0, 0), (150, 150), 20)
circle(screen, (255, 0, 0), (250, 150), 20)
circle(screen, (0, 0, 0), (150, 150), 10)
circle(screen, (0, 0, 0), (250, 150), 10)
rect(screen, (0, 0, 0), (120, 250, 150, 20))
polygon(screen, (0, 0, 0), [(100,100), (180,140),
                            (180,150), (100,110)])
polygon(screen, (0, 0, 0), [(300,100), (220,140),
                            (220,150), (300,110)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()