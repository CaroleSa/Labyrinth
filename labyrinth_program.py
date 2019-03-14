#! /usr/bin/env python3
# coding: utf-8

import os
import pygame
from pygame.locals import *
from labyrinth_position import * # j'importe les listes qui représentent visuellement la fenêtre de jeu  
from structure import *          # j'importe le script qui colle les images en fonction du contenu des listes de labyrinth_position.py
blit_background() 
from random_position_objects import *    # j'importe le script qui permet de déterminer au hasard la position des objets en début de partie
from path_position import *

pygame.init()  # j'initialise le module pygame

os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressource") # j'indique le chemin de mes images

mac_gyver_picture = pygame.image.load("MacGyver.png").convert()  # je charge mon image dans mon script
mac_gyver_picture.set_colorkey((255, 255, 255))                  # je rends le fond de l'image transparente
moving_mac_gyver = mac_gyver_picture.get_rect()                # j'indique que l'image serra en mouvement par la suite
window.blit(mac_gyver_picture, (0, 520))                       # j'indique l'emplacement de départ de l'image

guardian_picture = pygame.image.load("guardian.png").convert()
guardian_picture.set_colorkey((255, 255, 255))
window.blit(guardian_picture, (440, 0))

needle_picture = pygame.image.load("needle.png").convert()
needle_picture.set_colorkey((255, 255, 255))
window.blit(needle_picture, needle_position)

ether_picture = pygame.image.load("ether.png").convert_alpha()
ether_picture.set_colorkey((0, 0, 0))
window.blit(ether_picture, ether_position)

syringe_picture = pygame.image.load("syringe.png").convert()
syringe_picture.set_colorkey((255, 255, 255))
window.blit(syringe_picture, syringe_position)

grave_picture = pygame.image.load("grave.png").convert()
grave_picture.set_colorkey((255, 255, 255))

won_picture = pygame.image.load("won.png").convert()
won_picture.set_colorkey((255, 255, 255))

pygame.display.flip() 

def init_event():
    blit_background()
    window.blit(guardian_picture, (440, 0))
    window.blit(mac_gyver_picture, (last_location_mac_gyver_tuple))
    window.blit(ether_picture, ether_position)
    window.blit(needle_picture, needle_position)
    window.blit(syringe_picture, syringe_position)
    pygame.display.flip()

play = 1
last_location_mac_gyver_dict = {0: 520}
path_traveled_mac_gyver = [(0, 520)]
counter_objects = 0

while play:                                                  # permet de sortir de la denêtre avec clic droit et souris en mouvement
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_RIGHT:
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(40, 0)
                last_location_mac_gyver_tuple = (cle + 40, valeur)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle + 40]=valeur
                init_event()
        if event.type == KEYDOWN and event.key == K_LEFT:
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(- 40, 0)
                last_location_mac_gyver_tuple = (cle - 40, valeur)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle - 40] = valeur
                init_event()  
        if event.type == KEYDOWN and event.key == K_UP:
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(0, - 40)
                last_location_mac_gyver_tuple = (cle, valeur - 40)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle] = valeur- 40
                init_event()  
        if event.type == KEYDOWN and event.key == K_DOWN:
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(0, 40)
                last_location_mac_gyver_tuple = (cle, valeur + 40)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle] = valeur + 40
                init_event()
        if event.type == KEYDOWN:
            path_traveled_mac_gyver.append(last_location_mac_gyver_tuple)
        while event.type == KEYDOWN and event.key == K_DOWN and path_position.count(last_location_mac_gyver_tuple) == 0:
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(0, - 40)
                last_location_mac_gyver_tuple = (cle, valeur - 40)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle] = valeur - 40
                init_event()
        while event.type == KEYDOWN and event.key == K_UP and path_position.count(last_location_mac_gyver_tuple) == 0:
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(0, 40)
                last_location_mac_gyver_tuple = (cle, valeur + 40)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle] = valeur + 40
                init_event()
        while event.type == KEYDOWN and event.key == K_RIGHT and path_position.count(last_location_mac_gyver_tuple) == 0:
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(- 40, 0)
                last_location_mac_gyver_tuple = (cle - 40, valeur)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle - 40] = valeur
                init_event()
        while event.type == KEYDOWN and event.key == K_LEFT and path_position.count(last_location_mac_gyver_tuple) == 0:
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(40, 0)
                last_location_mac_gyver_tuple = (cle + 40, valeur)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle + 40] = valeur
                init_event()
        if path_traveled_mac_gyver.count(needle_position) == 1:
            counter_objects = counter_objects + 1
            needle_position = window.blit(needle_picture, (600, 600))
        if path_traveled_mac_gyver.count(ether_position) == 1:
            counter_objects = counter_objects + 1
            ether_position = window.blit(ether_picture, (600, 600))
        if path_traveled_mac_gyver.count(syringe_position) == 1:
            counter_objects = counter_objects + 1
            syringe_position = window.blit(syringe_picture, (600, 600))
        if path_traveled_mac_gyver.count((440, 0)) == 1 and counter_objects != 3:
            blit_background()
            window.blit(ether_picture, ether_position)
            window.blit(needle_picture, needle_position)
            window.blit(syringe_picture, syringe_position)
            window.blit(guardian_picture, (440, 0))
            window.blit(mac_gyver_picture, (last_location_mac_gyver_tuple))
            window.blit(grave_picture, (200, 200))
            pygame.display.flip()
        if last_location_mac_gyver_dict == {440: 0} and counter_objects == 3:
            blit_background()
            window.blit(ether_picture, ether_position)
            window.blit(needle_picture, needle_position)
            window.blit(syringe_picture, syringe_position)
            window.blit(won_picture, (120, 120))
            pygame.display.flip()
            play = 0
        

  




             
                
            
    

             
                
            
    











