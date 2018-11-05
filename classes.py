import pygame
from pygame.locals import *
from constants import *

class Level:

    def __init__(self, file):
        self.file = file
        self.structure = 0

    # We creat a list of list (1 list for 1 row)
    def generate(self):
        with open(self.file, "r") as file:
            structure_level = []
            for row in file:
                row_level = []
                for sprite in row:
                    if sprite != '\n':
                        row_level.append(sprite)
                structure_level.append(row_level)
            self.structure = structure_level
    
    def print(self, window):
        wall = pygame.image.load(picture_wall).convert()
        start = pygame.image.load(picture_start).convert()
        finish = pygame.image.load(picture_finish).convert_alpha()

        num_row = 0
        for row in self.structure:
            num_case = 0
            for sprite in row:
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

        """pygame.init()"""
        window = pygame.display.set_mode((size_window, size_window))
        background = pygame.image.load(picture_background).convert()
        window.blit(background, (0,0))
                    
        # Text writting
        font = pygame.font.Font(None, 36)
        text1 = font.render("I'm the boss of this level !", 1, (255,255,255))
        text2 = font.render("Type this message our you will die :", 1, (255,255,255))
        text3 = font.render("\"" + essai + "\"", 1, (255,255,255))
        text4 = font.render("Wrong !", 1, (255,255,255))
        text5 = font.render("You survive !", 1, (255,255,255))
        text6 = font.render("Please press Enter !", 1, (255,255,255))

        user_input = []

        continuer = 1
        quit = 0

        window.blit(text1, (0,0))
        window.blit(text2, (0,50))    
        window.blit(text3, (0,80))
        pygame.display.flip()

        while quit == 0:

            while continuer:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = 0
                    else:
                        if event.type == KEYDOWN and event.key != K_RETURN:
                            user_input += event.unicode
                            #print(event.unicode)
                        if event.type == KEYDOWN and event.key == K_RETURN:
                            continuer = 0
                        
            user_input_convert = "".join(user_input)
            if user_input_convert == essai:
                window.blit(background, (0,0))
                window.blit(text5, (0,120))
                window.blit(text6, (0, 150))
                pygame.display.flip()
            else:
                window.blit(background, (0,0))              # FAIRE UN SYSTEM DE 3 VIES
                window.blit(text4, (0,50))
                pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_RETURN:
                        quit = 1 