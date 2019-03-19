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
    os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressource")
    
    # creating variables with random coordinates for each objects
    needle_location = RandomPosition()
    ether_location = RandomPosition()
    plastic_tube_location = RandomPosition()
    needle_position = needle_location.random_location
    ether_position = ether_location.random_location
    plastic_tube_position = plastic_tube_location.random_location

    # while the objects overlap, we determine a new random coordinates
    while needle_position == ether_position or ether_position == plastic_tube_position \
        or plastic_tube_position == needle_position:
        needle_location = RandomPosition()
        ether_location = RandomPosition()
        plastic_tube_location = RandomPosition()
        needle_position = needle_location.random_location
        ether_position = ether_location.random_location
        plastic_tube_position = plastic_tube_location.random_location
    # while the objects overlap the characters, we determine a new random coordinates
    while needle_position == (0, 520) or ether_position == (0, 520) or plastic_tube_position == (0, 520):
        needle_location = RandomPosition()
        ether_location = RandomPosition()
        plastic_tube_location = RandomPosition()
        needle_position = needle_location.random_location
        ether_position = ether_location.random_location
        splastic_tube_position = plastic_tube_location.random_location

    # use the function imported from the file decor_blit.py :
    # paste the background
    background()

    # load the picture of the Mac Gyver, make the background
    # of the picture transparent and paste the picture
    mac_gyver_picture = pygame.image.load("MacGyver.png").convert()
    mac_gyver_picture.set_colorkey((255, 255, 255))
    moving_mac_gyver = mac_gyver_picture.get_rect()
    WINDOW.blit(mac_gyver_picture, (0, 520))

    # load the picture of the guardian, make the background
    # of the picture transparent and paste the picture
    guardian_picture = pygame.image.load("guardian.png").convert()
    guardian_picture.set_colorkey((255, 255, 255))
    WINDOW.blit(guardian_picture, (440, 0))

    # load the picture of the needle, make the background
    # of the picture transparent and paste the picture
    needle_picture = pygame.image.load("needle.png").convert()
    needle_picture.set_colorkey((255, 255, 255))
    WINDOW.blit(needle_picture, needle_position)

    # load the picture of the ether, make the background
    # of the picture transparent and paste the picture
    ether_picture = pygame.image.load("ether.png").convert()
    ether_picture.set_colorkey((255, 255, 255))
    WINDOW.blit(ether_picture, ether_position)

    # load the picture of the plastic tube, make the background
    # of the picture transparent and paste the picture
    plastic_tube_picture = pygame.image.load("plastic_tube.png").convert()
    plastic_tube_picture.set_colorkey((255, 255, 255))
    WINDOW.blit(plastic_tube_picture, plastic_tube_position)

    # load the picture of the grave and make the background
    # of the picture transparent
    grave_picture = pygame.image.load("grave.png").convert()
    grave_picture.set_colorkey((255, 255, 255))

    # load the picture of the won and make the background
    # of the picture transparent
    won_picture = pygame.image.load("won.png").convert()
    won_picture.set_colorkey((255, 255, 255))

    # load the picture of the quit and make the background
    # of the picture transparent
    quit_picture = pygame.image.load("quit.png").convert()
    quit_picture.set_colorkey((255, 255, 255))

    # load the picture of the replay and make the background
    # of the picture transparent
    replay_picture = pygame.image.load("replay.png").convert()
    replay_picture.set_colorkey((255, 255, 255))

    # refresh the screen
    pygame.display.flip()

    def init_event():
        """Function that paste the pictures and refresh the screen"""
        background()
        WINDOW.blit(guardian_picture, (440, 0))
        WINDOW.blit(mac_gyver_picture, (last_location_mac_gyver_tuple))
        WINDOW.blit(ether_picture, ether_position)
        WINDOW.blit(needle_picture, needle_position)
        WINDOW.blit(plastic_tube_picture, plastic_tube_position)
        pygame.display.flip()

    # dictionary that indicates the last position of mac gyver
    last_location_mac_gyver_dict = {0: 520}
    # list that indicates the coordinates of the path traveled
    # by mac gyver
    path_traveled_mac_gyver = [(0, 520)]
    # counter of objects
    counter_objects = 0

    # infinite loop
    play = 1
    while play:
        for event in pygame.event.get():
            # if press the right arrow key? mac gyver goes right
            # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
            if event.type == KEYDOWN and event.key == K_RIGHT:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(40, 0)
                    last_location_mac_gyver_tuple = (cle + 40, valeur)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle + 40] = valeur
                    path_traveled_mac_gyver.append(last_location_mac_gyver_tuple)
                    init_event()
            # if press the left arrow key, mac gyver goes left
            # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
            if event.type == KEYDOWN and event.key == K_LEFT:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(- 40, 0)
                    last_location_mac_gyver_tuple = (cle - 40, valeur)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle - 40] = valeur
                    path_traveled_mac_gyver.append(last_location_mac_gyver_tuple)
                    init_event()
            # if press the up arrow key, mac gyver goes up
            # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
            if event.type == KEYDOWN and event.key == K_UP:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(0, - 40)
                    last_location_mac_gyver_tuple = (cle, valeur - 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur -40
                    path_traveled_mac_gyver.append(last_location_mac_gyver_tuple)
                    init_event()
            # if press the down arrow key, mac gyver goes down
            # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
            if event.type == KEYDOWN and event.key == K_DOWN:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(0, 40)
                    last_location_mac_gyver_tuple = (cle, valeur + 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur + 40
                    path_traveled_mac_gyver.append(last_location_mac_gyver_tuple)
                    init_event()
            # if mac gyver goes down on the coordinates of a wall
            # mac gyver returns to its original position
            if event.type == KEYDOWN and event.key == K_DOWN \
                and path_position_list.count(last_location_mac_gyver_tuple) == 0:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(0, - 40)
                    del path_traveled_mac_gyver[-1]
                    last_location_mac_gyver_tuple = (cle, valeur - 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur - 40
                    init_event()
            # if mac gyver goes up on the coordinates of a wall
            # mac gyver returns to its original position
            if event.type == KEYDOWN and event.key == K_UP \
                and path_position_list.count(last_location_mac_gyver_tuple) == 0:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(0, 40)
                    del path_traveled_mac_gyver[-1]
                    last_location_mac_gyver_tuple = (cle, valeur + 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur + 40
                    init_event()
            # if mac gyver goes right on the coordinates of a wall
            # mac gyver returns to its original position
            if event.type == KEYDOWN and event.key == K_RIGHT \
                and path_position_list.count(last_location_mac_gyver_tuple) == 0:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(- 40, 0)
                    del path_traveled_mac_gyver[-1]
                    last_location_mac_gyver_tuple = (cle - 40, valeur)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle - 40] = valeur
                    init_event()
            # if mac gyver goes left on the coordinates of a wall
            # mac gyver returns to its original position
            if event.type == KEYDOWN and event.key == K_LEFT \
                and path_position_list.count(last_location_mac_gyver_tuple) == 0:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    del path_traveled_mac_gyver[-1]
                    moving_mac_gyver = moving_mac_gyver.move(40, 0)
                    last_location_mac_gyver_tuple = (cle + 40, valeur)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle + 40] = valeur
                    init_event()
            # if the player arrives on the guardien, he can no longer move
            if last_location_mac_gyver_dict == {440: - 40}:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    last_location_mac_gyver_tuple = (cle, valeur + 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur + 40
                    init_event()
            if path_traveled_mac_gyver.count((440, 0)) == 1 \
                and last_location_mac_gyver_dict == {440: 40}:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    del path_traveled_mac_gyver[-1]
                    last_location_mac_gyver_tuple = (cle, valeur - 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur - 40
                    init_event()
            # if mac gyver is passed on the neddle
            # +1 to the counter of objects and the needle disappears from the window
            if path_traveled_mac_gyver.count(needle_position) == 1:
                counter_objects = counter_objects + 1
                needle_position = WINDOW.blit(needle_picture, (600, 600))
            # if mac gyver is passed on the ether
            # +1 to the counter of objects and the ether disappears from the window
            if path_traveled_mac_gyver.count(ether_position) == 1:
                counter_objects = counter_objects + 1
                ether_position = WINDOW.blit(ether_picture, (600, 600))
            # if mac gyver is passed on the plastic_tube
            # +1 to the counter of objects and the syringe disappears from the window
            if path_traveled_mac_gyver.count(plastic_tube_position) == 1:
                counter_objects = counter_objects + 1
                plastic_tube_position = WINDOW.blit(plastic_tube_picture, (600, 600))
            # if mac gyver have not the 3 objects and arrives at the guardian
            # the messages "perdu !", "rejouer" and "quitter" is displayed
            # if the player clicks on "rejouer", the program restarts,
            # on "quitter", the program stops
            if last_location_mac_gyver_dict == {440: 0} and counter_objects != 3:
                background()
                WINDOW.blit(guardian_picture, (440, 0))
                WINDOW.blit(grave_picture, (200, 200))
                WINDOW.blit(replay_picture, (0, 520))
                WINDOW.blit(quit_picture, (520, 520))
                pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                    and event.pos[0] > 520 and event.pos[1] > 520:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                    and event.pos[0] < 80 and event.pos[1] > 520:
                    labyrinth_game()
            # if mac gyver have the 3 objects and arrives at the guardian
            # the message "gagné !" is displayed and the program quits
            if last_location_mac_gyver_dict == {440: 0} and counter_objects == 3:
                background()
                WINDOW.blit(won_picture, (120, 120))
                pygame.display.flip()
                pygame.quit()
                quit()
labyrinth_game()
