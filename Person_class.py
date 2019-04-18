#! /usr/bin/env python3
# coding: UTF-8


"""class Person"""


import pygame  # import the pygame library

import maze_class # import modules of the game
import objects_class


class Person():
    """define the movements of Mac Gyver and the conditions in which mac gyver loses or wins,
    display of pictures during the game"""

    def __init__(self):
        """download pictures"""
        # instantiate the class Maze
        self.maze = maze_class.Maze()
        self.maze_entry = self.maze.maze_entry
        self.maze_exit = self.maze.maze_exit
        self.window = self.maze.window
        # instantiate the class Objects
        self.objects = objects_class.Objects()
        self.position_object_1 = self.objects.position_object_1
        self.position_object_2 = self.objects.position_object_2
        self.position_object_3 = self.objects.position_object_3
        self.object_1 = self.objects.object_1
        self.object_2 = self.objects.object_2
        self.object_3 = self.objects.object_3
        # download pictures
        self.grave_picture = pygame.image.load("grave.png").convert()
        self.replay_picture = pygame.image.load("replay.png").convert()
        self.won_picture = pygame.image.load("won.png").convert()
        self.quit_picture = pygame.image.load("quit.png").convert()
        self.guardian_picture = pygame.image.load("guardian.png").convert()
        self.mac_gyver_picture = pygame.image.load("MacGyver.png").convert()
        # dictionary that indicates the last position of mac gyver
        self.last_location_mac_gyver_dict = {self.maze_entry[0]: self.maze_entry[1]}
        # tuple that indicates the last position of mac gyver
        self.last_location_mac_gyver_tuple = self.maze_entry
        # list that indicates the coordinates of the path traveled
        # by Mac Gyver
        self.path_traveled_mac_gyver = [self.maze_entry]
        # = 1 when Mac Gyver finds the object
        self.pick_up_object_1 = 0
        self.pick_up_object_2 = 0
        self.pick_up_object_3 = 0
        # creating a rect
        self.moving_mac_gyver = self.mac_gyver_picture.get_rect()

    def color_blit_person(self):
        """transparency of the background and blit of the pictures : guardian and Mac Gyver"""
        self.guardian_picture.set_colorkey((255, 255, 255))
        self.window.blit(self.guardian_picture, self.maze_exit)
        self.mac_gyver_picture.set_colorkey((255, 255, 255))
        self.window.blit(self.mac_gyver_picture, self.last_location_mac_gyver_tuple)

    def color_pictures_end_game(self):
        """transparency of the background : pictures of the end of the game"""
        self.grave_picture.set_colorkey((255, 255, 255))
        self.won_picture.set_colorkey((255, 255, 255))
        self.quit_picture.set_colorkey((255, 255, 255))
        self.replay_picture.set_colorkey((255, 255, 255))

    def init_event(self):
        """blit after the events"""
        self.maze.blit_pictures()
        self.color_blit_person()
        self.objects.color_blit_objects()
        # refreshing
        pygame.display.flip()

    def movement_right(self):
        """Mac Gyver turns to the right, update of the list path_traveled_mac_gyver"""
        # moving of Mac Gyver and blit all pictures
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(40, 0)
            self.last_location_mac_gyver_tuple = (key + 40, value)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key + 40] = value
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()
        # Mac Gyver avoids the right wall
        if self.maze.path_location().count(self.last_location_mac_gyver_tuple) == 0:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.moving_mac_gyver = self.moving_mac_gyver.move(- 40, 0)
                del self.path_traveled_mac_gyver[-1]
                self.last_location_mac_gyver_tuple = (key - 40, value)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key - 40] = value
                self.init_event()

    def movement_left(self):
        """Mac Gyver turns to the left, update of the list path_traveled_mac_gyver"""
        # moving of Mac Gyver and blit all pictures
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(- 40, 0)
            self.last_location_mac_gyver_tuple = (key - 40, value)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key - 40] = value
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()
        # Mac Gyver avoids the left wall
        if self.maze.path_location().count(self.last_location_mac_gyver_tuple) == 0:
            for key, value in self.last_location_mac_gyver_dict.items():
                del self.path_traveled_mac_gyver[-1]
                self.moving_mac_gyver = self.moving_mac_gyver.move(40, 0)
                self.last_location_mac_gyver_tuple = (key + 40, value)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key + 40] = value
                self.init_event()

    def movement_up(self):
        """Mac Gyver goes upstairs, update of the list path_traveled_mac_gyver"""
        # moving of Mac Gyver and blit all pictures
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(0, - 40)
            self.last_location_mac_gyver_tuple = (key, value - 40)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key] = value - 40
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()
        # Mac Gyver avoids the top wall
        if self.maze.path_location().count(self.last_location_mac_gyver_tuple) == 0:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.moving_mac_gyver = self.moving_mac_gyver.move(0, 40)
                del self.path_traveled_mac_gyver[-1]
                self.last_location_mac_gyver_tuple = (key, value + 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value + 40
                self.init_event()

    def movement_down(self):
        """Mac Gyver goes downstairs, update of the list path_traveled_mac_gyver"""
        # moving of Mac Gyver and blit all pictures
        for key, value in self.last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(0, 40)
            self.last_location_mac_gyver_tuple = (key, value + 40)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[key] = value + 40
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            self.init_event()
        # Mac Gyver avoids the bottom wall
        if self.maze.path_location().count(self.last_location_mac_gyver_tuple) == 0:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.moving_mac_gyver = self.moving_mac_gyver.move(0, - 40)
                del self.path_traveled_mac_gyver[-1]
                self.last_location_mac_gyver_tuple = (key, value - 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value - 40
                self.init_event()

    def keep_still(self):
        """if Mac Gyver arrives on the guardien, he can no longer move"""
        column = self.maze.maze_exit[0]
        line = self.maze.maze_exit[1]
        # if Mac Gyver goes over the guardian
        if self.path_traveled_mac_gyver.count(self.maze_exit) == 1 \
        and self.last_location_mac_gyver_dict == {column: line - 40}:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.last_location_mac_gyver_tuple = (key, value + 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value + 40
                self.init_event()
        # if Mac Gyver goes below the guardian
        if self.path_traveled_mac_gyver.count(self.maze_exit) == 1 \
        and self.last_location_mac_gyver_dict == {column: line + 40}:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.last_location_mac_gyver_tuple = (key, value - 40)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key] = value - 40
                self.init_event()
        # if Mac Gyver goes to the right of the guardian
        if self.path_traveled_mac_gyver.count(self.maze_exit) == 1 \
        and self.last_location_mac_gyver_dict == {column + 40: line}:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.last_location_mac_gyver_tuple = (key - 40, value)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key - 40] = value
                self.init_event()
        # if Mac Gyver goes to the left of the guardian
        if self.path_traveled_mac_gyver.count(self.maze_exit) == 1 \
        and self.last_location_mac_gyver_dict == {column - 40: line}:
            for key, value in self.last_location_mac_gyver_dict.items():
                self.last_location_mac_gyver_tuple = (key + 40, value)
                self.last_location_mac_gyver_dict.clear()
                self.last_location_mac_gyver_dict[key + 40] = value
                self.init_event()

    def pick_up_objects(self):
        """Mac Gyver takes objects"""
        # if mac gyver takes the object 1
        # initialization of the object counter and the object 1 disappears from the window
        if self.last_location_mac_gyver_tuple == self.position_object_1:
            self.pick_up_object_1 = 1
            self.objects.disappearance_object_1()
        # if mac gyver takes the object 2
        # initialization of the object counter and the object 2 disappears from the window
        if self.last_location_mac_gyver_tuple == self.position_object_2:
            self.pick_up_object_2 = 1
            self.objects.disappearance_object_2()
        # if mac gyver takes the object 3
        # initialization of the object counter and the object 3 disappears from the window
        if self.last_location_mac_gyver_tuple == self.position_object_3:
            self.pick_up_object_3 = 1
            self.objects.disappearance_object_3()
        # the objects counter
        self.counter_objects = self.pick_up_object_1 + self.pick_up_object_2 + self.pick_up_object_3

    def lost(self):
        """if Mac Gyver loses, blit pictures"""
        lost = 1
        if self.last_location_mac_gyver_tuple == self.maze_exit and self.counter_objects != 3:
            self.maze.blit_pictures()
            self.guardian_picture.set_colorkey((255, 255, 255))
            self.window.blit(self.guardian_picture, self.maze_exit)
            self.color_pictures_end_game()
            self.window.blit(self.grave_picture, (200, 200))
            self.window.blit(self.replay_picture, (0, 520))
            self.window.blit(self.quit_picture, (520, 520))
            pygame.display.flip()
            return lost

    def won(self):
        """if Mac Gyver wins, blit pictures"""
        won = 1
        if self.last_location_mac_gyver_tuple == self.maze_exit and self.counter_objects == 3:
            self.maze.blit_pictures()
            self.color_pictures_end_game()
            self.window.blit(self.won_picture, (120, 120))
            pygame.display.flip()
            return won
