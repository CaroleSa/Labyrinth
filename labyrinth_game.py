#! /usr/bin/env python3
# coding: UTF-8

""" Labyrinth game in which mac gyver must retrieve all objects
to kill the guardian and escape """

import os

# import the pygame library and this module
import pygame
from pygame.locals import *
# initialize the pygame library
pygame.init()

# import modules of the game
import class_of_labyrinth
import class_of_person
import class_of_objects
"""labyrinth = class_of_labyrinth.Labyrinth()
person = class_of_person.Person()
objects = class_of_objects.Objects()"""


def labyrinth_game():

    labyrinth = class_of_labyrinth.Labyrinth()
    person = class_of_person.Person()
    objects = class_of_objects.Objects()
    
    """For replay the game"""
    # indicates the way to find the images to be used for the program
    os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")

    person.init_event()

    # infinite loop
    play = 1
    while play:

        for event in pygame.event.get():
            
            # Mac Gyver turns to the right and avoids the wall
            if event.type == KEYDOWN and event.key == K_RIGHT:
                person.movement_right()

            # Mac Gyver turns to the left and avoids the wall
            if event.type == KEYDOWN and event.key == K_LEFT:
                person.movement_left()

            # Mac Gyver goes up and avoids the wall
            if event.type == KEYDOWN and event.key == K_UP:
                person.movement_up()

            # Mac Gyver goes down and avoids the wall
            if event.type == KEYDOWN and event.key == K_DOWN:
                person.movement_down()

            person.pick_up_objects()

            # Mac Gyver keep still when he arrives on the guardian
            person.keep_still()

            if person.lost() == 1:
                if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                and event.pos[0] > 520 and event.pos[1] > 520:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                and event.pos[0] < 80 and event.pos[1] > 520:
                    labyrinth_game()

            if person.won() == 1:
                pygame.quit()
                quit()

labyrinth_game()
