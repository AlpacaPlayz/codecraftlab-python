import pygame
import random
from pygame.locals import *

class Player(pygame.sprite.Sprite):
##    def __init__(self):
##        super(Player, self).__init__()
##        self.surf = pygame.Surface((75, 75))
##        self.surf.fill((255, 255, 255))
##        self.rect = self.surf.get_rect()
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('nyancat').convert()
        self.image.set_colorkey((0, 255, 0), RLEACCEL)
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.bottom > 600:
            self.rect.bottom = 600

class Opponent(pygame.sprite.Sprite):
    #def __init__(self):
        #self.surf = pygame.Surface((20, 10))
        #self.surf.fill((255, 255, 255))
        #self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        #self.speed = random.randint(0, 2)

    def __init__(self):
        super(Opponent, self).__init__()
        self.image = pymange.image.load('').convert
        self.image.set_colorkey((255, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randit(820, 900), random.randit(0, 600))
    
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
 
#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

player = Player()


background = pygame.Surface(screen.get_size())
background.fill((0,0,0))
                                               
players = pygame.sprite.Group()

opponents = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(player)

ADDOPPONENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOPPONENT, 250)


#create main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
        #and if that key happens to be the escape key
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif(event.type == ADDOPPONENT):
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)

    screen.blit(background, (0,0))

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    opponents.update()
    #put rectangle on screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()

    if pygame.sprite.spritecollideany(player, opponents):
        player.kill()

    
#end pygame         
pygame.quit()
