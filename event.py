#! /usr/bin/env python3
# coding: utf-8

import os
import pygame
from pygame.locals import *

pygame.init() 

os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressource")

from structure import *  # j'importe le module structure et la fonction background
                         # pour faire apparaitre ma fenêtre et mon fond d'écran

mac_gyver=pygame.image.load("MacGyver.png").convert_alpha()
gardien=pygame.image.load("gardien.png").convert_alpha()

window.blit(gardien, (440, 0))
window.blit(mac_gyver, (0, 520))
pygame.display.flip()
mac_gyver.set_colorkey((255, 255, 255))
gardien.set_colorkey((255, 255, 255))

pygame.display.flip()                                             # rafraichissement de ma fenêtre

continuer = 1
while continuer:                                                  # permet de sortir de la denêtre avec clic droit et souris en mouvement
    for event in pygame.event.get():
        if event.type == MOUSEMOTION and event.buttons [0] == 1:
            continuer = 0








