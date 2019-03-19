#! /usr/bin/env python3
# coding: utf-8

"""Allows to define the coordinates of objects at random"""

from random import *             # import the random library
from labyrinth_position import * # import lists that represent the game background

class RandomPosition:
    """Class that determines a random line and a random number in this line"""
    def __init__(self):
        line_list = [LINE_1, LINE_2, LINE_3, LINE_4, LINE_5, LINE_6, LINE_7, LINE_8,
                     LINE_9, LINE_10, LINE_11, LINE_12, LINE_13]
        path_position_of_random_line = []

        random_line = choice(line_list) # determines a random line
        # add in path_position_of_random_line the path coordinates of the random list
        for i, elt in enumerate(random_line):
            if elt == "6":
                index_random_line = line_list.index(random_line)
                path_position_of_random_line.append(((i * 40), (index_random_line + 1) * 40))
        # determines a random coordinates
        self.random_location = choice(path_position_of_random_line)
