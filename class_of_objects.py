#! /usr/bin/env python3
# coding: UTF-8 je garde


"""class Objects"""


import random  # import the random library
import pygame  # import the pygame library and this module
from pygame.locals import *

import class_of_labyrinth  # import module of the game


class Objects:
    """random position of objects and blit the objects"""

    def __init__(self):
        """random position of objects and download pictures"""
        # instantiate the class Labyrinth
        self.labyrinth = class_of_labyrinth.Labyrinth()
        self.labyrinth_entry = self.labyrinth.labyrinth_entry
        self.labyrinth_exit = self.labyrinth.labyrinth_exit
        self.path_location = self.labyrinth.path_location()
        self.window = self.labyrinth.window
        # download pictures
        self.object_1 = pygame.image.load("needle.png").convert()
        self.object_2 = pygame.image.load("ether.png").convert()
        self.object_3 = pygame.image.load("plastic_tube.png").convert()
        # determination of the random position objects
        self.path_location.remove(self.labyrinth_entry)
        self.path_location.remove(self.labyrinth_exit)
        self.list_random_position = random.sample(self.path_location, 3)
        self.position_object_1 = self.list_random_position[0]
        self.position_object_2 = self.list_random_position[1]
        self.position_object_3 = self.list_random_position[2]

    def color_blit_objects(self):
        """transparency of the background and blit of the pictures : objects"""
        self.object_1.set_colorkey((255, 255, 255))
        self.object_2.set_colorkey((255, 255, 255))
        self.object_3.set_colorkey((255, 255, 255))
        self.window.blit(self.object_1, self.position_object_1)
        self.window.blit(self.object_2, self.position_object_2)
        self.window.blit(self.object_3, self.position_object_3)

    def disappearance_object_1(self):
        """disappearing object 1 by blit them outside the window"""
        self.position_object_1 = (600, 600)
        return self.position_object_1

    def disappearance_object_2(self):
        """disappearing object 2 by blit them outside the window"""
        self.position_object_2 = (600, 600)
        return self.position_object_2

    def disappearance_object_3(self):
        """disappearing object 3 by blit them outside the window"""
        self.position_object_3 = (600, 600)
        return self.position_object_3
