import pygame
import pygame.surface
import random

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('PyPals')
clock = pygame.time.Clock()
# test_font = pygame.font.Font('X:\Files\Programming\Projects\PyPals\resources\font\Pixeltype.ttf', 50)
game_active = False
start_time = 0

# create game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()