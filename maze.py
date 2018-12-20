import pygame
from pygame.locals import *

from constants import *
from classes import *

# Initialization
pygame.init()
window = pygame.display.set_mode((size_window, size_window))
player_icon = pygame.image.load(picture_player).convert_alpha()
pygame.display.set_icon(player_icon)
pygame.display.set_caption(window_title)

# Loop
proceed = 1
while proceed:
    menu = pygame.image.load(picture_menu).convert()        # Load menu
    window.blit(menu, (0,0))

    pygame.display.flip()                                   # Refresh

    proceed_game = 1
    proceed_menu = 1

    while proceed_menu:
        
        pygame.time.Clock().tick(30)                        # Limit loop's speed

        for event in pygame.event.get():

            # Exit
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                proceed_menu = 0
                proceed_game = 0
                proceed = 0
                choice = 0
            
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    proceed_menu = 0
                    choice = "m1.txt"
                if event.key == K_F2:
                    choice = "m2.txt"

    # We check if the user select a level
    if choice != 0:
        background = pygame.image.load(picture_background).convert()        # Load background

        level = Level(choice)                                               # Generate level
        level.generate()
        level.print(window)

        player = Player("images/snake.png", level)                          # Player creation

    while proceed_game:
        
        # To go directly to the boss stage (comment to play the game)
       # level.structure[player.case_y][player.case_x] = 'f'
        
        pygame.time.Clock().tick(30)                        # Limit loop's speed

        for event in pygame.event.get():

            if event.type == QUIT:                          # If player quit the game                  
                proceed_game = 0
                proceed = 0

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:                   # Back to the menu
                    proceed_game = 0
            
                if event.key == K_RIGHT:
                    player.move("right")
                if event.key == K_LEFT:
                    player.move("left")
                if event.key == K_UP:
                    player.move("up")
                if event.key == K_DOWN:
                    player.move("down")
        
        # Print new position
        window.blit(background, (0,0))
        level.print(window)
        window.blit(player.icone, (player.x, player.y))
        pygame.display.flip()                                       # Update the full display Surface to the screen

        if level.structure[player.case_y][player.case_x] == 'f':    # If player finished the level
            #proceed_game = 0                                        # Back to the menu
            t1 = Typing("test")
            t1.typing_boss()
            proceed_game = 0
            





            
