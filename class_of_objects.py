#! /usr/bin/env python3
# coding: UTF-8 je garde

import os

import random
# import the pygame library and this module
import pygame
from pygame.locals import *
# initialize the pygame library
pygame.init()

import class_of_labyrinth

class Objects:
    
    def __init__(self):
        self.labyrinth = class_of_labyrinth.Labyrinth()

        self.WINDOW = self.labyrinth.WINDOW
        os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")
        self.object_1 = pygame.image.load("needle.png").convert()
        self.object_2 = pygame.image.load("ether.png").convert()
        self.object_3 = pygame.image.load("plastic_tube.png").convert()

    def random_position(self):
        self.labyrinth_entry = self.labyrinth.labyrinth_entry
        self.labyrinth_exit = self.labyrinth.labyrinth_exit
        self.path_location = self.labyrinth.path_location()

        self.path_location.remove(self.labyrinth.labyrinth_entry)
        self.path_location.remove(self.labyrinth.labyrinth_exit)
        self.list_random_position = random.sample(self.path_location, 3)
        return self.list_random_position
   
    def __get__value_position_objects(self):
        self.WINDOW = self.labyrinth.WINDOW

        self.position_object_1 = self.random_position()[0]
        self.position_object_2 = self.random_position()[1]
        self.position_object_3 = self.random_position()[2]
        return self.position_object_1, self.position_object_2, self.position_object_3

    def color_blit_objects(self):
        self.object_1.set_colorkey((255, 255, 255))
        self.object_2.set_colorkey((255, 255, 255))
        self.object_3.set_colorkey((255, 255, 255))

        self.WINDOW.blit(self.object_1, self.__get__value_position_objects()[0])
        self.WINDOW.blit(self.object_2, self.__get__value_position_objects()[1])
        self.WINDOW.blit(self.object_3, self.__get__value_position_objects()[2])

Objects()