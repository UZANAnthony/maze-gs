import pygame
from pygame.locals import *

from constants import *
from classes import *

essai = "test"

pygame.init()
window = pygame.display.set_mode((size_window, size_window))
background = pygame.image.load(picture_background).convert()
window.blit(background, (0,0))
            
# Text writting
font = pygame.font.Font(None, 36)
text1 = font.render("I'm the boss of this level !", 1, (255,255,255))
text2 = font.render("Type this message our you will die :", 1, (255,255,255))
text3 = font.render("\"" + essai + "\"", 1, (255,255,255))

continuer = 1

while continuer:

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    window.blit(text1, (0,0))
    window.blit(text2, (0,50))
    window.blit(text3, (0,80))
    pygame.display.flip()

pygame.quit()