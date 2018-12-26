import pygame
from pygame.locals import *
from constants import *
from classes import *

pygame.init()
window = pygame.display.set_mode((size_window, size_window))
background = pygame.image.load(picture_background).convert()
window.blit(background, (0,0))
pygame.display.flip()  


arr = [1,2,3,4]

s = Stack()
print(not s.is_empty())

print(arr.index(2))