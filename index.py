import pygame
import pygame.surface
import random
import sys
from pygame.locals import *

# initialize pygame
pygame.init()
resolution = (800, 600)
screen = pygame.display.set_mode(resolution)

pygame.display.set_caption('PyPals')
icon = pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\turtle.png')
pygame.display.set_icon(icon)


font = pygame.font.Font('X:\\Files\\Programming\\Projects\\PyPals\\resources\\font\\Pixeltype.ttf', 50)
game_background = pygame.image.load('game_background.png')

fps_clock = pygame.time.Clock()
fps = 30
start_time = pygame.time.get_ticks()
start_of_game = True

#need to create classes and methods for creating characters DRY

class Player:
    def __init__(self, image, attack, x, y):
        self.image = image
        self.attack = attack
        self.x = x
        self.y = y
    
    def get_image(self):
        return self.image
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_attack(self):
        return self.attack

    def set_image(self, image_to_set):
        self.image = image_to_set

    def set_x(self, x_to_set):
        self.x = x_to_set

    def set_y(self, y_to_set):
        self.y = y_to_set

    def set_attack(self, attack_to_set):
        self.attack = attack_to_set

    def blit_player(self, x,y):
        screen.blit(self.image, (x,y))


# half the size of a player image
def image_resizer(image_to_half):
    original_width, original_height = image_to_half.get_size()
    new_width, new_height = original_width // 4, original_height // 4
    image_to_return = pygame.transform.scale(image_to_half, (new_width, new_height))
    return image_to_return

# player 1
playerImage1 = image_resizer(pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\toucan.png'))
player1X = 200; player1Y = 200
fireball_attack = pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\fireball\efecto_fuego_00011.png')
def player1(x,y):
    screen.blit(playerImage1, (x, y))

# player 2
playerImage2 = image_resizer(pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\turtle.png'))
player2X = 600; player2Y = 200
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
        pygame.display.update()

# start menu
def start_menu():
    # main_menu_image = pygame.image.load('') !!make main menu image
    global start_of_game
    while start_of_game:
        # screen.fill(main_menu_image, (0, 0)) 
        screen.fill((0, 255, 255)) #cyan for start
        draw_text('PyPals Ultra Deluxe Version 2017', font, (0,0,0), screen, 700, 20)
        draw_text('Press S to start!', font, (0,0,0), screen, 800, 800)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    start_of_game = False
        pygame.display.update()
        
# game loop
while True:

    if start_of_game:
        start_menu()

    for event in pygame.event.get(): # event handling loop

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
            if event.key == pygame.K_s:
                player2Y += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               pass
        


    screen.blit(game_background, (0,0))
    player1(player1X, player1Y)
    player2(player2X, player2Y)
    pygame.display.update()
    fps_clock.tick(fps)