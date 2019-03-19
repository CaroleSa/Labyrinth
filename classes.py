#! /usr/bin/env python3
# coding: utf-8

""" Commands for moving Mac Gyver """

# import the pygame library and this module
import pygame
from pygame.locals import *
# initialize the pygame library
pygame.init()

# dictionary that indicates the last position of mac gyver
#last_location_mac_gyver_dict = {0: 520}
        # list that indicates the coordinates of the path traveled
        # by mac gyver
        #self.path_traveled_mac_gyver = [(0, 520)]

"""class MacGyverGoes:
    def __init__(self, column_movement, line_movement):
        for cle, valeur in last_location_mac_gyver_dict.items():
            self.moving_mac_gyver = self.moving_mac_gyver.move(column_movement, line_movement)
            self.last_location_mac_gyver_tuple = (cle + column_movement, valeur)
            self.last_location_mac_gyver_dict.clear()
            self.last_location_mac_gyver_dict[cle + column_movement] = valeur
            self.path_traveled_mac_gyver.append(self.last_location_mac_gyver_tuple)
            init_event()"""


line_number_list = [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)]
LINE_1 = [(5, 6, 6)]
path_position_list = []
for i, elt in enumerate("LINE_{}".format(1)):
    if elt == "6":
        path_position_list.append((i*40, 0))

print(path_position_list)

