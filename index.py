import pygame
import pygame.surface
import random

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('PyPals')
icon = pygame.image.load('Projects\PyPals\\resources\icon\\turtle.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
pygame.font.Font('X:\Files\Programming\Projects\PyPals\\resources\\font\Pixeltype.ttf', 50)
game_active = False
start_time = 0

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()