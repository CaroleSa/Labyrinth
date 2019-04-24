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
        # tuple that indicates the last position of mac gyver
        self.location_mac_gyver = self.maze_entry
        # = 1 indicates that Mac Gyver has arrived at the end of the maze
        self.exit = 0
        # = 1 indicates that Mac Gyver finds the object
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
        self.window.blit(self.mac_gyver_picture, self.location_mac_gyver)

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

    def movement(self, x, y):
        """Mac Gyver moves and avoids the walls"""
        # Mac Gyver moves
        column = self.location_mac_gyver[0]
        line = self.location_mac_gyver[1]
        self.location_mac_gyver = (column + x, line + y)
        # Mac Gyver avoids the right wall
        if self.maze.path_location().count(self.location_mac_gyver) == 0:
            self.location_mac_gyver = (column, line)     
        else:
            self.moving_mac_gyver = self.moving_mac_gyver.move(x, y)
        self.init_event()

    def keep_still(self, x, y):
        """if Mac Gyver arrives on the guardien, he can no longer move"""
        column_exit = self.maze.maze_exit[0]
        line_exit = self.maze.maze_exit[1]
        column = self.location_mac_gyver[0]
        line = self.location_mac_gyver[1]
        if self.location_mac_gyver == self.maze_exit:
            self.exit = 1
        if self.exit == 1 and self.location_mac_gyver == (column_exit + x, line_exit + y):
            self.location_mac_gyver = (column - x, line - y)
            self.init_event()

    def pick_up_objects(self):
        """Mac Gyver takes objects"""
        # if mac gyver takes the object 1
        # initialization of the object counter and the object 1 disappears from the window
        if self.location_mac_gyver == self.position_object_1:
            self.pick_up_object_1 = 1
            self.objects.disappearance_object_1()
        # if mac gyver takes the object 2
        # initialization of the object counter and the object 2 disappears from the window
        if self.location_mac_gyver == self.position_object_2:
            self.pick_up_object_2 = 1
            self.objects.disappearance_object_2()
        # if mac gyver takes the object 3
        # initialization of the object counter and the object 3 disappears from the window
        if self.location_mac_gyver == self.position_object_3:
            self.pick_up_object_3 = 1
            self.objects.disappearance_object_3()
        # the objects counter
        self.counter_objects = self.pick_up_object_1 + self.pick_up_object_2 + self.pick_up_object_3

    def lost(self):
        """if Mac Gyver loses, blit pictures"""
        lost = 1
        if self.location_mac_gyver == self.maze_exit and self.counter_objects != 3:
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
        if self.location_mac_gyver == self.maze_exit and self.counter_objects == 3:
            self.maze.blit_pictures()
            self.color_pictures_end_game()
            self.window.blit(self.won_picture, (120, 120))
            pygame.display.flip()
            return won
