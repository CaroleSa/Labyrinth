#! /usr/bin/env python3
# coding: utf-8

import os
import pygame

from pygame.locals import *
pygame.init() 

os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressource")

from structure import *

pygame.display.flip()

mac_gyver=pygame.image.load("MacGyver.png").convert_alpha()
gardien=pygame.image.load("gardien.png").convert_alpha()
window.blit(gardien, (440, 0))
window.blit(MacGyver, (0, 520))

pygame.display.flip()

