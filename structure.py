#! /usr/bin/env python3
# coding: utf-8

import os
import pygame

from pygame.locals import *

pygame.init() 
"""initialise le module"""

def background():
    """Script qui permet de réunir plusieurs images 
    afin de créer et d'afficher le fond d'écran"""

    os.chdir("C:/Users/Carole/program_python/program/labyrinth/ressource")

    window = pygame.display.set_mode((600, 600)) 

    wall_top_left = pygame.image.load("top_left.png").convert_alpha()
    wall_top_right = pygame.image.load("top_right.png").convert_alpha()
    wall_low_right = pygame.image.load("low_right.png").convert_alpha()
    wall_low_left = pygame.image.load("low_left.png").convert_alpha()
    wall_horizontal = pygame.image.load("horizontal.png").convert_alpha()
    wall_vertical = pygame.image.load("vertical.png").convert_alpha()
    """Téléchargement des images de fond"""
    
    line_0 =  ["0","4","4","4","4","4","4","4","4","4","2"," ","3","4","1"]
    line_1 =  ["5"," "," "," "," "," "," "," "," "," "," "," "," "," ","5"]
    line_2 =  ["5"," ","0","4","4","4","4","4","4","4","4","4","4","4","5"]
    line_3 =  ["5"," ","5"," "," "," "," "," "," "," ","5"," "," "," ","5"]
    line_4 =  ["5"," ","5"," ","0","4","4"," ","4","4","4","4","1"," ","5"]
    line_5 =  ["5"," ","5"," ","5"," "," "," "," "," "," "," ","5"," ","5"]
    line_6 =  ["5"," ","5"," ","5"," ","0","4","4","4","4"," ","5"," ","5"]
    line_7 =  ["5"," ","5"," ","5"," ","5"," "," "," "," "," "," "," ","5"]
    line_8 =  ["5"," ","5"," ","5"," ","5"," ","5"," ","4","4","4","4","5"]
    line_9 =  ["5"," "," "," ","5"," ","5"," ","5"," "," "," "," "," ","5"]
    line_10 = ["5"," ","5"," ","5"," ","5"," ","5","4","4","4","4"," ","5"]
    line_11 = ["5"," ","5"," ","5"," ","5"," ","5"," ","5"," "," "," ","5"]
    line_12 = ["3","4","4","4","4","4","2"," ","5"," ","3","4","4","4","5"]
    line_13 = [" "," "," "," "," "," "," "," "," "," "," "," "," "," ","5"]
    line_14 = ["4","4","4","4","4","4","4","4","4","4","4","4","4","4","2"]
    
    
    def wall_location(line_number, index, number_picture, picture):
        """fonction qui permet d'appliquer les informations des lines ci-dessus afin
        de bliter les images sur la fond d'écran :
        ces lignes forment un visuel du fond d'écran, et nous pouvons ainsi indiquer
        quelles images nous souhaitons positionner à tel endroit (number_picture):
        0 pour wall top left
        1 pour wall top right
        2 pour wall low right
        3 pour wall low left
        4 pour wall horizontal
        5 pour wall vertical"""
        line_finale=[]
        i=0
        for i, elt in enumerate(line_number):
            if elt == number_picture:
                line_finale.append(((i*40), index))
        i+=1
        print(line_finale)
        for location in line_finale:
            window.blit(picture, (location))
    
    wall_location(line_0, 0, "0", wall_top_left)
    wall_location(line_1, 40, "0", wall_top_left)
    wall_location(line_2, 80, "0", wall_top_left)
    wall_location(line_3, 120, "0", wall_top_left)
    wall_location(line_4, 160, "0", wall_top_left)
    wall_location(line_5, 200, "0", wall_top_left)
    wall_location(line_6, 240, "0", wall_top_left)
    wall_location(line_7, 280, "0", wall_top_left)
    wall_location(line_8, 320, "0", wall_top_left)
    wall_location(line_9, 360, "0", wall_top_left)
    wall_location(line_10, 400, "0", wall_top_left)
    wall_location(line_11, 440, "0", wall_top_left)
    wall_location(line_12, 480, "0", wall_top_left)
    wall_location(line_13, 520, "0", wall_top_left)
    wall_location(line_14, 560, "0", wall_top_left)

    wall_location(line_0, 0, "1", wall_top_right)
    wall_location(line_1, 40, "1", wall_top_right)
    wall_location(line_2, 80, "1", wall_top_right)
    wall_location(line_3, 120, "1", wall_top_right)
    wall_location(line_4, 160, "1", wall_top_right)
    wall_location(line_5, 200, "1", wall_top_right)
    wall_location(line_6, 240, "1", wall_top_right)
    wall_location(line_7, 280, "1", wall_top_right)
    wall_location(line_8, 320, "1", wall_top_right)
    wall_location(line_9, 360, "1", wall_top_right)
    wall_location(line_10, 400, "1", wall_top_right)
    wall_location(line_11, 440, "1", wall_top_right)
    wall_location(line_12, 480, "1", wall_top_right)
    wall_location(line_13, 520, "1", wall_top_right)
    wall_location(line_14, 560, "1", wall_top_right)

    wall_location(line_0, 0, "2", wall_low_right)
    wall_location(line_1, 40, "2", wall_low_right)
    wall_location(line_2, 80, "2", wall_low_right)
    wall_location(line_3, 120, "2", wall_low_right)
    wall_location(line_4, 160, "2", wall_low_right)
    wall_location(line_5, 200, "2", wall_low_right)
    wall_location(line_6, 240, "2", wall_low_right)
    wall_location(line_7, 280, "2", wall_low_right)
    wall_location(line_8, 320, "2", wall_low_right)
    wall_location(line_9, 360, "2", wall_low_right)
    wall_location(line_10, 400, "2", wall_low_right)
    wall_location(line_11, 440, "2", wall_low_right)
    wall_location(line_12, 480, "2", wall_low_right)
    wall_location(line_13, 520, "2", wall_low_right)
    wall_location(line_14, 560, "2", wall_low_right)

    wall_location(line_0, 0, "3", wall_low_left)
    wall_location(line_1, 40, "3", wall_low_left)
    wall_location(line_2, 80, "3", wall_low_left)
    wall_location(line_3, 120, "3", wall_low_left)
    wall_location(line_4, 160, "3", wall_low_left)
    wall_location(line_5, 200, "3", wall_low_left)
    wall_location(line_6, 240, "3", wall_low_left)
    wall_location(line_7, 280, "3", wall_low_left)
    wall_location(line_8, 320, "3", wall_low_left)
    wall_location(line_9, 360, "3", wall_low_left)
    wall_location(line_10, 400, "3", wall_low_left)
    wall_location(line_11, 440, "3", wall_low_left)
    wall_location(line_12, 480, "3", wall_low_left)
    wall_location(line_13, 520, "3", wall_low_left)
    wall_location(line_14, 560, "3", wall_low_left)

    wall_location(line_0, 0, "4", wall_horizontal)
    wall_location(line_1, 40, "4", wall_horizontal)
    wall_location(line_2, 80, "4", wall_horizontal)
    wall_location(line_3, 120, "4", wall_horizontal)
    wall_location(line_4, 160, "4", wall_horizontal)
    wall_location(line_5, 200, "4", wall_horizontal)
    wall_location(line_6, 240, "4", wall_horizontal)
    wall_location(line_7, 280, "4", wall_horizontal)
    wall_location(line_8, 320, "4", wall_horizontal)
    wall_location(line_9, 360, "4", wall_horizontal)
    wall_location(line_10, 400, "4", wall_horizontal)
    wall_location(line_11, 440, "4", wall_horizontal)
    wall_location(line_12, 480, "4", wall_horizontal)
    wall_location(line_13, 520, "4", wall_horizontal)
    wall_location(line_14, 560, "4", wall_horizontal)

    wall_location(line_0, 0, "5", wall_vertical)
    wall_location(line_1, 40, "5", wall_vertical)
    wall_location(line_2, 80, "5", wall_vertical)
    wall_location(line_3, 120, "5", wall_vertical)
    wall_location(line_4, 160, "5", wall_vertical)
    wall_location(line_5, 200, "5", wall_vertical)
    wall_location(line_6, 240, "5", wall_vertical)
    wall_location(line_7, 280, "5", wall_vertical)
    wall_location(line_8, 320, "5", wall_vertical)
    wall_location(line_9, 360, "5", wall_vertical)
    wall_location(line_10, 400, "5", wall_vertical)
    wall_location(line_11, 440, "5", wall_vertical)
    wall_location(line_12, 480, "5", wall_vertical)
    wall_location(line_13, 520, "5", wall_vertical)
    wall_location(line_14, 560, "5", wall_vertical)

    
    pygame.display.flip()

    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == MOUSEMOTION and event.buttons [0] == 1:
                continuer = 0





background()
        







