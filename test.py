import pygame
from pygame.locals import *
from constants import *

pygame.init()
window = pygame.display.set_mode((size_window, size_window))
background = pygame.image.load(picture_background).convert()
window.blit(background, (0,0))
pygame.display.flip()  

user_input = []
quit = 0

while quit == 0:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key != K_BACKSPACE: 
            user_input += event.unicode
            print(user_input)
        if event.type == KEYDOWN and event.key == K_BACKSPACE:
            user_input = user_input[:-1]
            print(user_input)
        if event.type == QUIT:
            quit = 1