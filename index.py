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

# player 1
playerImage1 = pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\toucan.png')
player1X = 800
player1Y = 200
fireball_attack = pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\fireball\efecto_fuego_00011.png')

# player 2
playerImage2 = pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\turtle.png')
player2X = 200
player2Y = 200

def player1(x,y):
    screen.blit(playerImage1, (x, y))

def player2(x,y):
    screen.blit(playerImage2, (x,y))

# game loop
while True:

    screen.fill((100, 100, 100))
    
    for event in pygame.event.get():

        # quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # settings menu
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                continue


        # player1 movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1X -= 10
            if event.key == pygame.K_RIGHT:
                player1X += 10
            if event.key == pygame.K_UP:
                player1Y -= 10
            if event.key == pygame.K_DOWN:
                player1Y += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               pass
        
        # player1 attack
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                screen.blit(fireball_attack, (100, 100))

        # player2 movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player2X -= 10
            if event.key == pygame.K_d:
                player2X += 10
            if event.key == pygame.K_w:
                player2Y -= 10
            if event.key == pygame.K_d:
                player2Y += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               pass
        


    
    player1(player1X, player1Y)
    player2(player2X, player2Y)
    pygame.display.update()