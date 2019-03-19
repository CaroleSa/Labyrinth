#! /usr/bin/env python3
# coding: utf-8

""" Creates the window and paste the background """

import os
import pygame                    # import the pygame library and this module
from pygame.locals import *
from labyrinth_position import * # import lists that visually represent the game background

# initialize the pygame library
pygame.init()

# creates the window
WINDOW = pygame.display.set_mode((600, 600))

def background():
    """Function that pastes multiple images to create the wallpaper"""
    
    # load the pictures of the wall and the ground
    ground_picture = pygame.image.load("ground.png").convert_alpha()
    wall_top_left_picture = pygame.image.load("top_left.png").convert_alpha()
    wall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
    wall_low_right_picture = pygame.image.load("low_right.png").convert_alpha()
    wall_low_left_picture = pygame.image.load("low_left.png").convert_alpha()
    wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
    wall_vertical_picture = pygame.image.load("vertical.png").convert_alpha()

    def wall_ground_location(line_number, index, number_picture, picture):
        """Searchs each list for the coordinates of each image to paste them"""
        coordinates_number_picture_list = []

        for i, elt in enumerate(line_number):
            if elt == number_picture:
                coordinates_number_picture_list.append(((i*40), index))
        for location in coordinates_number_picture_list:
            WINDOW.blit(picture, (location))

    # call the function with different parameters
    wall_ground_location(LINE_0, 0, "0", wall_top_left_picture)
    wall_ground_location(LINE_1, 40, "0", wall_top_left_picture)
    wall_ground_location(LINE_2, 80, "0", wall_top_left_picture)
    wall_ground_location(LINE_3, 120, "0", wall_top_left_picture)
    wall_ground_location(LINE_4, 160, "0", wall_top_left_picture)
    wall_ground_location(LINE_5, 200, "0", wall_top_left_picture)
    wall_ground_location(LINE_6, 240, "0", wall_top_left_picture)
    wall_ground_location(LINE_7, 280, "0", wall_top_left_picture)
    wall_ground_location(LINE_8, 320, "0", wall_top_left_picture)
    wall_ground_location(LINE_9, 360, "0", wall_top_left_picture)
    wall_ground_location(LINE_10, 400, "0", wall_top_left_picture)
    wall_ground_location(LINE_11, 440, "0", wall_top_left_picture)
    wall_ground_location(LINE_12, 480, "0", wall_top_left_picture)
    wall_ground_location(LINE_13, 520, "0", wall_top_left_picture)
    wall_ground_location(LINE_14, 560, "0", wall_top_left_picture)

    wall_ground_location(LINE_0, 0, "1", wall_top_right_picture)
    wall_ground_location(LINE_1, 40, "1", wall_top_right_picture)
    wall_ground_location(LINE_2, 80, "1", wall_top_right_picture)
    wall_ground_location(LINE_3, 120, "1", wall_top_right_picture)
    wall_ground_location(LINE_4, 160, "1", wall_top_right_picture)
    wall_ground_location(LINE_5, 200, "1", wall_top_right_picture)
    wall_ground_location(LINE_6, 240, "1", wall_top_right_picture)
    wall_ground_location(LINE_7, 280, "1", wall_top_right_picture)
    wall_ground_location(LINE_8, 320, "1", wall_top_right_picture)
    wall_ground_location(LINE_9, 360, "1", wall_top_right_picture)
    wall_ground_location(LINE_10, 400, "1", wall_top_right_picture)
    wall_ground_location(LINE_11, 440, "1", wall_top_right_picture)
    wall_ground_location(LINE_12, 480, "1", wall_top_right_picture)
    wall_ground_location(LINE_13, 520, "1", wall_top_right_picture)
    wall_ground_location(LINE_14, 560, "1", wall_top_right_picture)

    wall_ground_location(LINE_0, 0, "2", wall_low_right_picture)
    wall_ground_location(LINE_1, 40, "2", wall_low_right_picture)
    wall_ground_location(LINE_2, 80, "2", wall_low_right_picture)
    wall_ground_location(LINE_3, 120, "2", wall_low_right_picture)
    wall_ground_location(LINE_4, 160, "2", wall_low_right_picture)
    wall_ground_location(LINE_5, 200, "2", wall_low_right_picture)
    wall_ground_location(LINE_7, 280, "2", wall_low_right_picture)
    wall_ground_location(LINE_8, 320, "2", wall_low_right_picture)
    wall_ground_location(LINE_9, 360, "2", wall_low_right_picture)
    wall_ground_location(LINE_10, 400, "2", wall_low_right_picture)
    wall_ground_location(LINE_11, 440, "2", wall_low_right_picture)
    wall_ground_location(LINE_12, 480, "2", wall_low_right_picture)
    wall_ground_location(LINE_13, 520, "2", wall_low_right_picture)
    wall_ground_location(LINE_14, 560, "2", wall_low_right_picture)

    wall_ground_location(LINE_0, 0, "3", wall_low_left_picture)
    wall_ground_location(LINE_1, 40, "3", wall_low_left_picture)
    wall_ground_location(LINE_2, 80, "3", wall_low_left_picture)
    wall_ground_location(LINE_3, 120, "3", wall_low_left_picture)
    wall_ground_location(LINE_4, 160, "3", wall_low_left_picture)
    wall_ground_location(LINE_5, 200, "3", wall_low_left_picture)
    wall_ground_location(LINE_6, 240, "3", wall_low_left_picture)
    wall_ground_location(LINE_7, 280, "3", wall_low_left_picture)
    wall_ground_location(LINE_8, 320, "3", wall_low_left_picture)
    wall_ground_location(LINE_9, 360, "3", wall_low_left_picture)
    wall_ground_location(LINE_10, 400, "3", wall_low_left_picture)
    wall_ground_location(LINE_11, 440, "3", wall_low_left_picture)
    wall_ground_location(LINE_12, 480, "3", wall_low_left_picture)
    wall_ground_location(LINE_13, 520, "3", wall_low_left_picture)
    wall_ground_location(LINE_14, 560, "3", wall_low_left_picture)

    wall_ground_location(LINE_0, 0, "4", wall_horizontal_picture)
    wall_ground_location(LINE_1, 40, "4", wall_horizontal_picture)
    wall_ground_location(LINE_2, 80, "4", wall_horizontal_picture)
    wall_ground_location(LINE_3, 120, "4", wall_horizontal_picture)
    wall_ground_location(LINE_4, 160, "4", wall_horizontal_picture)
    wall_ground_location(LINE_5, 200, "4", wall_horizontal_picture)
    wall_ground_location(LINE_6, 240, "4", wall_horizontal_picture)
    wall_ground_location(LINE_7, 280, "4", wall_horizontal_picture)
    wall_ground_location(LINE_8, 320, "4", wall_horizontal_picture)
    wall_ground_location(LINE_9, 360, "4", wall_horizontal_picture)
    wall_ground_location(LINE_10, 400, "4", wall_horizontal_picture)
    wall_ground_location(LINE_11, 440, "4", wall_horizontal_picture)
    wall_ground_location(LINE_12, 480, "4", wall_horizontal_picture)
    wall_ground_location(LINE_13, 520, "4", wall_horizontal_picture)
    wall_ground_location(LINE_14, 560, "4", wall_horizontal_picture)

    wall_ground_location(LINE_0, 0, "5", wall_vertical_picture)
    wall_ground_location(LINE_1, 40, "5", wall_vertical_picture)
    wall_ground_location(LINE_2, 80, "5", wall_vertical_picture)
    wall_ground_location(LINE_3, 120, "5", wall_vertical_picture)
    wall_ground_location(LINE_4, 160, "5", wall_vertical_picture)
    wall_ground_location(LINE_5, 200, "5", wall_vertical_picture)
    wall_ground_location(LINE_6, 240, "5", wall_vertical_picture)
    wall_ground_location(LINE_7, 280, "5", wall_vertical_picture)
    wall_ground_location(LINE_8, 320, "5", wall_vertical_picture)
    wall_ground_location(LINE_9, 360, "5", wall_vertical_picture)
    wall_ground_location(LINE_10, 400, "5", wall_vertical_picture)
    wall_ground_location(LINE_11, 440, "5", wall_vertical_picture)
    wall_ground_location(LINE_12, 480, "5", wall_vertical_picture)
    wall_ground_location(LINE_13, 520, "5", wall_vertical_picture)
    wall_ground_location(LINE_14, 560, "5", wall_vertical_picture)

    wall_ground_location(LINE_0, 0, "6", ground_picture)
    wall_ground_location(LINE_1, 40, "6", ground_picture)
    wall_ground_location(LINE_2, 80, "6", ground_picture)
    wall_ground_location(LINE_3, 120, "6", ground_picture)
    wall_ground_location(LINE_4, 160, "6", ground_picture)
    wall_ground_location(LINE_5, 200, "6", ground_picture)
    wall_ground_location(LINE_6, 240, "6", ground_picture)
    wall_ground_location(LINE_7, 280, "6", ground_picture)
    wall_ground_location(LINE_8, 320, "6", ground_picture)
    wall_ground_location(LINE_9, 360, "6", ground_picture)
    wall_ground_location(LINE_10, 400, "6", ground_picture)
    wall_ground_location(LINE_11, 440, "6", ground_picture)
    wall_ground_location(LINE_12, 480, "6", ground_picture)
    wall_ground_location(LINE_13, 520, "6", ground_picture)
    wall_ground_location(LINE_14, 560, "6", ground_picture)
    return WINDOW
