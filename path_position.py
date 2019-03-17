#! /usr/bin/env python3
# coding: utf-8

"""creation of a list of coordinates of the labyrinth path"""

from labyrinth_position import *  # import lists that visually represent the game background

# empty list that will indicate the coordinates of the labyrinth path
path_position_list = []

# we get in each line, the coordinates of the path and add it to the empty list
i = 0
for i, elt in enumerate(LINE_0):
    if elt == "6":
        path_position_list.append((i*40, 0))
for i, elt in enumerate(LINE_1):
    if elt == "6":
        path_position_list.append((i*40, 40))
for i, elt in enumerate(LINE_2):
    if elt == "6":
        path_position_list.append((i*40, 80))
for i, elt in enumerate(LINE_3):
    if elt == "6":
        path_position_list.append((i*40, 120))
for i, elt in enumerate(LINE_4):
    if elt == "6":
        path_position_list.append((i*40, 160))
for i, elt in enumerate(LINE_5):
    if elt == "6":
        path_position_list.append((i*40, 200))
for i, elt in enumerate(LINE_6):
    if elt == "6":
        path_position_list.append((i*40, 240))
for i, elt in enumerate(LINE_7):
    if elt == "6":
        path_position_list.append((i*40, 280))
for i, elt in enumerate(LINE_8):
    if elt == "6":
        path_position_list.append((i*40, 320))
for i, elt in enumerate(LINE_9):
    if elt == "6":
        path_position_list.append((i*40, 360))
for i, elt in enumerate(LINE_10):
    if elt == "6":
        path_position_list.append((i*40, 400))
for i, elt in enumerate(LINE_11):
    if elt == "6":
        path_position_list.append((i*40, 440))
for i, elt in enumerate(LINE_12):
    if elt == "6":
        path_position_list.append((i*40, 480))
for i, elt in enumerate(LINE_13):
    if elt == "6":
        path_position_list.append((i*40, 520))
for i, elt in enumerate(LINE_14):
    if elt == "6":
        path_position_list.append((i*40, 560))
i += 1
