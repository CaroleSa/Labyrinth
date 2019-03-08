#! /usr/bin/env python3
# coding: utf-8

import os
import pygame
from pygame.locals import *

pygame.init() 

os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressource")

from structure import *  # j'importe le module structure et la fonction background
                         # pour faire apparaitre ma fenêtre et mon fond d'écran

mac_gyver=pygame.image.load("MacGyver.png").convert()
mac_gyver.set_colorkey((255,255,255))
window.blit(mac_gyver, (0, 520))
mac_gyver_location=mac_gyver.get_rect()

guardian=pygame.image.load("guardian.png").convert()
guardian.set_colorkey((255,255,255))
window.blit(guardian, (440, 0))
guardian_location=guardian.get_rect()

pygame.display.flip()                                             # rafraichissement de ma fenêtre

continuer = 1
while continuer:                                                  # permet de sortir de la denêtre avec clic droit et souris en mouvement
    for event in pygame.event.get():
        if event.type == MOUSEMOTION and event.buttons [0] == 1:
            continuer = 0








