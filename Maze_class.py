#! /usr/bin/env python3
# coding: UTF-8


""" class Maze """

import os 
os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")
import pygame # import the pygame library


class Maze:
    """creating the window, features of the maze and blit the background"""

    def __init__(self):
        """creating the window, features of the maze and download pictures"""
        # open and read the file
        with open("maze_structure.txt", "r") as maze_structure:
            maze_structure = maze_structure.read()
        
        # creates liste of maze
        self.maze_list = []
        i = 0
        while i < 15:
            self.maze_list.append(list(maze_structure.split()[i]))
            i += 1
        
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

        # list of pictures so each index corresponds to the number of the maze_list
        self.pictures_list = [self.wall_top_left_picture, self.wall_top_right_picture,
                              self.wall_low_right_picture, self.wall_low_left_picture,
                              self.wall_horizontal_picture, self.wall_vertical_picture,
                              self.ground_picture, self.ground_picture, self.ground_picture]

        # list that contains the coordinates of the maze path
        self.path_position_list = []

        # determining the coordinates of the maze entry and exit : number 7 and 8 in the maze_list
        for i, elt in enumerate(self.maze_list):
            for index, number in enumerate(elt):
                if number == "7":
                    self.maze_entry = (index * 40, i * 40)
                if number == "8":
                    self.maze_exit = (index * 40, i * 40)

    def blit_pictures(self):
        """determining the coordinates of each picture to blit them"""
        for i, elt in enumerate(self.maze_list):
            for index, number in enumerate(elt):
                number = int(number)
                picture = self.pictures_list[number]
                location = (index * 40, i * 40)
                self.window.blit(picture, location)

    def path_location(self):
        """determining the coordinates of the path"""
        for i, elt in enumerate(self.maze_list):
            for index, number in enumerate(elt):
                if number in ("6", "7", "8"):
                    self.path_position_list.append((index * 40, i * 40))
        return self.path_position_list
