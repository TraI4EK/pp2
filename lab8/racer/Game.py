#Imports
import pygame, sys
from pygame.locals import *
import random, time


#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
COINS_NUM = 0
#background sound
back_sound = pygame.mixer.music
back_sound.load('a.mp3')
back_sound.play(-1)
back_sound.set_volume(0.1)
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)  
        if self.rect.left > 0:
              if pressed_keys[K_LEFT] and pressed_keys[K_LSHIFT]:
                  self.rect.move_ip(-20, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT] and pressed_keys[K_LSHIFT]:
                  self.rect.move_ip(20, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("coin.png"), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH -40), random.randint(0, SCREEN_HEIGHT - 150))
    #Contact method, to count amount of coins was colected
    def contact(self):
        global COINS
        COINS+=1
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(0,SCREEN_HEIGHT - 150))

    def move(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(50, SCREEN_WIDTH -40), random.randint(0,SCREEN_HEIGHT - 150))        

                    

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
bounties = pygame.sprite.Group()
bounties.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
COIN_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(INC_SPEED, 1000)
pygame.time.set_timer( COIN_SPAWN, random.randint(1000, 3000))

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5 
        if event.type == COIN_SPAWN and COINS_NUM <= 1:
            C1 = Coin()
            bounties.add(C1)
            all_sprites.add(C1)
            COINS_NUM += 1     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Scoreboards
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coins = font_small.render(str(COINS), True, GREEN)
    DISPLAYSURF.blit(coins, (360,10))
    
   
    

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
  
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        back_sound.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
                   
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
          
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    #killing sprites in bounties when car touches coins, 
    #and recreating it again, to make collecting effect 
       
    elif pygame.sprite.spritecollideany(P1, bounties):
        C1.contact()
        for entity in bounties:
            entity.kill()
            COINS_NUM -= 1
        
    pygame.display.update()
    FramePerSec.tick(FPS)   