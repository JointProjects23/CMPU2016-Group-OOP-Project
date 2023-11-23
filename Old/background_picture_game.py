import pygame
import sys
import os

pygame.init()

# initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((626, 435))
bg = pygame.image.load(os.path.join("./", "background.png"))
pygame.mouse.set_visible(1)
pygame.display.set_caption('The Poirot Mystery')
while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
