#! /usr/bin/env python3
# coding: UTF-8

""" Labyrinth game in which mac gyver must retrieve all objects
to kill the guardian and escape """
import os

import pygame # import the pygame library and this module
from pygame.locals import *
pygame.init() # initialize the pygame library

import class_of_person # import modules of the game

# path to the pictures
os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")

def labyrinth_game():
    """play the game"""

    person = class_of_person.Person() # instantiate the class Person

    person.init_event() # blits the pictures

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

            # Mac Gyver picks up the objects
            person.pick_up_objects()

            # Mac Gyver does not move when he arrives on the guardian
            person.keep_still()

            # if Mac Gyver loses, the player may choose to restart or stop the program
            if person.lost() == 1:
                if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                and event.pos[0] > 520 and event.pos[1] > 520:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                and event.pos[0] < 80 and event.pos[1] > 520:
                    labyrinth_game()

            # if Mac Gyver wins, the program stops
            if person.won() == 1:
                pygame.quit()
                quit()

# call the function to play the game
labyrinth_game()
