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
labyrinth = class_of_labyrinth.Labyrinth()
person = class_of_person.Person()
objects = class_of_objects.Objects()


def labyrinth_game():
    """For replay the game"""
    # indicates the way to find the images to be used for the program
    os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")
    
    
    objects.color_blit_objects()
    
    labyrinth.blit_pictures()

    person.color_blit_person()

    pygame.display.flip()


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


            

            
            
                    

           
            """# if mac gyver is passed on the neddle
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
                quit()"""
labyrinth_game()
