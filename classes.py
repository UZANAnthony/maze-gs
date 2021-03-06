import pygame
from pygame.locals import *
from constants import *



class Level:
    def __init__(self, file):
        self.file = file
        self.structure = 0

    # We creat a list of list (1 list for 1 row)
    def generate(self):
        with open(self.file, "r") as file:                              # We open the file
            structure_level = []                                        # Creation of the main array
            for row in file:                                            # We read the file line by line
                row_level = []                                          # Creation of a little array which represents a line
                for sprite in row:
                    if sprite != '\n':
                        row_level.append(sprite)
                structure_level.append(row_level)                       # We add the little array (the line) to the main array
            self.structure = structure_level                            # Matrix generated
    
    def print(self, window):
        wall = pygame.image.load(picture_wall).convert()
        start = pygame.image.load(picture_start).convert()
        finish = pygame.image.load(picture_finish).convert_alpha()

        num_row = 0
        for row in self.structure:                                      # Goes from line to line
            num_case = 0
            for sprite in row:                                          # Goes from character to character
                x = num_case * size_case
                y = num_row * size_case
                if sprite == 'w':                       # w = Wall
                    window.blit(wall, (x,y))
                elif sprite == 'f':                     # f = Finish
                    window.blit(finish, (x,y))
                elif sprite == 's':                     # s = Start
                    window.blit(start, (x,y))
                num_case += 1
            num_row += 1



class Player:
    def __init__(self, icon, level):
        self.icone = pygame.image.load(picture_player).convert_alpha()
        # Player's postion in case
        self.case_x = 0
        self.case_y = 0
        # Player's position in pixel
        self.x = 0
        self.y = 0
        self.level = level

    def move(self, direction):
        if direction == "right":
            if self.case_x < (nb_case_side - 1):
                if self.level.structure[self.case_y][self.case_x + 1] != 'w':
                    self.case_x += 1
                    self.x = self.case_x * size_case
        
        if direction == "left":
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'w':
                    self.case_x -= 1
                    self.x = self.case_x * size_case
        
        if direction == "up":
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'w':
                    self.case_y -= 1
                    self.y = self.case_y * size_case
        
        if direction == "down":
            if self.case_y < (nb_case_side - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'w':
                    self.case_y += 1
                    self.y = self.case_y * size_case



class Typing:
    def __init__(self, character_str):
        self.character_str = character_str
    
    def typing_boss(self):
        essai = self.character_str

        window = pygame.display.set_mode((size_window, size_window))
        background = pygame.image.load(picture_background).convert()
        input_background = pygame.image.load(picture_input).convert()
        window.blit(background, (0,0))

        continuer = 1
        quit = 0
        lives = 3
                    
        # Text writting
        font = pygame.font.Font(None, 36)
        text1 = font.render("I'm the boss of this level!", 1, (255,255,255))
        text2 = font.render("Type this to survive:", 1, (255,255,255))
        text3 = font.render("\"" + essai + "\"", 1, (255,255,255))
        text4 = font.render("Wrong!", 1, (255,255,255))
        text5 = font.render("You survive!", 1, (255,255,255))
        text6 = font.render("Please press Enter!", 1, (255,255,255))
        text7 = font.render(str(lives) + " lives remaining!", 1, (255,255,255))
        text8 = font.render("Press Enter to validate.", 1, (255,255,255))

        text1_rect = text1.get_rect(center=(450/2, 25))
        text2_rect = text2.get_rect(topleft=(0, 100))
        text3_rect = text3.get_rect(center=(450/2, 140))
        text4_rect = text4.get_rect(center=(450/2, 300))
        text5_rect = text5.get_rect(center=(450/2, 25))
        text6_rect = text6.get_rect(center=(450/2, 70))
        text7_rect = text7.get_rect(center=(450/2, 330))
        text8_rect = text8.get_rect(center=(450/2, 170))
        
        user_input = []

        window.blit(background, (0,0))
        window.blit(text1, text1_rect)
        window.blit(text2, text2_rect)    
        window.blit(text3, text3_rect)
        window.blit(text8, text8_rect)
        pygame.display.flip()

        while quit == 0:
            while lives > 0:
                while continuer:
                    
                    for event in pygame.event.get():
                        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                            quit = 1
                            lives = 0
                            continuer = 0
                        else:
                            if event.type == KEYDOWN and event.key != K_RETURN and event.key != K_BACKSPACE:        # Add the character in the array
                                user_input += event.unicode
                            if event.type == KEYDOWN and event.key ==  K_BACKSPACE:
                                user_input = user_input[:-1]                                                        # Remove the last letter of the string
                            if event.type == KEYDOWN and event.key == K_RETURN:
                                continuer = 0
                            
                            text_input = font.render("".join(user_input), 1, (255,255,255))                         # Display the user's input in real time
                            window.blit(input_background, (0,250))
                            window.blit(text_input, (0,250))
                            pygame.display.flip()
                            
                user_input_convert = "".join(user_input)            # Pre-processing of the user's input

                if user_input_convert == essai:                     # Check if the input is the String asked, if yes the player win                
                    window.blit(background, (0,0))
                    window.blit(text5, text5_rect)
                    window.blit(text6, text6_rect)
                    pygame.display.flip()
                    lives = 0
                else:                                               # If not ...
                    user_input = []
                    lives = lives - 1
                    if lives == 0:                                                                          # If the player has lost his three lives, he loses the game
                        text7 = font.render("You have lost!", 1, (255,255,255))
                        text7_rect = text7.get_rect(center=(450/2, 330))
                    else:                                                                                   # If he still has lives, he loses one 
                        if lives > 1:                                                                       # Customized diplay due to "life" and "lives"
                            text7 = font.render(str(lives) + " lives remaining!", 1, (255,255,255))
                        else:
                            text7 = font.render(str(lives) + " life remaining!", 1, (255,255,255))
                            text7_rect = text7.get_rect(center=(450/2, 330))
                        
                    window.blit(background, (0,0))
                    window.blit(text1, text1_rect)
                    window.blit(text2, text2_rect)    
                    window.blit(text3, text3_rect)
                    window.blit(text8, text8_rect)
                    window.blit(text4, text4_rect)
                    window.blit(text7, text7_rect)
                    pygame.display.flip()
                    
                    continuer = 1      
            
            for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_RETURN:
                        quit = 1 



class Solver:
    def __init__(self, grid):
        self.result = False
        self.maze = grid
        self.x = 0
        self.y = 0
    
    def search(self, x, y):
            if self.maze[x][y] == 'f':
                #print("finish at %d,%d" % (x,y))
                return True
            elif self.maze[x][y] == 'w':
                #print("wall at %d,%d" % (x,y))
                return False
            elif self.maze[x][y] == 'v':
                #print("visited at %d,%d" % (x,y))
                return False
            
            #print("visiting %d,%d" % (x,y))

            self.maze[x][y] = 'v'               # To mark the case visited

            if ((x < len(self.maze)-1 and self.search(x+1, y)) or (y > 0 and self.search(x, y-1)) or (x > 0 and self.search(x-1, y)) or (y < len(self.maze)-1 and self.search(x, y+1))):
                return True
            return False
