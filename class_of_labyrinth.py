#! /usr/bin/env python3
# coding: UTF-8


""" class Labyrinth """


import pygame # import the pygame library and this module
from pygame.locals import *


class Labyrinth:
    """features of the labyrinth and blit the background"""

    def __init__(self):
        """features of the labyrinth and download pictures"""
        # corresponds to the visual of the labyrinth,
        # each number corresponds to an picture :
        # 0 wall_top_left_picture   5 wall_vertical_picture
        # 1 wall_top_right_picture  6 ground_picture
        # 2 wall_low_right_picture  7 labyrinth_entry
        # 3 wall_low_left_picture   8 labyrinth exit
        # 4 wall_horizontal_picture
        self.labyrinth_list = [
            [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 8, 3, 4, 1],
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
            [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2]]

        # creates the window
        self.window = pygame.display.set_mode((600, 600))

        # download pictures
        self.ground_picture = pygame.image.load("ground.png").convert_alpha()
        self.wall_top_left_picture = pygame.image.load("top_left.png").convert_alpha()
        self.wall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        self.wall_low_right_picture = pygame.image.load("low_right.png").convert_alpha()
        self.wall_low_left_picture = pygame.image.load("low_left.png").convert_alpha()
        self.wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
        self.wall_vertical_picture = pygame.image.load("vertical.png").convert_alpha()

        # list of pictures so each index corresponds to the number of the LABYRINTH_LIST
        self.pictures_list = [self.wall_top_left_picture, self.wall_top_right_picture,
                              self.wall_low_right_picture, self.wall_low_left_picture,
                              self.wall_horizontal_picture, self.wall_vertical_picture,
                              self.ground_picture, self.ground_picture, self.ground_picture]

        # list that contains the coordinates of the labyrinth path
        self.path_position_list = []

        # determining the coordinates of the labyrinth entry and exit
        for i, elt in enumerate(self.labyrinth_list):
            for index, number in enumerate(elt):
                if number == 7:
                    self.labyrinth_entry = (index * 40, i * 40)
                if number == 8:
                    self.labyrinth_exit = (index * 40, i * 40)

    def blit_pictures(self):
        """determining the coordinates of each picture to blit them"""
        for i, elt in enumerate(self.labyrinth_list):
            for index, number in enumerate(elt):
                picture = self.pictures_list[number]
                location = (index * 40, i * 40)
                self.window.blit(picture, location)

    def path_location(self):
        """determining the coordinates of the path"""
        for i, elt in enumerate(self.labyrinth_list):
            for index, number in enumerate(elt):
                if number in (6, 7, 8):
                    self.path_position_list.append((index * 40, i * 40))
        return self.path_position_list
