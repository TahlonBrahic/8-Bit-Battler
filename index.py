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
game_background = pygame.image.load('background.png')
game_background = pygame.transform.scale(game_background, (800, 600))

clock = pygame.time.Clock()
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
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self, image, attack, x, y, alive=True, velocity=10, health=100, jumping=False, gravity=-1):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image, -1)
        self.attack, self.attack_image = load_image(attack_image, -1)
        self.x = x
        self.y = y
        self.alive = alive
        self.velocity = velocity
        self.gravity = gravity
        self.health = health
        self.jumping = jumping

    def _attack(self):
        pass

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

    def set_health(self, health_to_set):
        self.health = health_to_set

    def draw(self):
        return screen.blit(image_resizer(self.image), (self.x, self.y))

    def surface(self):
        return 

    def jump(self):
        player.jumping = True
        if player.jumping:
           self.y -= 200
   
    def attack(self):
        screen.blit(image_resizer(self.attack), (self.x, self.y))




# half the size of a player image
def image_resizer(image):
    return pygame.transform.scale(image, (200, 150))
    

# attack list
attack_image = 'X:\Files\Programming\Projects\PyPals\\resources\\test artwork\\attack.png'

# character image list
player2_image = 'X:\Files\Programming\Projects\PyPals\\resources\\test artwork\player1.png'
player1_image= 'X:\Files\Programming\Projects\PyPals\\resources\\test artwork\player2.png'



# player's
player1 = Player(player1_image, attack_image, 500, 380)
player2 = Player(player2_image, attack_image, 200, 380)

player_list = [player1, player2]

# draw text to screen
def draw_text_centered(text, font, color, surface, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.centerx = screen.get_rect().centerx 
    textrect.y += y
    surface.blit(textobj, textrect)


# pause menu
def pause_game():   
    paused = True  
    while paused:
        screen.fill((0,0,0))
        draw_text_centered('paused', font, (255,255,255), screen, 200)

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
        draw_text_centered('PyPals Ultra Deluxe Version 2017', font, (0,0,0), screen, 20)
        draw_text_centered('Press S to start!', font, (0,0,0), screen, 140)
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
            if event.key == pygame.K_SPACE:
                if player1.jumping == False:
                    player1.jump()
            if event.key == pygame.K_RCTRL:
                player2.jump()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player1.x -= 10
    if keys[pygame.K_RIGHT]: player1.x += 10      
    if keys[pygame.K_f]: player1.attack()   
    if keys[pygame.K_a]: player2.x -= 10
    if keys[pygame.K_d]: player2.x += 10
    if keys[pygame.K_0]: player2.attack()


    # bounding
    for player in player_list:
        if player.y < 380:
            player.y += player.gravity
            player.gravity += 1
        if player.y >= 380:
            player.y = 380
            player.gravity = 1
        if player.x > 640:
            player.x = 640
        if player.x < 0:
            player.x = 0


    screen.blit(game_background, (0,0))
    player1.draw()
    player2.draw()
    pygame.display.update()
    clock.tick(fps)