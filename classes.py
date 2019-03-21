#! /usr/bin/env python3
# coding: utf-8

import os

from random import *  
import pygame                # import the pygame library and this module
from pygame.locals import *
pygame.init()                # initialize the pygame library

from labyrinth_list import *

os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")
WINDOW = pygame.display.set_mode((600, 600))
pygame.display.flip()
class Labyrinth:
    """ Creates the window and paste the background """
    
    def __init__(self):
        self.coordinates_number_picture_list = []

    def load_ground_picture(self):   
        # load the pictures of the wall and the ground
        self.ground_picture = pygame.image.load("ground.png").convert_alpha()
        return self.ground_picture
    
    def load_wall_top_left_picture(self):   
        # load the pictures of the wall and the ground
        self.wall_top_left_picture = pygame.image.load("top_left.png").convert_alpha()
        return self.wall_top_left_picture

    def load_wall_top_right_picture(self):   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        self.wall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        return self.wall_top_right_picture

    def load_wall_low_right_picture(self):   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        self.wall_low_right_picture = pygame.image.load("low_right.png").convert_alpha()
        return self.wall_low_right_picture

    def load_wall_low_left_picture(self):   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        self.wall_low_left_picture = pygame.image.load("low_left.png").convert_alpha()
        return self.wall_low_left_picture
        
    def load_wall_vertical_picture(self):   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
        self.wall_vertical_picture = pygame.image.load("vertical.png").convert_alpha()
        return self.wall_vertical_picture

    def load_wall_horizontal_picture(self):   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
        self.wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
        return self.wall_horizontal_picture 
    
    def decor_blit(self, line_number, index, number_picture, picture):
        for i, elt in enumerate(line_number):
            if elt == number_picture:
                self.coordinates_number_picture_list.append(((i*40), index))
        for location in self.coordinates_number_picture_list:
            WINDOW.blit(picture, (location))
    
    def call_decor_blit(self):
        # call the function with different parameters
        """for index in range(0, 600, 40):
            line_number = int(index / 40)"""
        
        """self.decor_blit(LINE_{}, {}, \"0\", self.load_wall_top_left_picture())".format(line_number, index)
        "self.decor_blit(LINE_{}, {}, \"1\", self.load_wall_top_right_picture())".format(line_number, index)
        "self.decor_blit(LINE_{}, {}, \"2\", self.load_wall_low_right_picture())".format(line_number, index)
        "self.decor_blit(LINE_{}, {}, \"3\", self.load_wall_low_left_picture())".format(line_number, index)
        "self.decor_blit(LINE_{}, {}, \"4\", self.load_wall_horizontal_picture())".format(line_number, index)
        "self.decor_blit(LINE_{}, {}, \"5\", self.load_wall_vertical_picture())".format(line_number, index)
        "self.decor_blit(LINE_{}, {}, \"6\", self.load_ground_picture())".format(line_number, index)"""     

        """self.decor_blit(LINE_0, 0, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_1, 40, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_2, 80, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_3, 120, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_4, 160, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_5, 200, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_6, 240, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_7, 280, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_8, 320, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_9, 360, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_10, 400, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_11, 440, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_12, 480, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_13, 520, "0", self.load_wall_top_left_picture())
        self.decor_blit(LINE_14, 560, "0", self.load_wall_top_left_picture())
        
        self.decor_blit(LINE_0, 0, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_1, 40, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_2, 80, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_3, 120, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_4, 160, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_5, 200, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_6, 240, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_7, 280, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_8, 320, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_9, 360, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_10, 400, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_11, 440, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_12, 480, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_13, 520, "1", self.load_wall_top_right_picture())
        self.decor_blit(LINE_14, 560, "1", self.load_wall_top_right_picture())
        
        self.decor_blit(LINE_0, 0, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_1, 40, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_2, 80, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_3, 120, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_4, 160, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_5, 200, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_6, 240, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_7, 280, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_8, 320, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_9, 360, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_10, 400, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_11, 440, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_12, 480, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_13, 520, "2", self.load_wall_low_right_picture())
        self.decor_blit(LINE_14, 560, "2", self.load_wall_low_right_picture())
        
        self.decor_blit(LINE_0, 0, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_1, 40, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_2, 80, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_3, 120, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_4, 160, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_5, 200, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_6, 240, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_7, 280, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_8, 320, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_9, 360, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_10, 400, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_11, 440, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_12, 480, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_13, 520, "5", self.load_wall_vertical_picture())
        self.decor_blit(LINE_14, 560, "5", self.load_wall_vertical_picture())
        
        self.decor_blit(LINE_0, 0, "6", self.load_ground_picture())
        self.decor_blit(LINE_1, 40, "6", self.load_ground_picture())
        self.decor_blit(LINE_2, 80, "6", self.load_ground_picture())
        self.decor_blit(LINE_3, 120, "6", self.load_ground_picture())
        self.decor_blit(LINE_4, 160, "6", self.load_ground_picture())
        self.decor_blit(LINE_5, 200, "6", self.load_ground_picture())
        self.decor_blit(LINE_6, 240, "6", self.load_ground_picture())
        self.decor_blit(LINE_7, 280, "6", self.load_ground_picture())
        self.decor_blit(LINE_8, 320, "6", self.load_ground_picture())
        self.decor_blit(LINE_9, 360, "6", self.load_ground_picture())
        self.decor_blit(LINE_10, 400, "6", self.load_ground_picture())
        self.decor_blit(LINE_11, 440, "6", self.load_ground_picture())
        self.decor_blit(LINE_12, 480, "6", self.load_ground_picture())
        self.decor_blit(LINE_13, 520, "6", self.load_ground_picture())
        self.decor_blit(LINE_14, 560, "6", self.load_ground_picture())

        self.decor_blit(LINE_0, 0, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_1, 40, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_2, 80, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_3, 120, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_4, 160, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_5, 200, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_6, 240, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_7, 280, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_8, 320, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_9, 360, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_10, 400, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_11, 440, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_12, 480, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_13, 520, "3", self.load_wall_low_left_picture())
        self.decor_blit(LINE_14, 560, "3", self.load_wall_low_left_picture())

        self.decor_blit(LINE_0, 0, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_1, 40, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_2, 80, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_3, 120, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_4, 160, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_5, 200, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_6, 240, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_7, 280, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_8, 320, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_9, 360, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_10, 400, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_11, 440, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_12, 480, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_13, 520, "4", self.load_wall_horizontal_picture())
        self.decor_blit(LINE_14, 560, "4", self.load_wall_horizontal_picture())"""

        
    """Function that pastes multiple images to create the wallpaper"""
    """Searchs each list for the coordinates of each image to paste them"""
 
class PathPosition:
    # empty list that will indicate the coordinates of the labyrinth path
    def __init__(self):
        self.path_position_list = []

    def incrementation(self):
        # we get in each line, the coordinates of the path and add it to the empty list
        # for elt in line_list... c'est surement plus simple et ca reduit le code
        for i, elt in enumerate(LINE_0):
            if elt == "6":
                self.path_position_list.append((i*40, 0))
        for i, elt in enumerate(LINE_1):
            if elt == "6":
                self.path_position_list.append((i*40, 40))
        for i, elt in enumerate(LINE_2):
            if elt == "6":
                self.path_position_list.append((i*40, 80))
        for i, elt in enumerate(LINE_3):
            if elt == "6":
                self.path_position_list.append((i*40, 120))
        for i, elt in enumerate(LINE_4):
            if elt == "6":
                self.path_position_list.append((i*40, 160))
        for i, elt in enumerate(LINE_5):
            if elt == "6":
                self.path_position_list.append((i*40, 200))
        for i, elt in enumerate(LINE_6):
            if elt == "6":
                self.path_position_list.append((i*40, 240))
        for i, elt in enumerate(LINE_7):
            if elt == "6":
                self.path_position_list.append((i*40, 280))
        for i, elt in enumerate(LINE_8):
            if elt == "6":
                self.path_position_list.append((i*40, 320))
        for i, elt in enumerate(LINE_9):
            if elt == "6":
                self.path_position_list.append((i*40, 360))
        for i, elt in enumerate(LINE_10):
            if elt == "6":
                self.path_position_list.append((i*40, 400))
        for i, elt in enumerate(LINE_11):
            if elt == "6":
                self.path_position_list.append((i*40, 440))
        for i, elt in enumerate(LINE_12):
            if elt == "6":
                self.path_position_list.append((i*40, 480))
        for i, elt in enumerate(LINE_13):
            if elt == "6":
                self.path_position_list.append((i*40, 520))
        for i, elt in enumerate(LINE_14):
            if elt == "6":
                self.path_position_list.append((i*40, 560))
        return self.path_position_list

class Objects:
    def __init__(self):

            self.line_list = [LINE_1, LINE_2, LINE_3, LINE_4, LINE_5, LINE_6, LINE_7, LINE_8,
                    LINE_9, LINE_10, LINE_11, LINE_12, LINE_13]
            self.path_position_of_random_line = []
        
    def random_position(self):
        """Class that determines a random line and a random number in this line"""
        random_line = choice(self.line_list) # determines a random line
        # add in path_position_of_random_line the path coordinates of the random list
        for i, elt in enumerate(random_line):
                if elt == "6":
                        index_random_line = self.line_list.index(random_line)
                        self.path_position_of_random_line.append(((i * 40), (index_random_line + 1) * 40))
        # determines a random coordinates
        random_location = choice(self.path_position_of_random_line)
        return random_location

    def objects_random_position(self):
        # creating variables with random coordinates for each objects
        needle_position = self.random_position()
        ether_position = self.random_position()
        plastic_tube_position = self.random_position()
                
        """# while the objects overlap, we determine a new random coordinates
        while needle_position == ether_position or ether_position == plastic_tube_position \
                or plastic_tube_position == needle_position:     
            self.objects_random_position()    
        # while the objects overlap the characters, we determine a new random coordinates
        while needle_position == (0, 520) or ether_position == (0, 520) or plastic_tube_position == (0, 520):
            self.objects_random_position()"""
                
        return needle_position, ether_position, plastic_tube_position
                        
    def objects_position(self):
        self.needle_position = self.objects_random_position()[0]
        self.ether_position = self.objects_random_position()[1]
        self.plastic_tube_position = self.objects_random_position()[2]

    def load_needle_picture(self):
        # load the picture of the needle, make the background
        # of the picture transparent and paste the picture
        self.needle_picture = pygame.image.load("needle.png").convert()
        self.needle_picture.set_colorkey((255, 255, 255))
        return self.needle_picture      
        
    def load_ether_picture(self):
        # load the picture of the ether, make the background
        # of the picture transparent and paste the picture
        self.ether_picture = pygame.image.load("ether.png").convert()
        self.ether_picture.set_colorkey((255, 255, 255))
        return self.ether_picture
                
    def load_plastic_tube_picture(self):
        # load the picture of the plastic tube, make the background
        # of the picture transparent and paste the picture
        self.plastic_tube_picture = pygame.image.load("plastic_tube.png").convert()
        self.plastic_tube_picture.set_colorkey((255, 255, 255))
        return self.plastic_tube_picture
         
    def blit_needle_picture(self):
        #if self.load_needle_picture() != None:
        self.objects_position()
        WINDOW.blit(self.load_needle_picture(), self.needle_position)
        
    def blit_ether_picture(self):
        self.objects_position()        
        WINDOW.blit(self.load_ether_picture(), self.ether_position)

    def blit_plastic_tube_picture(self):
        self.objects_position()
        WINDOW.blit(self.load_plastic_tube_picture(), self.plastic_tube_position)
    
class Person:
    def __init__(self):
        # dictionary that indicates the last position of mac gyver
        self.last_location_mac_gyver_dict = {0: 520}
        # list that indicates the coordinates of the path traveled
        # by mac gyver
        self.path_traveled_mac_gyver = [(0, 520)]
        # counter of objects
        self.counter_objects = 0

    def blit_mac_gyver_picture(self):
        # load the picture of the Mac Gyver, make the background
        # of the picture transparent and paste the picture
        self.mac_gyver_picture = pygame.image.load("MacGyver.png").convert()
        self.mac_gyver_picture.set_colorkey((255, 255, 255))
        self.moving_mac_gyver = self.mac_gyver_picture.get_rect()
        WINDOW.blit(self.mac_gyver_picture, (0, 520))
        return self.moving_mac_gyver, self.mac_gyver_picture

    def blit_guardian_picture(self):
        # load the picture of the guardian, make the background
        # of the picture transparent and paste the picture
        self.guardian_picture = pygame.image.load("guardian.png").convert()
        self.guardian_picture.set_colorkey((255, 255, 255))
        WINDOW.blit(self.guardian_picture, (440, 0))
        return self.guardian_picture

    def load_grave_picture(self):
        # load the picture of the grave and make the background
        # of the picture transparent
        self.grave_picture = pygame.image.load("grave.png").convert()
        self.grave_picture.set_colorkey((255, 255, 255))
        return self.grave_picture

    def load_won_picture(self):
        # load the picture of the won and make the background
        # of the picture transparent
        self.won_picture = pygame.image.load("won.png").convert()
        self.won_picture.set_colorkey((255, 255, 255))
        return self.won_picture

    def load_quit_picture(self):
        # load the picture of the quit and make the background
        # of the picture transparent
        self.quit_picture = pygame.image.load("quit.png").convert()
        self.quit_picture.set_colorkey((255, 255, 255))
        return self.quit_picture

    def load_replay_picture(self):
        # load the picture of the replay and make the background
        # of the picture transparent
        self.replay_picture = pygame.image.load("replay.png").convert()
        self.replay_picture.set_colorkey((255, 255, 255))
        return self.replay_picture

    def init_event(self):
        """Function that paste the pictures and refresh the screen"""
        
        """Objects.load_ether_picture(self)
        Objects.load_needle_picture(self)
        Objects.load_plastic_tube_picture(self)
        Objects.objects_random_position(self)
        Objects.objects_position(self)"""
        
        Labyrinth.call_decor_blit(self)
        self.mac_gyver_picture = self.blit_mac_gyver_picture()[1]
        WINDOW.blit(self.blit_guardian_picture(), (440, 0))
        WINDOW.blit(self.mac_gyver_picture, (self.last_location_mac_gyver_tuple))
        """WINDOW.blit(load_ether_picture(), ether_position)
        WINDOW.blit(load_needle_picture(), needle_position)
        WINDOW.blit(load_plastic_tube_picture(), plastic_tube_position)"""
        pygame.display.flip()
    
    def movement_right(self):
        for cle, valeur in self.last_location_mac_gyver_dict.items():
            """self.moving_mac_gyver = self.blit_mac_gyver_picture()[0]"""
            self.moving_mac_gyver = self.moving_mac_gyver.move(40, 0)
            self.last_location_mac_gyver_tuple = (cle + 40, valeur)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[cle + 40] = valeur
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()
            print(self.path_traveled_mac_gyver)
    