#! /usr/bin/env python3
# coding: UTF-8
""" Maze game in which mac gyver must retrieve all objects
to kill the guardian and escape """


import os

# pylint: disable = no-member
import pygame # import the pygame library
import pygame.locals
pygame.init() # initialize the pygame library

import person_class as pc # import file

# path to the pictures
os.chdir("./ressources")


def maze_game():
    """play the game"""

    person = pc.Person() # instantiate the class Person
    person.init_event() # blits the pictures

    play = 1
    while play:  # infinite loop

        for event in pygame.event.get():
            # if the player presses the right key
            # Mac Gyver turns to the right and avoids the wall
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                person.movement(+ 40, 0)

            # if the player presses the left key
            # Mac Gyver turns to the left and avoids the wall
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                person.movement(- 40, 0)

            # if the player presses the up key
            # Mac Gyver goes up and avoids the wall
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                person.movement(0, - 40)

            # if the player presses the down key
            # Mac Gyver goes down and avoids the wall
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                person.movement(0, + 40)

            # Mac Gyver picks up the objects
            person.pick_up_objects()

            # Mac Gyver does not move when he arrives on the guardian
            person.keep_still(0, - 40)
            person.keep_still(0, + 40)
            person.keep_still(- 40, 0)
            person.keep_still(+ 40, 0)

            # if Mac Gyver loses, the player may choose to restart or stop the program
            if person.lost() == 1:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
                and event.pos[0] > 520 and event.pos[1] > 520:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
                and event.pos[0] < 80 and event.pos[1] > 520:
                    maze_game()

            # if Mac Gyver wins, the program stops
            if person.won() == 1:
                quit()

# call the function to play the game
maze_game()

def main():
    """use of class Person"""
    pc.Person()

if __name__ == "__main__":
    # execute only if run as a script
    main()
