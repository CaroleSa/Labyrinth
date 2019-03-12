#! /usr/bin/env python3
# coding: utf-8

import os
import pygame
from pygame.locals import *
from random_position import *    # j'importe le script qui permet de déterminer au hasard la position des objets en début de partie
from labyrinth_position import * # j'importe les listes qui représentent visuellement la fenêtre de jeu  
from structure import *          # j'importe le script qui colle les images en fonction du contenu des listes de labyrinth_position.py
background() 

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


def init_event():
    background()
    window.blit(guardian, (440, 0))
    window.blit(mac_gyver, (position_finale))
    window.blit(ether, ether_position)
    window.blit(needle, needle_position)
    window.blit(syringe, syringe_position)
    pygame.display.flip() 

pygame.display.flip()                                             # rafraichissement de ma fenêtre

continuer = 1
mouv_dict={0: 520}
while continuer:                                                  # permet de sortir de la denêtre avec clic droit et souris en mouvement
    for event in pygame.event.get():
        if event.type == MOUSEMOTION and event.buttons [0] == 1:
            continuer = 0
        
        if event.type == KEYDOWN and event.key == K_RIGHT:
            
            for cle, valeur in mouv_dict.items():
                
                mac_gyver_location = mac_gyver_location.move(40, 0)
                position_finale=(cle+40, valeur)  
                mouv_dict.clear()
                new_key=cle+40
                new_value=valeur
                mouv_dict[new_key]=new_value  
                background()
                window.blit(mac_gyver, (position_finale))
                window.blit(guardian, (440, 0))
                window.blit(ether, ether_position)
                window.blit(needle, needle_position)
                window.blit(syringe, syringe_position)
                pygame.display.flip()
                
                
        
        
        """if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mac_gyver_location = mac_gyver_location.move(40, 0)
                init_event(40, 520) # rafraichissement et recollage des images
            if event.key == K_LEFT:
                mac_gyver_location = mac_gyver_location.move(-40, 0)
                init_event(0, 520) # rafraichissement et recollage des images"""

