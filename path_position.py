#! /usr/bin/env python3
# coding: utf-8

import os

import pygame                # import the pygame library and this module
from pygame.locals import *
pygame.init()                # initialize the pygame library

from labyrinth_position import LabyrinthList # import lists that represent the game background

os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")

class Objects:
        def __init__(self):
                # load the picture of the needle, make the background
                # of the picture transparent and paste the picture
                self.needle_picture = pygame.image.load("needle.png").convert()
                self.needle_picture.set_colorkey((255, 255, 255))
                WINDOW.blit(self.needle_picture, needle_position)

                # load the picture of the ether, make the background
                # of the picture transparent and paste the picture
                self.ether_picture = pygame.image.load("ether.png").convert()
                self.ether_picture.set_colorkey((255, 255, 255))
                WINDOW.blit(self.ether_picture, ether_position)

                # load the picture of the plastic tube, make the background
                # of the picture transparent and paste the picture
                self.plastic_tube_picture = pygame.image.load("plastic_tube.png").convert()
                self.plastic_tube_picture.set_colorkey((255, 255, 255))
                WINDOW.blit(self.plastic_tube_picture, plastic_tube_position)

                self.line_list = [LINE_1, LINE_2, LINE_3, LINE_4, LINE_5, LINE_6, LINE_7, LINE_8,
                     LINE_9, LINE_10, LINE_11, LINE_12, LINE_13]
                self.path_position_of_random_line = []

        def random_position(self):
                """Class that determines a random line and a random number in this line"""
                random_line = choice(line_list) # determines a random line
                # add in path_position_of_random_line the path coordinates of the random list
                for i, elt in enumerate(random_line):
                        if elt == "6":
                                index_random_line = self.line_list.index(random_line)
                                self.path_position_of_random_line.append(((i * 40), (index_random_line + 1) * 40))
                # determines a random coordinates
                random_location = choice(self.path_position_of_random_line)
                return random_location

        def needle_random_position():
                # creating variables with random coordinates for each objects
                needle_position = random_position()
                return needle_position
        
        def ether_random_position():
                # creating variables with random coordinates for each objects
                ether_position = random_position()
                return ether_position
        
        def plastic_tube_random_position():
                # creating variables with random coordinates for each objects
                plastic_tube_position = random_position()
                return plastic_tube_position

        #def new_needle_position():
                #needle_position = random_position()
                #return needle_position
        
        #def new_ether_position():
                #ether_position = random_position()
                #return ether_position
                        
        #def new_plastic_tube_position():
                #plastic_tube_position = random_position()
                #return plastic_tube_position

        def recall_function_random_position():
                # while the objects overlap, we determine a new random coordinates
                while needle_position == ether_position or ether_position == plastic_tube_position \
                        or plastic_tube_position == needle_position:
                        needle_position()
                        ether_position()
                        plastic_tube_position()      
                        
                # while the objects overlap the characters, we determine a new random coordinates
                while needle_position == (0, 520) or ether_position == (0, 520) or plastic_tube_position == (0, 520):
                        needle_position()
                        ether_position()
                        plastic_tube_position()
                        
def main():
    Objet()

if __name__ == "__main__":
    main()
