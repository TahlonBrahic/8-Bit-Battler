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
game_background = pygame.image.load('resources/background/background.png')
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
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self, image, attack_image, x, y, direction, alive=True, velocity=0, health=100, jumping=False, attacking=False, gravity=10):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image, -1)
        self.attack_image, self.attack_rect = load_image(attack_image, -1)
        self.x = x
        self.y = y
        self.alive = alive
        self.velocity = velocity
        self.gravity = gravity
        self.health = health
        self.jumping = jumping
        self.attacking = attacking
        self.direction = direction

    def draw(self):
        return screen.blit(image_resizer(self.image), (self.x, self.y))

    def turn(self):
        self.image = pygame.transform.flip(self.image, True, False)

    # def move(self, input_direction):
    #     if input_direction:


    def jump(self): 
        if not self.jumping:
            self.jumping = True
            self.velocity = -10
            self.gravity = 10

    def attack(self):
        if not self.attacking:
            self.attacking = True
        if self.attacking:
            new_attack = Attack(self.attack_image, self)
            sprite_group.add(new_attack)

    def update(self):
        if self.jumping:
            self.y += self.velocity
            self.velocity += 1
            self.gravity -= 1

        if self.gravity <= 0:
            self.jumping = False
        
        if not self.direction:
            self.turn()


class Attack(pygame.sprite.Sprite):
    def __init__(self, image, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.player = player
        self.x = player.x
        self.y = player.y
        self.rect = self.image.get_rect()

    def flip_image(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        if player.direction == 'left':
            screen.blit(image_resizer(self.image), (self.x, self.y))
            self.x += 10
        if player.direction =='right':
            screen.blit(self.flip_image(image_resizer(self.image)), (self.x, self.y))
            self.x -= 10
        if self.x > 600 or self.x < 0:
            self.attacking = False
            sprite_group.remove(self)



# half the size of a player image
def image_resizer(image):
    return pygame.transform.scale(image, (200, 150))
    

# attack list
attack_image = 'X:\Files\Programming\Projects\PyPals\\resources\\test artwork\\attack.png'

# character image list
player2_image = 'X:\Files\Programming\Projects\PyPals\\resources\\test artwork\player1.png'
player1_image= 'X:\Files\Programming\Projects\PyPals\\resources\\test artwork\player2.png'

# player's
player1 = Player(player1_image, attack_image, 500, 380, 'right')
player2 = Player(player2_image, attack_image, 200, 380, 'left')

player_list = [player1, player2]
sprite_group = pygame.sprite.Group()
sprite_group.add(player_list)

# draw text to screen
def draw_text_centered(text, y, font=font, color=(0,0,0), surface=screen):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.centerx = screen.get_rect().centerx 
    textrect.y += y
    surface.blit(textobj, textrect)

def draw_player_health(x, player, font=font, color=(0,0,0), surface=screen):
    textobj = font.render(str(player.health), 1, color)
    textrect = textobj.get_rect()
    textrect.x += x
    textrect.y = 20
    surface.blit(textobj, textrect)


# pause menu
def pause_game():   
    paused = True  
    while paused:
        screen.fill((0,0,0))
        draw_text_centered('paused', 200, color=(255,255,255))

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
        draw_text_centered('PyPals Ultra Deluxe Version 2017', 20)
        draw_text_centered('Press S to start!', 140)
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
                if not player1.jumping:
                    player1.jump()
            if event.key == pygame.K_RCTRL:
                if not player2.jumping:
                    player2.jump()
            if event.key == pygame.K_f:
                player1.attack()
            if event.key == pygame.K_RSHIFT:
                player2.attack()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player1.x -= 10; player1.direction == 'left'
    if keys[pygame.K_RIGHT]: player1.x += 10; player1.direction == 'right'      
    if keys[pygame.K_a]: player2.x -= 10; player2.direction == 'left'
    if keys[pygame.K_d]: player2.x += 10; player2.direction == 'right'

    # horizontal bounding
    for player in player_list:
        if player.y < 380:
            player.y += player.gravity - 9
            player.gravity += 1
        if player.y >= 380:
            player.y = 380
            player.gravity = 1
        if player.x > 640:
            player.x = 640
        if player.x < -10:
            player.x = -10

    # player and bullet collision
    for sprite in sprite_group:
        collisions = pygame.sprite.spritecollide(sprite, sprite_group, False)
        if len(collisions) > 2:
            player.health -= 1

    screen.blit(game_background, (0,0))
    draw_text_centered('Fight!', 20)
    player1.draw() 
    player2.draw() 
    draw_player_health(200, player1)
    draw_player_health(550, player2)
    sprite_group.update()
    pygame.display.update()
    clock.tick(fps)