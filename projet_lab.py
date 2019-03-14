#! /usr/bin/env python3
# coding: utf-8

import os
import pygame
from pygame.locals import *
from random_position import *    # j'importe le script qui permet de déterminer au hasard la position des objets en début de partie
from labyrinth_position import * # j'importe les listes qui représentent visuellement la fenêtre de jeu  
from structure import *          # j'importe le script qui colle les images en fonction du contenu des listes de labyrinth_position.py
background() 
from path import *

pygame.init()  # j'initialise le module pygame

os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressource") # j'indique le chemin de mes images

mac_gyver=pygame.image.load("MacGyver.png").convert()  # je charge mon image dans mon script
mac_gyver.set_colorkey((255,255,255))                  # je rends le fond de l'image transparente
mac_gyver_location=mac_gyver.get_rect()                # j'indique que l'image serra en mouvement par la suite
window.blit(mac_gyver, (0, 520))                       # j'indique l'emplacement de départ de l'image

guardian=pygame.image.load("guardian.png").convert()
guardian.set_colorkey((255,255,255))
guardian_position=window.blit(guardian, (440, 0))

needle=pygame.image.load("needle.png").convert()
needle.set_colorkey((255,255,255))
window.blit(needle, needle_position)

ether=pygame.image.load("ether.png").convert_alpha()
ether.set_colorkey((0,0,0))
window.blit(ether, ether_position)

syringe=pygame.image.load("syringe.png").convert()
syringe.set_colorkey((255,255,255))
window.blit(syringe, syringe_position)

grave=pygame.image.load("grave.png").convert()
grave.set_colorkey((255,255,255))

won=pygame.image.load("won.png").convert()
won.set_colorkey((255,255,255))

def init_event():

    background()
    window.blit(guardian, (440, 0))
    window.blit(mac_gyver, (position_finale))
    window.blit(ether, ether_position)
    window.blit(needle, needle_position)
    window.blit(syringe, syringe_position)
    pygame.display.flip()

    if path_position.count(position_finale) == 1:
        print("chemin")
    else:
        print("mur")
        
    
  
pygame.display.flip()                                             # rafraichissement de ma fenêtre

continuer = 1
mouv_dict = {0: 520}
path_traveled = [(0, 520)]
counter_objects = 0
while continuer:                                                  # permet de sortir de la denêtre avec clic droit et souris en mouvement
    for event in pygame.event.get():
        if mouv_dict == {440: 0} and counter_objects == 3:
            background()
            window.blit(ether, ether_position)
            window.blit(needle, needle_position)
            window.blit(syringe, syringe_position)
            window.blit(won, (120, 120))
            pygame.display.flip()
            continuer = 0
        if event.type == KEYDOWN and event.key == K_RIGHT:
            for cle, valeur in mouv_dict.items():
                mac_gyver_location = mac_gyver_location.move(40, 0)
                position_finale=(cle+40, valeur)  
                mouv_dict.clear()
                mouv_dict[cle+40]=valeur
                init_event()
        if event.type == KEYDOWN and event.key == K_LEFT:
            for cle, valeur in mouv_dict.items():
                mac_gyver_location = mac_gyver_location.move(-40, 0)
                position_finale=(cle-40, valeur)  
                mouv_dict.clear()
                mouv_dict[cle-40]=valeur
                init_event()  
        if event.type == KEYDOWN and event.key == K_UP:
            for cle, valeur in mouv_dict.items():
                mac_gyver_location = mac_gyver_location.move(0, -40)
                position_finale=(cle, valeur-40)  
                mouv_dict.clear()
                mouv_dict[cle]=valeur-40
                init_event()  
        if event.type == KEYDOWN and event.key == K_DOWN:
            for cle, valeur in mouv_dict.items():
                mac_gyver_location = mac_gyver_location.move(0, 40)
                position_finale=(cle, valeur+40)  
                mouv_dict.clear()
                mouv_dict[cle]=valeur+40
                init_event()
        if event.type == KEYDOWN:
            path_traveled.append(position_finale)
        while event.type == KEYDOWN and event.key == K_DOWN and path_position.count(position_finale) == 0:
            for cle, valeur in mouv_dict.items():
                mac_gyver_location = mac_gyver_location.move(0, -40)
                position_finale=(cle, valeur-40)  
                mouv_dict.clear()
                mouv_dict[cle]=valeur-40
                init_event()
        while event.type == KEYDOWN and event.key == K_UP and path_position.count(position_finale) == 0:
            for cle, valeur in mouv_dict.items():
                mac_gyver_location = mac_gyver_location.move(0, 40)
                position_finale=(cle, valeur+40)  
                mouv_dict.clear()
                mouv_dict[cle]=valeur+40
                init_event()
        while event.type == KEYDOWN and event.key == K_RIGHT and path_position.count(position_finale) == 0:
            for cle, valeur in mouv_dict.items():
                mac_gyver_location = mac_gyver_location.move(-40, 0)
                position_finale=(cle-40, valeur)  
                mouv_dict.clear()
                mouv_dict[cle-40]=valeur
                init_event()
        while event.type == KEYDOWN and event.key == K_LEFT and path_position.count(position_finale) == 0:
            for cle, valeur in mouv_dict.items():
                mac_gyver_location = mac_gyver_location.move(40, 0)
                position_finale=(cle+40, valeur)  
                mouv_dict.clear()
                mouv_dict[cle+40]=valeur
                init_event()
        if path_traveled.count(needle_position) == 1:
            counter_objects=counter_objects+1
            needle_position=window.blit(needle, (600, 600))
        if path_traveled.count(ether_position) == 1:
            counter_objects=counter_objects+1
            ether_position=window.blit(ether, (600, 600))
        if path_traveled.count(syringe_position) == 1:
            counter_objects=counter_objects+1
            syringe_position=window.blit(syringe, (600, 600))
        if mouv_dict == {440: 0} and counter_objects != 3:
            background()
            window.blit(ether, ether_position)
            window.blit(needle, needle_position)
            window.blit(syringe, syringe_position)
            window.blit(guardian, (440, 0))
            window.blit(mac_gyver, (position_finale))
            window.blit(grave, (200, 200))
            pygame.display.flip()
        

#eviter les murs et recommencer programme si il perd    , objet doit etre different de position mc gyver   




             
                
            
    

             
                
            
    











