#! /usr/bin/env python3
# coding: UTF-8 je garde

import os

import random
# import the pygame library and this module
import pygame
from pygame.locals import *
# initialize the pygame library
pygame.init()

import class_of_labyrinth
import class_of_objects

class Person():
    
    

    def __init__(self):
        self.labyrinth = class_of_labyrinth.Labyrinth()
        self.objects = class_of_objects.Objects()
    
        self.WINDOW = self.labyrinth.WINDOW
        self.labyrinth_entry = self.labyrinth.labyrinth_entry
        os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")        
        self.grave_picture = pygame.image.load("grave.png").convert()
        self.replay_picture = pygame.image.load("replay.png").convert()
        self.won_picture = pygame.image.load("won.png").convert()
        self.quit_picture = pygame.image.load("quit.png").convert()
        self.guardian_picture = pygame.image.load("guardian.png").convert()
        self.mac_gyver_picture = pygame.image.load("MacGyver.png").convert()
        # dictionary that indicates the last position of mac gyver
        self.last_location_mac_gyver_dict = {self.labyrinth_entry[0]: self.labyrinth_entry[1]}
        # list that indicates the coordinates of the path traveled
        # by mac gyver
        self.path_traveled_mac_gyver = [self.labyrinth_entry]
        # counter of objects
        self.counter_objects = 0 
        self.last_location_mac_gyver_tuple = self.labyrinth_entry
        self.moving_mac_gyver = self.mac_gyver_picture.get_rect()

    def color_blit_person(self):
        
        
        self.WINDOW = self.labyrinth.WINDOW
        self.labyrinth_entry = self.labyrinth.labyrinth_entry
        self.labyrinth_exit = self.labyrinth.labyrinth_exit

        self.guardian_picture.set_colorkey((255, 255, 255))       
        self.WINDOW.blit(self.guardian_picture, self.labyrinth_exit)
        
        self.mac_gyver_picture.set_colorkey((255, 255, 255))
        self.WINDOW.blit(self.mac_gyver_picture, self.last_location_mac_gyver_tuple)

    def color_pictures_end_game(self):
        self.grave_picture.set_colorkey((255, 255, 255))
        self.won_picture.set_colorkey((255, 255, 255))
        self.quit_picture.set_colorkey((255, 255, 255))
        self.replay_picture.set_colorkey((255, 255, 255))
                
    def init_event(self):
        
        self.objects = class_of_objects.Objects()
        self.labyrinth.blit_pictures()
        
        self.color_blit_person()

        self.objects.color_blit_objects()
        pygame.display.flip()

    def movement_right(self):
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(40, 0)
            self.last_location_mac_gyver_tuple = (key + 40, value)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key + 40] = value
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()

        if self.labyrinth.path_location().count(self.last_location_mac_gyver_tuple) == 0:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.moving_mac_gyver = self.moving_mac_gyver.move(- 40, 0)
                del self.path_traveled_mac_gyver[-1]
                self.last_location_mac_gyver_tuple = (key - 40, value)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key - 40] = value
                self.init_event()

    def movement_left(self):
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(- 40, 0)
            self.last_location_mac_gyver_tuple = (key - 40, value)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key - 40] = value
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()

        if self.labyrinth.path_location().count(self.last_location_mac_gyver_tuple) == 0:
            for key, value in self.last_location_mac_gyver_dict.items():
                del self.path_traveled_mac_gyver[-1]
                self.moving_mac_gyver = self.moving_mac_gyver.move(40, 0)
                self.last_location_mac_gyver_tuple = (key + 40, value)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key + 40] = value
                self.init_event()
                    
    def movement_up(self):
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(0, - 40)
            self.last_location_mac_gyver_tuple = (key, value - 40)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key] = value - 40
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()

        if self.labyrinth.path_location().count(self.last_location_mac_gyver_tuple) == 0:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.moving_mac_gyver = self.moving_mac_gyver.move(0, 40)
                del self.path_traveled_mac_gyver[-1]
                self.last_location_mac_gyver_tuple = (key, value + 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value + 40
                self.init_event()

    def movement_down(self):
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(0, 40)
            self.last_location_mac_gyver_tuple = (key, value + 40)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key] = value + 40
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()

        if self.labyrinth.path_location().count(self.last_location_mac_gyver_tuple) == 0:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.moving_mac_gyver = self.moving_mac_gyver.move(0, - 40)
                del self.path_traveled_mac_gyver[-1]
                self.last_location_mac_gyver_tuple = (key, value - 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value - 40
                self.init_event()

    def avoid_wall_right(self):
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(- 40, 0)
            del self.path_traveled_mac_gyver[-1]
            self.last_location_mac_gyver_tuple = (key - 40, value)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key - 40] = value
            self.init_event()

    def avoid_wall_left(self):
        for key, value in self.last_location_mac_gyver_dict.items():
            del self.path_traveled_mac_gyver[-1]
            self.moving_mac_gyver = self.moving_mac_gyver.move(40, 0)
            self.last_location_mac_gyver_tuple = (key + 40, value)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key + 40] = value
            self.init_event()

    def avoid_wall_top(self):
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(0, 40)
            del self.path_traveled_mac_gyver[-1]
            self.last_location_mac_gyver_tuple = (key, value + 40)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key] = value + 40
            self.init_event() #ne pas oublier dans fichier principal de permettre de modifier le labyrinth
        
    def avoid_wall_down(self):
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(0, - 40)
            del self.path_traveled_mac_gyver[-1]
            self.last_location_mac_gyver_tuple = (key, value - 40)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key] = value - 40
            self.init_event()

    def keep_still(self):
        column = self.labyrinth.labyrinth_exit[0]
        line = self.labyrinth.labyrinth_exit[1]
        
        # if the player arrives on the guardien, he can no longer move
        if self.last_location_mac_gyver_dict == {column, line - 40}:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.last_location_mac_gyver_tuple = (key, value + 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value + 40
                self.init_event()
        if self.path_traveled_mac_gyver.count(self.labyrinth.labyrinth_exit) == 1 \
        and self.last_location_mac_gyver_dict == {column: line + 40}:
            for key, value in self.last_location_mac_gyver_dict.items():
                del self.path_traveled_mac_gyver[-1]
                self.last_location_mac_gyver_tuple = (key, value - 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value - 40
                self.init_event()
        """if self.last_location_mac_gyver_dict == {440: - 40}:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.last_location_mac_gyver_tuple = (key, value + 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value + 40
                self.init_event()
        if self.last_location_mac_gyver_dict == {440: - 40}:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.last_location_mac_gyver_tuple = (key, value + 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value + 40
                self.init_event()"""

    """def pick_up_objects(self):
        new_objects = Objects()  #voir si on peut pas réduire les lignes
        object_1 = new_objects.object_1
        object_2 = new_objects.object_2
        object_3 = new_objects.object_3
        object_1_position = new_objects.blit_random_position()[0]
        object_2_position = new_objects.blit_random_position()[1]
        object_3_position = new_objects.blit_random_position()[2]
        # if mac gyver is passed on the neddle
        # +1 to the counter of objects and the needle disappears from the window
        if self.path_traveled_mac_gyver.count(object_1_position) == 1:
            self.counter_objects = self.counter_objects + 1
            object_1_position = self.WINDOW.blit(object_1, (600, 600))
        # if mac gyver is passed on the ether
        # +1 to the counter of objects and the ether disappears from the window
        if self.path_traveled_mac_gyver.count(object_2_position) == 1:
            self.counter_objects = self.counter_objects + 1
            object_2_position = self.WINDOW.blit(object_2, (600, 600))
        # if mac gyver is passed on the plastic_tube
        # +1 to the counter of objects and the syringe disappears from the window
        if self.path_traveled_mac_gyver.count(object_3_position) == 1:
            self.counter_objects = self.counter_objects + 1
            object_2_position = self.WINDOW.blit(object_3, (600, 600))"""



    


    
         
        




                                        


