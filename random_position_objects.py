import os
from random import *
import pygame
from pygame.locals import *
from labyrinth_position import *

pygame.init() 


class random_position:
    def __init__(self):
        line_list = [line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8,
             line_9, line_10, line_11, line_12, line_13
]
        path_position_of_random_line=[]
        
        random_line = choice(line_list)
        i=0             # i : notre compteur
        for i, elt in enumerate(random_line):     # va permettre de parcourir tous les élèments de la ligne définie dans les paramètres 
            if elt == "6": 
                index_random_line = line_list.index(random_line)                  # si un des élèments correspond au number_picture demandé,
                path_position_of_random_line.append(((i * 40), (index_random_line + 1) * 40))     # les coordonnées de son emplacement s'ajoute à ma liste vide
        self.random_location = choice(path_position_of_random_line)
        i+=1  
       
needle_location = random_position()
ether_location = random_position()
syringe_location = random_position()
needle_position = needle_location.random_location
ether_position = ether_location.random_location
syringe_position = syringe_location.random_location

while needle_position == ether_position or ether_position == syringe_position or syringe_position == needle_position:
    needle_location = random_position()
    ether_location = random_position()
    syringe_location = random_position()
    needle_position = needle_location.random_location
    ether_position = ether_location.random_location
    syringe_position = syringe_location.random_location
    
while needle_position == (0,520) or ether_position == (0,520) or syringe_position == (0,520):
    needle_location = random_position()
    ether_location = random_position()
    syringe_location = random_position()
    needle_position = needle_location.random_location
    ether_position = ether_location.random_location
    syringe_position = syringe_location.random_location