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
font = pygame.font.Font(None, 36)

# Loop
wrong_key = False    #To store if the user has entered a wrong key
proceed = 1
while proceed:
    menu = pygame.image.load(picture_menu).convert()        # Load menu                

    text1 = font.render("Press \"F1\" for level 1", 1, (255,255,255))
    text2 = font.render("Press \"F2\" for level 2", 1, (255,255,255))
    text3 = font.render("Wrong key!", 1, (255,255,255))
    
    text1_rect = text1.get_rect(center=(450/2, 250))
    text2_rect = text2.get_rect(center=(450/2, 280))
    text3_rect = text3.get_rect(center=(450/2, 330))

    window.blit(menu, (0,0))
    window.blit(text1, text1_rect)
    window.blit(text2, text2_rect)
    if wrong_key: window.blit(text3, text3_rect)           

    pygame.display.flip()                                   # Refresh

    proceed_game = 1
    proceed_menu = 1

    while proceed_menu:
        
        pygame.time.Clock().tick(30)                        # Limit loop's speed

        for event in pygame.event.get():

            choice = 0
            # Exit
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                proceed_menu = 0
                proceed_game = 0
                proceed = 0
                choice = 0
            
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    choice = "m1.txt"
                    boss = "Fire ball"
                if event.key == K_F2:
                    choice = "m2.txt"
                    boss = "Avada,Kedavra"
                if event.key == K_F3:
                    choice = "m3.txt"
                    boss = "cheat"
                else :
                    wrong_key = True
                proceed_menu = 0

    # We check if the user select a level
    if choice != 0:
        wrong_key = False # For deleting the message for the new game 

        background = pygame.image.load(picture_background).convert()        # Load background

        level = Level(choice)                                               # Generate level
        level.generate()
        level.print(window)

        player = Player("images/snake.png", level)                          # Player creation

        while proceed_game:
            
        # level.structure[player.case_y][player.case_x] = 'f'           # To go directly to the boss stage (comment to play the game)
            
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
                t = Typing(boss)
                t.typing_boss()
                proceed_game = 0            # Back to the menu
            





            
