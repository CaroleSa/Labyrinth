#! /usr/bin/env python3
# coding: UTF-8 je garde


"""class Objects"""


import random  # import the random module
import pygame  # import the pygame library

import maze_class # import file


class Objects:
    """random position of objects and blit the objects"""

    def __init__(self):
        """random position of objects and download pictures"""
        # instantiate the class Maze
        self.maze = maze_class.Maze()
        self.maze_entry = self.maze.maze_entry
        self.maze_exit = self.maze.maze_exit
        self.path_location = self.maze.path_location()
        self.window = self.maze.window
        # download pictures
        self.object_1 = pygame.image.load("needle.png").convert()
        self.object_2 = pygame.image.load("ether.png").convert()
        self.object_3 = pygame.image.load("plastic_tube.png").convert()
        # determination of the random position objects
        self.path_location.remove(self.maze_entry)
        self.path_location.remove(self.maze_exit)
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
        self.position_object_1 = (2000, 2000)
        return self.position_object_1

    def disappearance_object_2(self):
        """disappearing object 2 by blit them outside the window"""
        self.position_object_2 = (2000, 2000)
        return self.position_object_2

    def disappearance_object_3(self):
        """disappearing object 3 by blit them outside the window"""
        self.position_object_3 = (2000, 2000)
        return self.position_object_3
