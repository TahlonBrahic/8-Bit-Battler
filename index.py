import pygame
import pygame.surface
import random

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('PyPals')
icon = pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\turtle.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
pygame.font.Font('X:\\Files\\Programming\\Projects\\PyPals\\resources\\font\\Pixeltype.ttf', 50)
game_active = False
start_time = 0

# player
playerImage1 = pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\toucan.png')
playerX = 800
playerY = 200
fireball_attack = pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\fireball\efecto_fuego_00011.png')

def player1(x,y):
    screen.blit(playerImage1, (x, y))

def player2(x,y):
    screen.blit(playerImage, (x,y))

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
                playerX -= 10
            if event.key == pygame.K_RIGHT:
                playerX += 10
            if event.key == pygame.K_UP:
                playerY -= 10
            if event.key == pygame.K_DOWN:
                playerY += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               pass
        
        # player attack
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                screen.blit(fireball_attack, (100, 100))


    
    player1(playerX, playerY)
    pygame.display.update()