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
        