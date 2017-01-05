#!/usr/bin/env python
import pygame
pygame.init()
song = pygame.mixer.Sound('thesong.ogg')
clock = pygame.time.Clock()
song.play()
while True:
    clock.tick(60)
pygame.quit()
