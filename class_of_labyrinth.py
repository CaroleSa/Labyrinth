#! /usr/bin/env python3
# coding: UTF-8 je garde

import os

import random
# import the pygame library and this module
import pygame
from pygame.locals import *
# initialize the pygame library
pygame.init()

class Labyrinth:

    def __init__(self):
        self.LABYRINTH_LIST = [
        [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 6, 3, 4, 1],
        [5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5],
        [5, 6, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
        [5, 6, 5, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 5],
        [5, 6, 5, 6, 0, 4, 4, 6, 4, 4, 4, 4, 1, 6, 5],
        [5, 6, 5, 6, 5, 6, 6, 6, 6, 6, 6, 6, 5, 6, 5],
        [5, 6, 5, 6, 5, 6, 0, 4, 4, 4, 4, 6, 5, 6, 5],
        [5, 6, 5, 6, 5, 6, 5, 6, 6, 6, 6, 6, 6, 6, 5],
        [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4, 4, 4, 4, 5],
        [5, 6, 6, 6, 5, 6, 5, 6, 5, 6, 6, 6, 6, 6, 5],
        [5, 6, 5, 6, 5, 6, 5, 6, 5, 4, 4, 4, 4, 6, 5],
        [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 6, 6, 5],
        [3, 4, 4, 4, 4, 4, 2, 6, 5, 6, 3, 4, 4, 4, 5],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2]]

        # creates the window    
        self.WINDOW = pygame.display.set_mode((600, 600))

        self.ground_picture = pygame.image.load("ground.png").convert_alpha()
        self.wall_top_left_picture = pygame.image.load("top_left.png").convert_alpha()
        self.wall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        self.wall_low_right_picture = pygame.image.load("low_right.png").convert_alpha()
        self.wall_low_left_picture = pygame.image.load("low_left.png").convert_alpha()
        self.wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
        self.wall_vertical_picture = pygame.image.load("vertical.png").convert_alpha()
                
        self.PICTURE_LIST = [self.wall_top_left_picture, self.wall_top_right_picture, self.wall_low_right_picture, 
        self.wall_low_left_picture, self.wall_horizontal_picture, self.wall_vertical_picture, self.ground_picture]
        # empty list that will indicate the coordinates of the labyrinth path
                
        self.path_position_list = []

        self.labyrinth_entry = (0, 520) #prevoir de mettre l'entree et la sortie dans le tableau

        self.labyrinth_exit = (440, 0)

    def blit_pictures(self):
        """Searchs each list for the coordinates of each image to paste them"""
        for i, elt in enumerate(self.LABYRINTH_LIST):
            for y, number in enumerate(elt):
                picture = self.PICTURE_LIST[number]
                location = (y*40, i*40)
                self.WINDOW.blit(picture, location)

    def path_location(self): 
        for i, elt in enumerate(self.LABYRINTH_LIST):
            for y, number in enumerate(elt):
                if number == 6:
                    self.path_position_list.append((y*40, i*40))
        return self.path_position_list



         

