#! /usr/bin/env python3
# coding: utf-8

import os

from random import *             # import the random library
import pygame                # import the pygame library and this module
from pygame.locals import *
pygame.init()                # initialize the pygame library

from labyrinth_position import * # import lists that represent the game background

os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")

class Objects:
        def __init__(self):

                self.LINE_0 = ["0", "4", "4", "4", "4", "4", "4", "4", "4", "4", "2", "6", "3", "4", "1"]
                self.LINE_1 = ["5", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "5"]
                self.LINE_2 = ["5", "6", "0", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "5"]
                self.LINE_3 = ["5", "6", "5", "6", "6", "6", "6", "6", "6", "6", "5", "6", "6", "6", "5"]
                self.LINE_4 = ["5", "6", "5", "6", "0", "4", "4", "6", "4", "4", "4", "4", "1", "6", "5"]
                self.LINE_5 = ["5", "6", "5", "6", "5", "6", "6", "6", "6", "6", "6", "6", "5", "6", "5"]
                self.LINE_6 = ["5", "6", "5", "6", "5", "6", "0", "4", "4", "4", "4", "6", "5", "6", "5"]
                self.LINE_7 = ["5", "6", "5", "6", "5", "6", "5", "6", "6", "6", "6", "6", "6", "6", "5"]
                self.LINE_8 = ["5", "6", "5", "6", "5", "6", "5", "6", "5", "6", "4", "4", "4", "4", "5"]
                self.LINE_9 = ["5", "6", "6", "6", "5", "6", "5", "6", "5", "6", "6", "6", "6", "6", "5"]
                self.LINE_10 = ["5", "6", "5", "6", "5", "6", "5", "6", "5", "4", "4", "4", "4", "6", "5"]
                self.LINE_11 = ["5", "6", "5", "6", "5", "6", "5", "6", "5", "6", "5", "6", "6", "6", "5"]
                self.LINE_12 = ["3", "4", "4", "4", "4", "4", "2", "6", "5", "6", "3", "4", "4", "4", "5"]
                self.LINE_13 = ["6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "5"]
                self.LINE_14 = ["4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "2"]
                
                self.line_list = [self.LINE_1, self.LINE_2, self.LINE_3, self.LINE_4, self.LINE_5, self.LINE_6, self.LINE_7, self.LINE_8,
                     self.LINE_9, self.LINE_10, self.LINE_11, self.LINE_12, self.LINE_13]
                self.path_position_of_random_line = []
        
        def random_position(self):
                """Class that determines a random line and a random number in this line"""
                random_line = choice(self.line_list) # determines a random line
                # add in path_position_of_random_line the path coordinates of the random list
                for i, elt in enumerate(random_line):
                        if elt == "6":
                                index_random_line = self.line_list.index(random_line)
                                self.path_position_of_random_line.append(((i * 40), (index_random_line + 1) * 40))
                # determines a random coordinates
                random_location = choice(self.path_position_of_random_line)
                return random_location

        def needle_random_position(self):
                # creating variables with random coordinates for each objects
                needle_position = self.random_position()
                return needle_position

        def ether_random_position(self):
                # creating variables with random coordinates for each objects
                ether_position = self.random_position()
                return ether_position
        
        def plastic_tube_random_position(self):
                # creating variables with random coordinates for each objects
                plastic_tube_position = self.random_position()
                return plastic_tube_position

        def recall_function_random_position(self):
                # while the objects overlap, we determine a new random coordinates
                while self.needle_random_position() == self.ether_random_position() or self.ether_random_position() == self.plastic_tube_random_position() \
                        or self.plastic_tube_random_position() == self.needle_random_position():
                        self.needle_random_position()
                        self.ether_random_position()
                        self.plastic_tube_random_position()     
                        
                # while the objects overlap the characters, we determine a new random coordinates
                while self.needle_random_position() == (0, 520) or self.ether_random_position() == (0, 520) or self.plastic_tube_random_position() == (0, 520):
                        self.needle_random_position()
                        self.ether_random_position()
                        self.plastic_tube_random_position()

        def load_needle_picture(self):
                # load the picture of the needle, make the background
                # of the picture transparent and paste the picture
                self.needle_picture = pygame.image.load("needle.png").convert()
                self.needle_picture.set_colorkey((255, 255, 255))
                
        
        def load_ether_picture(self):
                # load the picture of the ether, make the background
                # of the picture transparent and paste the picture
                self.ether_picture = pygame.image.load("ether.png").convert()
                self.ether_picture.set_colorkey((255, 255, 255))
                

        def load_plastic_tube_picture(self):
                # load the picture of the plastic tube, make the background
                # of the picture transparent and paste the picture
                self.plastic_tube_picture = pygame.image.load("plastic_tube.png").convert()
                self.plastic_tube_picture.set_colorkey((255, 255, 255))
        
        def creation_window(self):
                # creates the window
                self.WINDOW = pygame.display.set_mode((600, 600))
                pygame.display.flip()
                return self.WINDOW
                
        
        def blit_needle_picture(self):
                if self.load_needle_picture() != None:
                        self.creation_window().blit(self.load_needle_picture(), self.needle_random_position())
                        pygame.display.flip()
        
        def blit_ether_picture(self):
                if self.load_ether_picture() != None:
                        self.creation_window().blit(self.load_ether_picture(), self.ether_random_position())
                        pygame.display.flip()

        def blit_plastic_tube_picture(self):
                if self.load_plastic_tube_picture() != None:
                        self.creation_window().blit(self.load_plastic_tube_picture(), self.plastic_tube_random_position())
                        pygame.display.flip()

testt = Objects()
testt.random_position()
testt.recall_function_random_position()
testt.needle_random_position()
testt.ether_random_position()
testt.plastic_tube_random_position()
testt.load_needle_picture()
testt.load_ether_picture()
testt.load_plastic_tube_picture()
testt.blit_needle_picture()
testt.blit_ether_picture()
testt.blit_plastic_tube_picture()
testt.creation_window()