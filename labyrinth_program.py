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
from random_position_objects import *
# import the file which indicates in list form the coordinates
# of the labyrinth path
from path_position import *

# initialize the pygame library
pygame.init()

# indicates the way to find the images to be used for the program
os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressource")

# use the function imported from the file decor_blit.py :
# paste the background
background()

# load the picture of the Mac Gyver, make the background
# of the picture transparent and paste the picture
MAC_GYVER_PICTURE = pygame.image.load("MacGyver.png").convert()
MAC_GYVER_PICTURE.set_colorkey((255, 255, 255))
MOVING_MAC_GYVER = MAC_GYVER_PICTURE.get_rect()
WINDOW.blit(MAC_GYVER_PICTURE, (0, 520))

# load the picture of the guardian, make the background
# of the picture transparent and paste the picture
GUARDIAN_PICTURE = pygame.image.load("guardian.png").convert()
GUARDIAN_PICTURE.set_colorkey((255, 255, 255))
WINDOW.blit(GUARDIAN_PICTURE, (440, 0))

# load the picture of the needle, make the background
# of the picture transparent and paste the picture
NEEDLE_PICTURE = pygame.image.load("needle.png").convert()
NEEDLE_PICTURE.set_colorkey((255, 255, 255))
WINDOW.blit(NEEDLE_PICTURE, NEEDLE_POSITION)

# load the picture of the ether, make the background
# of the picture transparent and paste the picture
ETHER_PICTURE = pygame.image.load("ether.png").convert_alpha()
ETHER_PICTURE.set_colorkey((0, 0, 0))
WINDOW.blit(ETHER_PICTURE, ETHER_POSITION)

# load the picture of the syringe, make the background
# of the picture transparent and paste the picture
SYRINGE_PICTURE = pygame.image.load("syringe.png").convert()
SYRINGE_PICTURE.set_colorkey((255, 255, 255))
WINDOW.blit(SYRINGE_PICTURE, SYRINGE_POSITION)

# load the picture of the grave and make the background
# of the picture transparent
GRAVE_PICTURE = pygame.image.load("grave.png").convert()
GRAVE_PICTURE.set_colorkey((255, 255, 255))

# load the picture of the won and make the background
# of the picture transparent
WON_PICTURE = pygame.image.load("won.png").convert()
WON_PICTURE.set_colorkey((255, 255, 255))

# refresh the screen
pygame.display.flip()

def init_event():
    """Function that paste the pictures and refresh the screen"""
    background()
    WINDOW.blit(GUARDIAN_PICTURE, (440, 0))
    WINDOW.blit(MAC_GYVER_PICTURE, (last_location_mac_gyver_tuple))
    WINDOW.blit(ETHER_PICTURE, ETHER_POSITION)
    WINDOW.blit(NEEDLE_PICTURE, NEEDLE_POSITION)
    WINDOW.blit(SYRINGE_PICTURE, SYRINGE_POSITION)
    pygame.display.flip()

# dictionary that indicates the last position of mac gyver
LAST_LOCATION_MAC_GYVER_DICT = {0: 520}
# list that indicates the coordinates of the path traveled
# by mac gyver
PATH_TRAVELED_MAC_GYVER = [(0, 520)]
# counter of objects
COUNTER_OBJECTS = 0

# infinite loop
PLAY = 1
while PLAY:
    for event in pygame.event.get():
        # if press the right arrow key? mac gyver goes right
        # creates a tuple that represents the last position of mac gyver
        # clears and recreates a new dictionary = last position of mac gyver
        if event.type == KEYDOWN and event.key == K_RIGHT:
            for cle, valeur in LAST_LOCATION_MAC_GYVER_DICT.items():
                MOVING_MAC_GYVER = MOVING_MAC_GYVER.move(40, 0)
                last_location_mac_gyver_tuple = (cle + 40, valeur)
                LAST_LOCATION_MAC_GYVER_DICT.clear()
                LAST_LOCATION_MAC_GYVER_DICT[cle + 40] = valeur
                init_event()
        # if press the left arrow key, mac gyver goes left
        # creates a tuple = last position of mac gyver
        # clears and recreates a new dictionary = last position of mac gyver
        if event.type == KEYDOWN and event.key == K_LEFT:
            for cle, valeur in LAST_LOCATION_MAC_GYVER_DICT.items():
                MOVING_MAC_GYVER = MOVING_MAC_GYVER.move(- 40, 0)
                last_location_mac_gyver_tuple = (cle - 40, valeur)
                LAST_LOCATION_MAC_GYVER_DICT.clear()
                LAST_LOCATION_MAC_GYVER_DICT[cle - 40] = valeur
                init_event()
        # if press the up arrow key, mac gyver goes up
        # creates a tuple = last position of mac gyver
        # clears and recreates a new dictionary = last position of mac gyver
        if event.type == KEYDOWN and event.key == K_UP:
            for cle, valeur in LAST_LOCATION_MAC_GYVER_DICT.items():
                MOVING_MAC_GYVER = MOVING_MAC_GYVER.move(0, - 40)
                last_location_mac_gyver_tuple = (cle, valeur - 40)
                LAST_LOCATION_MAC_GYVER_DICT.clear()
                LAST_LOCATION_MAC_GYVER_DICT[cle] = valeur- 40
                init_event()
        # if press the down arrow key, mac gyver goes down
        # creates a tuple = last position of mac gyver
        # clears and recreates a new dictionary = last position of mac gyver
        if event.type == KEYDOWN and event.key == K_DOWN:
            for cle, valeur in LAST_LOCATION_MAC_GYVER_DICT.items():
                MOVING_MAC_GYVER = MOVING_MAC_GYVER.move(0, 40)
                last_location_mac_gyver_tuple = (cle, valeur + 40)
                LAST_LOCATION_MAC_GYVER_DICT.clear()
                LAST_LOCATION_MAC_GYVER_DICT[cle] = valeur + 40
                init_event()
        # if press a key, creates a list with all mac gyver move coordinates
        if event.type == KEYDOWN:
            PATH_TRAVELED_MAC_GYVER.append(last_location_mac_gyver_tuple)
        # while mac gyver goes down on the coordinates of a wall
        # mac gyver returns to its original position
        while event.type == KEYDOWN and event.key == K_DOWN \
            and PATH_POSITION_LIST.count(last_location_mac_gyver_tuple) == 0:
            for cle, valeur in LAST_LOCATION_MAC_GYVER_DICT.items():
                MOVING_MAC_GYVER = MOVING_MAC_GYVER.move(0, - 40)
                last_location_mac_gyver_tuple = (cle, valeur - 40)
                LAST_LOCATION_MAC_GYVER_DICT.clear()
                LAST_LOCATION_MAC_GYVER_DICT[cle] = valeur - 40
                init_event()
        # while mac gyver goes up on the coordinates of a wall
        # mac gyver returns to its original position
        while event.type == KEYDOWN and event.key == K_UP \
            and PATH_POSITION_LIST.count(last_location_mac_gyver_tuple) == 0:
            for cle, valeur in LAST_LOCATION_MAC_GYVER_DICT.items():
                MOVING_MAC_GYVER = MOVING_MAC_GYVER.move(0, 40)
                last_location_mac_gyver_tuple = (cle, valeur + 40)
                LAST_LOCATION_MAC_GYVER_DICT.clear()
                LAST_LOCATION_MAC_GYVER_DICT[cle] = valeur + 40
                init_event()
        # while mac gyver goes right on the coordinates of a wall
        # mac gyver returns to its original position
        while event.type == KEYDOWN and event.key == K_RIGHT \
            and PATH_POSITION_LIST.count(last_location_mac_gyver_tuple) == 0:
            for cle, valeur in LAST_LOCATION_MAC_GYVER_DICT.items():
                MOVING_MAC_GYVER = MOVING_MAC_GYVER.move(- 40, 0)
                last_location_mac_gyver_tuple = (cle - 40, valeur)
                LAST_LOCATION_MAC_GYVER_DICT.clear()
                LAST_LOCATION_MAC_GYVER_DICT[cle - 40] = valeur
                init_event()
        # while mac gyver goes left on the coordinates of a wall
        # mac gyver returns to its original position
        while event.type == KEYDOWN and event.key == K_LEFT \
            and PATH_POSITION_LIST.count(last_location_mac_gyver_tuple) == 0:
            for cle, valeur in LAST_LOCATION_MAC_GYVER_DICT.items():
                MOVING_MAC_GYVER = MOVING_MAC_GYVER.move(40, 0)
                last_location_mac_gyver_tuple = (cle + 40, valeur)
                LAST_LOCATION_MAC_GYVER_DICT.clear()
                LAST_LOCATION_MAC_GYVER_DICT[cle + 40] = valeur
                init_event()
        # if mac gyver is passed on the neddle
        # +1 to the counter of objects and the needle disappears from the window
        if PATH_TRAVELED_MAC_GYVER.count(NEEDLE_POSITION) == 1:
            COUNTER_OBJECTS = COUNTER_OBJECTS + 1
            NEEDLE_POSITION = WINDOW.blit(NEEDLE_PICTURE, (600, 600))
        # if mac gyver is passed on the ether
        # +1 to the counter of objects and the ether disappears from the window
        if PATH_TRAVELED_MAC_GYVER.count(ETHER_POSITION) == 1:
            COUNTER_OBJECTS = COUNTER_OBJECTS + 1
            ETHER_POSITION = WINDOW.blit(ETHER_PICTURE, (600, 600))
        # if mac gyver is passed on the syringe
        # +1 to the counter of objects and the syringe disappears from the window
        if PATH_TRAVELED_MAC_GYVER.count(SYRINGE_POSITION) == 1:
            COUNTER_OBJECTS = COUNTER_OBJECTS + 1
            SYRINGE_POSITION = WINDOW.blit(SYRINGE_PICTURE, (600, 600))
        # if mac gyver have not the 3 objects and arrives at the guardian
        # the message "perdu !" is displayed
        if PATH_TRAVELED_MAC_GYVER.count((440, 0)) == 1 and COUNTER_OBJECTS != 3:
            background()
            WINDOW.blit(GUARDIAN_PICTURE, (440, 0))
            WINDOW.blit(MAC_GYVER_PICTURE, (last_location_mac_gyver_tuple))
            WINDOW.blit(GRAVE_PICTURE, (200, 200))
            pygame.display.flip()
        # if mac gyver have the 3 objects and arrives at the guardian
        # the message "gagné !" is displayed and the program quits
        if LAST_LOCATION_MAC_GYVER_DICT == {440: 0} and COUNTER_OBJECTS == 3:
            background()
            WINDOW.blit(ETHER_PICTURE, ETHER_POSITION)
            WINDOW.blit(NEEDLE_PICTURE, NEEDLE_POSITION)
            WINDOW.blit(SYRINGE_PICTURE, SYRINGE_POSITION)
            WINDOW.blit(WON_PICTURE, (120, 120))
            pygame.display.flip()
            PLAY = 0
