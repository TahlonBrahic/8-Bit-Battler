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

# player
playerImage = pygame.image.load('Projects\PyPals\\resources\icon\\toucan.png')
playerX = 800
playerY = 200

def player(x,y):
    screen.blit(playerImage, (x, y))

# game loop
while True:

    screen.fill((100, 100, 100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX -= 5
            if event.key == pygame.K_RIGHT:
                playerX += 5

    
    player(playerX, playerY)
    pygame.display.update()