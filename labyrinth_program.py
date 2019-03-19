#! /usr/bin/env python3
# coding: utf-8

""" Labyrinth game in which mac gyver must retrieve all objects
to kill the guardian and escape """

import os

# import the pygame library and this module
import pygame
from pygame.locals import *

# import lists that visually represent the game background
from labyrinth_position import *
# import decor_blit.py that creates the window
# and paste the background
from decor_blit import *
# import the file that defines the random coordinates of objects
from random_position_objects import RandomPosition
# import the file which indicates in list form the coordinates
# of the labyrinth path
from path_position import *

# initialize the pygame library
pygame.init()

def labyrinth_game():
    """For replay the game"""
    # indicates the way to find the images to be used for the program
    os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")


    

    
    # refresh the screen
    pygame.display.flip()

    