import pygame
from pygame.locals import *

pygame.init()

print("hello world")

pygame.mixer.music.load("/Users/gomjoey/Development/StarWars3.wav");
pygame.mixer.music.play(0);
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)