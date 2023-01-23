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
font = pygame.font.Font('X:\\Files\\Programming\\Projects\\PyPals\\resources\\font\\Pixeltype.ttf', 50)
game_active = True
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

# draw text to screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

# pause menu
def pause_game():
    
    paused = True
    
    while paused:
        screen.fill((0,0,0))
        draw_text('paused', font, (255,255,255), screen, 1000, 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

        


# game loop
while game_active:

    screen.fill((255, 255, 255))
    clock.tick(60)

    for event in pygame.event.get():

        # quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # pause game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_game()

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