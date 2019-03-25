#! /usr/bin/env python3
# coding: UTF-8 je garde

import os

import random
# import the pygame library and this module
import pygame
from pygame.locals import *
# initialize the pygame library
pygame.init()

class Labyrinth:

    def __init__(self):

        os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")
        self.LABYRINTH_LIST = [
        [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 6, 3, 4, 1],
        [5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5],
        [5, 6, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
        [5, 6, 5, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 5],
        [5, 6, 5, 6, 0, 4, 4, 6, 4, 4, 4, 4, 1, 6, 5],
        [5, 6, 5, 6, 5, 6, 6, 6, 6, 6, 6, 6, 5, 6, 5],
        [5, 6, 5, 6, 5, 6, 0, 4, 4, 4, 4, 6, 5, 6, 5],
        [5, 6, 5, 6, 5, 6, 5, 6, 6, 6, 6, 6, 6, 6, 5],
        [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4, 4, 4, 4, 5],
        [5, 6, 6, 6, 5, 6, 5, 6, 5, 6, 6, 6, 6, 6, 5],
        [5, 6, 5, 6, 5, 6, 5, 6, 5, 4, 4, 4, 4, 6, 5],
        [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 6, 6, 5],
        [3, 4, 4, 4, 4, 4, 2, 6, 5, 6, 3, 4, 4, 4, 5],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2]]

        # creates the window    
        self.WINDOW = pygame.display.set_mode((600, 600))

        self.ground_picture = pygame.image.load("ground.png").convert_alpha()
        self.wall_top_left_picture = pygame.image.load("top_left.png").convert_alpha()
        self.wall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        self.wall_low_right_picture = pygame.image.load("low_right.png").convert_alpha()
        self.wall_low_left_picture = pygame.image.load("low_left.png").convert_alpha()
        self.wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
        self.wall_vertical_picture = pygame.image.load("vertical.png").convert_alpha()
                
        self.PICTURE_LIST = [self.wall_top_left_picture, self.wall_top_right_picture, self.wall_low_right_picture, 
        self.wall_low_left_picture, self.wall_horizontal_picture, self.wall_vertical_picture, self.ground_picture]
        # empty list that will indicate the coordinates of the labyrinth path
                
        self.path_position_list = []

        self.labyrinth_entry = (0, 520)

        self.labyrinth_exit = (440, 0)

    def blit_pictures(self):
        """Searchs each list for the coordinates of each image to paste them"""
        for i, elt in enumerate(self.LABYRINTH_LIST):
            for y, number in enumerate(elt):
                picture = self.PICTURE_LIST[number]
                location = (y*40, i*40)
                self.WINDOW.blit(picture, location)

    def path_location(self): 
        for i, elt in enumerate(self.LABYRINTH_LIST):
            for y, number in enumerate(elt):
                if number == 6:
                    self.path_position_list.append((y*40, i*40))
        return self.path_position_list

class Objects:

    def __init__(self):
        self.WINDOW = Labyrinth().WINDOW
        os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")
        self.object_1 = pygame.image.load("needle.png").convert()
        self.object_2 = pygame.image.load("ether.png").convert()
        self.object_3 = pygame.image.load("plastic_tube.png").convert()

    def random_position(self):
        self.labyrinth_entry = Labyrinth().labyrinth_entry
        self.labyrinth_exit = Labyrinth().labyrinth_exit
        self.path_location = Labyrinth().path_location()

        self.path_location.remove(Labyrinth().labyrinth_entry)
        self.path_location.remove(Labyrinth().labyrinth_exit)
        self.list_random_position = random.sample(self.path_location, 3)
        return self.list_random_position
   
    def color_blit_objects(self):
        self.WINDOW = Labyrinth().WINDOW
        self.object_1.set_colorkey((255, 255, 255))
        self.object_2.set_colorkey((255, 255, 255))
        self.object_3.set_colorkey((255, 255, 255))

        self.WINDOW.blit(self.object_1, self.random_position()[0])
        self.WINDOW.blit(self.object_2, self.random_position()[1])
        self.WINDOW.blit(self.object_3, self.random_position()[2])

class Person(Labyrinth):

    def __init__(self):
        self.WINDOW = Labyrinth().WINDOW
        self.labyrinth_entry = Labyrinth().labyrinth_entry
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

    def color(self):
        self.grave_picture.set_colorkey((255, 255, 255))
        self.won_picture.set_colorkey((255, 255, 255))
        self.quit_picture.set_colorkey((255, 255, 255))
        self.replay_picture.set_colorkey((255, 255, 255))

    def mac_gyver_move(self):
        self.moving_mac_gyver = self.mac_gyver_picture.get_rect()
        return self.moving_mac_gyver
                
    def init_event(self):
        self.WINDOW = Labyrinth().WINDOW

        Labyrinth().blit_pictures()
        new_objects = Objects()
        new_objects.color_blit_objects()

        self.labyrinth_entry = Labyrinth().labyrinth_entry
        self.labyrinth_exit = Labyrinth().labyrinth_exit
        
        self.guardian_picture.set_colorkey((255, 255, 255))       
        self.WINDOW.blit(self.guardian_picture, self.labyrinth_exit)
        
        self.mac_gyver_picture.set_colorkey((255, 255, 255))
        self.WINDOW.blit(self.mac_gyver_picture, self.last_location_mac_gyver_tuple)

        


        pygame.display.flip()

    def movement_right(self):
        self.moving_mac_gyver = self.mac_gyver_move()

        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(40, 0)
            self.last_location_mac_gyver_tuple = (key + 40, value)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key + 40] = value
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()
            print(self.last_location_mac_gyver_dict)

    def movement_left(self):
        self.moving_mac_gyver = self.mac_gyver_move()

        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(- 40, 0)
            self.last_location_mac_gyver_tuple = (key - 40, value)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key - 40] = value
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()
                    
    def movement_up(self):
        self.moving_mac_gyver = self.mac_gyver_move()

        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(0, - 40)
            self.last_location_mac_gyver_tuple = (key, value - 40)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key] = value - 40
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()

    def movement_down(self):
        self.moving_mac_gyver = self.mac_gyver_move()

        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(0, 40)
            self.last_location_mac_gyver_tuple = (key, value + 40)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key] = value + 40
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()

    """def avoid_wall_right(self):
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
        new_labyrinth = Labyrinth()
        exit_location = new_labyrinth.labyrinth_exit
        column = exit_location[0]
        line = exit_location[1]  #a tout revoir car l'idée et de pouvoir modif la localisation de la sortie
        # if the player arrives on the guardien, he can no longer move
        if self.last_location_mac_gyver_dict == {440: - 40}:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.last_location_mac_gyver_tuple = (cle, valeur + 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[cle] = valeur + 40
                init_event()
        if self.path_traveled_mac_gyver.count((440, 0)) == 1 \
        and self.last_location_mac_gyver_dict == {440: 40}:
            for key, value in self.last_location_mac_gyver_dict.items():
                del self.path_traveled_mac_gyver[-1]
                self.last_location_mac_gyver_tuple = (cle, valeur - 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[cle] = valeur - 40
                init_event()

    def pick_up_objects(self):
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



    


    
         
        

"""new_labyrinth = Labyrinth()
new_labyrinth.blit_pictures()
new_labyrinth.path_location()"""
"""new_objects = Objects("needle.png", "ether.png", "plastic_tube.png")
new_objects.random_position()
new_objects.color_blit_objects()"""
"""Person().init_event()
Person().person_color_blit()
Person().movement_right()"""



                                        


