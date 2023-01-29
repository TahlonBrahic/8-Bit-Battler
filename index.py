import pygame
import pygame.surface
import random
import os, sys
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
fps = 60
start_time = pygame.time.get_ticks()
start_of_game = True

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image:", name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Player:
    def __init__(self, image, attack, x, y, alive=True, velocity=0):
        self.image = image
        self.attack = attack
        self.x = x
        self.y = y
        self.alive = alive
        self.velocity = velocity
        self.gravity = 20
    
    def get_image(self):
        return self.image
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_attack(self):
        return self.attack
        
    def get_alive(self):
        return self.alive
    
    def get_velocity(self):
        return self.get_velocity

    def get_gravity(self):
        return self.gravity

    def set_image(self, image_to_set):
        self.image = image_to_set

    def set_x(self, x_to_set):
        self.x = x_to_set

    def set_y(self, y_to_set):
        self.y = y_to_set

    def set_attack(self, attack_to_set):
        self.attack = attack_to_set

    def set_alive(self, state):
        self.alive = state

    def blit_player(self):
        return screen.blit(self.image, (self.x, self.y))

    def player_surface(self):
        self.get_rect()

    def player_jump(self):
        self.y += 50
    
    def player_attack(self):
        return screen.blit(self.attack, (self.x, self.y))

# considering replacing with sprite
class PlayerNew(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprrite.Sprite.__init__(self, image)
        self.image, self.rect = load_image(image)
        self.x, self. y = (100,100)


# half the size of a player image
def image_resizer(image_to_half):
    original_width, original_height = image_to_half.get_size()
    new_width, new_height = original_width // 4, original_height // 4
    image_to_return = pygame.transform.scale(image_to_half, (new_width, new_height))
    return image_to_return

# attack list
fireball_attack = pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\fireball\efecto_fuego_00011.png').convert()

# character image list
toucan = image_resizer(pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\toucan.png')).convert()
turtle = image_resizer(pygame.image.load('X:\Files\Programming\Projects\PyPals\\resources\icon\\turtle.png')).convert()

# player's
player1 = Player(toucan, fireball_attack, 200, 200)
player2 = Player(turtle, fireball_attack, 600, 200)
player_list = [player1, player2]

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

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_game()
            if event.key == pygame.K_LEFT:
                player1.x -= 10
            if event.key == pygame.K_RIGHT:
                player1.x += 10
            if event.key == pygame.K_UP:
                player1.jump() 
            if event.key == pygame.K_DOWN:
                player1.y += 10    
            if event.key == pygame.K_f:
                player1.player_attack()
            if event.key == pygame.K_a:
                player2.x -= 10
            if event.key == pygame.K_d:
                player2.x += 10
            if event.key == pygame.K_w:
                player2.jump()
            if event.key == pygame.K_s:
                player2.y += 10

        # gravity
        for player in player_list:
            if player.y < 290:
                player.y += player.gravity
            if player.y > 290:
                player.y = 290

    screen.blit(game_background, (0,0))
    player1.blit_player()
    player2.blit_player()
    pygame.display.update()
    fps_clock.tick(fps)