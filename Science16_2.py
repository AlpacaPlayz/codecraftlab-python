import pygame
from time import sleep
import random
from pygame.locals import *
#import random, sys, time, pygame, sleep
#from pygame.locals import *


#pygame.mixer.init()
#pygame.mixer.music.load(open("\Users\Donna\Downloads\atone.wav", "r"))
#pygame.mixer.play()



class Player(pygame.sprite.Sprite):




    def __init__(self):


        super(Player, self).__init__()

        self.image = pygame.image.load('blue.png').convert()

        self.image.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.image.get_rect()

        self.rect.top = 400  # y

        self.rect.left = 60  # x

        self.sound = pygame.mixer.Sound("atone.wav")

        self.sound.set_volume(100)


        
    def play_sound(self):
        
        self.sound.play()

    def stop_sound(self):
        self.sound.stop
        
   
         



    def update(self, pressed_keys):

   

        if pressed_keys[K_LEFT]:
            pygame.mixer.stop()
            player.play_sound()
            self.rect.move_ip(-540, 0)
            sleep(.4)
            
            
        if pressed_keys[K_RIGHT]:
            pygame.mixer.stop()
            player.play_sound()
            sleep(.2)
            player.play_sound()
            self.rect.move_ip(540, 0)
            sleep(.4)
        
        if self.rect.left < 0:

            self.rect.left = 0

        if self.rect.top < 0:

            self.rect.top = 0

        if self.rect.right > 800:

            self.rect.right = 800
           
        if self.rect.bottom > 600:

            self.rect.bottom = 600



    


class Opponent(pygame.sprite.Sprite):


    def __init__(self):

        super(Opponent, self).__init__()
        
        self.image = pygame.image.load('red.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(

            center=(random.randint(0, 400), random.randint(0, 1)))
        
        self.speed = random.randint(1,1)
        self.sound = pygame.mixer.Sound("beep.wav")

        self.sound.set_volume(20)
        
    def play_sound(self):
        
        self.sound.play()

    def stop_sound(self):
        self.sound.stop

    def update(self, pressed_keys):

        #self.rect.move_ip(0, self.speed)
        #if self.rect.bottom > 600 :
          #self.kill()
         #self.rect.move_ip(0, self.speed)
        #self.rect.bottom = 600
        
        if pressed_keys[K_UP]:
            opponent.play_sound()
            self.rect.move_ip(0, self.speed)
            
            
            
        else:
            
            self.kill()
            
           


class Opponent2(pygame.sprite.Sprite):


    def __init__(self):

        super(Opponent2, self).__init__()
        
        self.image = pygame.image.load('red.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(

            center=(random.randint(400, 800), random.randint(0, 1))
            
        )
        self.speed = random.randint(1,1)

        self.sound = pygame.mixer.Sound("ping.wav")

        self.sound.set_volume(20)
        
    def play_sound(self):
        
        self.sound.play()

    def stop_sound(self):
        self.sound.stop()
        

    def update(self, pressed_keys):

        #self.rect.move_ip(0, self.speed)
        #if self.rect.bottom > 600 :
          #self.kill()
         #self.rect.move_ip(0, self.speed)
        #self.rect.bottom = 600

        if pressed_keys[K_DOWN]:
            opponent2.play_sound()
            self.rect.move_ip(0, self.speed)
        else:
            self.kill()
            opponent2.stop_sound()

            
            #sleep(.4)
            #center=(random.randint(267,534),random.randint(0,1))
            #sleep(.4)

        
            
        #if pressed_keys[K_RIGHT]:
            #sleep(.4)
            #self.rect.move_ip(123, 0)
            #sleep(.4)
            #self.rect.move_ip(0,0)


        



#initialize pygame

pygame.init()

#create screen


screen = pygame.display.set_mode((800, 600))

player = Player()

opponent = Opponent()
opponent2 =Opponent2()

        
asound = pygame.mixer.Sound("buzz.wav")

background = pygame.Surface(screen.get_size())

background.fill((0,0,0))

players = pygame.sprite.Group()

opponents = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(player)

ADDOPPONENT = pygame.USEREVENT + 1

pygame.time.set_timer(ADDOPPONENT, 1500)


#create main loop

running = True

while running:

    for event in pygame.event.get():

        

            
                
        #and if that key happens to be the escape key

            #if event.key == K_ESCAPE:

                #running = False

            if event.type == QUIT:

                running = False

        #elif(event.type == KEYDOWN & event.type == ADDOPPONENT):
                #new_opponent = Opponent()
                #opponents.add(new_opponent)
                #all_sprites.add(new_opponent)
                


            elif(event.type == ADDOPPONENT):

                new_opponent = Opponent()
                new_opponent2 = Opponent2()
            
                opponents.add(new_opponent)
                opponents.add(new_opponent2)
            
                all_sprites.add(new_opponent)
                all_sprites.add(new_opponent2)

    screen.blit(background, (0,0))

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    opponents.update(pressed_keys)
    
    for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
    pygame.display.flip()
    if pygame.sprite.spritecollideany(player, opponents):
        pygame.mixer.stop()
        player.kill()
        asound.play()

#end pygame         

pygame.quit()

    
