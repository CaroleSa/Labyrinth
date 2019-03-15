#! /usr/bin/env python3
# coding: utf-8

import os
import pygame                         # import the pygame library and this module
from pygame.locals import *         
from labyrinth_position import *      # import lists that visually represent the game background
from decor_blit import *              # import decor_blit.py that creates the window and paste the background
from random_position_objects import * # import the file that defines the random coordinates of objects
from path_position import *           # import the file which indicates in list form the coordinates of the labyrinth path

# initialize the pygame library
pygame.init()  

# indicates the way to find the images to be used for the program
os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressource") 

# use the function imported from the file decor_blit.py : open the window and paste the background
background() 

# load the picture of the Mac Gyver, make the background of the picture transparent and paste the picture
mac_gyver_picture = pygame.image.load("MacGyver.png").convert()  
mac_gyver_picture.set_colorkey((255, 255, 255))                   
moving_mac_gyver = mac_gyver_picture.get_rect()                  
window.blit(mac_gyver_picture, (0, 520))                         

# load the picture of the guardian, make the background of the picture transparent and paste the picture
guardian_picture = pygame.image.load("guardian.png").convert() 
guardian_picture.set_colorkey((255, 255, 255))                 
window.blit(guardian_picture, (440, 0))                        

# load the picture of the needle, make the background of the picture transparent and paste the picture
needle_picture = pygame.image.load("needle.png").convert()
needle_picture.set_colorkey((255, 255, 255))
window.blit(needle_picture, needle_position)

# load the picture of the ether, make the background of the picture transparent and paste the picture
ether_picture = pygame.image.load("ether.png").convert_alpha()
ether_picture.set_colorkey((0, 0, 0))
window.blit(ether_picture, ether_position)

# load the picture of the syringe, make the background of the picture transparent and paste the picture
syringe_picture = pygame.image.load("syringe.png").convert()
syringe_picture.set_colorkey((255, 255, 255))
window.blit(syringe_picture, syringe_position)

# load the picture of the grave and make the background of the picture transparent
grave_picture = pygame.image.load("grave.png").convert()
grave_picture.set_colorkey((255, 255, 255))

# load the picture of the won and make the background of the picture transparent
won_picture = pygame.image.load("won.png").convert()
won_picture.set_colorkey((255, 255, 255))

# refresh the screen
pygame.display.flip() 

# function that paste the pictures and refresh the screen
def init_event():
    background()
    window.blit(guardian_picture, (440, 0))
    window.blit(mac_gyver_picture, (last_location_mac_gyver_tuple))
    window.blit(ether_picture, ether_position)
    window.blit(needle_picture, needle_position)
    window.blit(syringe_picture, syringe_position)
    pygame.display.flip()

# 
last_location_mac_gyver_dict = {0: 520}
path_traveled_mac_gyver = [(0, 520)]
counter_objects = 0

# infinite loop
play = 1
while play:                                                  
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_RIGHT: # if press the right arrow key
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(40, 0) # mac gyver goes right
                last_location_mac_gyver_tuple = (cle + 40, valeur) # creates a tuple that represents the last position of mac gyver 
                last_location_mac_gyver_dict.clear() # clears and recreates a new dictionary = last position of mac gyver
                last_location_mac_gyver_dict[cle + 40]=valeur
                init_event()
        if event.type == KEYDOWN and event.key == K_LEFT: # if press the left arrow key
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(- 40, 0) # mac gyver goes left
                last_location_mac_gyver_tuple = (cle - 40, valeur) # creates a tuple = last position of mac gyver  
                last_location_mac_gyver_dict.clear() # clears and recreates a new dictionary = last position of mac gyver
                last_location_mac_gyver_dict[cle - 40] = valeur
                init_event()  
        if event.type == KEYDOWN and event.key == K_UP: # if press the up arrow key
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(0, - 40) # mac gyver goes up
                last_location_mac_gyver_tuple = (cle, valeur - 40) # creates a tuple = last position of mac gyver  
                last_location_mac_gyver_dict.clear() # clears and recreates a new dictionary = last position of mac gyver
                last_location_mac_gyver_dict[cle] = valeur- 40
                init_event()  
        if event.type == KEYDOWN and event.key == K_DOWN: # if press the down arrow key
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(0, 40) # mac gyver goes down
                last_location_mac_gyver_tuple = (cle, valeur + 40) # creates a tuple = last position of mac gyver 
                last_location_mac_gyver_dict.clear() # clears and recreates a new dictionary = last position of mac gyver
                last_location_mac_gyver_dict[cle] = valeur + 40
                init_event()
        if event.type == KEYDOWN: # if press a key
            path_traveled_mac_gyver.append(last_location_mac_gyver_tuple) # creates a list with all mac gyver move coordinates 
            print(path_traveled_mac_gyver)
        # while mac gyver goes down on the coordinates of a wall
        while event.type == KEYDOWN and event.key == K_DOWN and path_position.count(last_location_mac_gyver_tuple) == 0: 
            # mac gyver returns to its original position        
            for cle, valeur in last_location_mac_gyver_dict.items(): 
                moving_mac_gyver = moving_mac_gyver.move(0, - 40)
                last_location_mac_gyver_tuple = (cle, valeur - 40)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle] = valeur - 40
                init_event()
        # while mac gyver goes up on the coordinates of a wall
        while event.type == KEYDOWN and event.key == K_UP and path_position.count(last_location_mac_gyver_tuple) == 0:
            # mac gyver returns to its original position
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(0, 40)
                last_location_mac_gyver_tuple = (cle, valeur + 40)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle] = valeur + 40
                init_event()
        # while mac gyver goes right on the coordinates of a wall
        while event.type == KEYDOWN and event.key == K_RIGHT and path_position.count(last_location_mac_gyver_tuple) == 0:
            # mac gyver returns to its original position
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(- 40, 0)
                last_location_mac_gyver_tuple = (cle - 40, valeur)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle - 40] = valeur
                init_event()
        # while mac gyver goes left on the coordinates of a wall
        while event.type == KEYDOWN and event.key == K_LEFT and path_position.count(last_location_mac_gyver_tuple) == 0:
            # mac gyver returns to its original position
            for cle, valeur in last_location_mac_gyver_dict.items():
                moving_mac_gyver = moving_mac_gyver.move(40, 0)
                last_location_mac_gyver_tuple = (cle + 40, valeur)  
                last_location_mac_gyver_dict.clear()
                last_location_mac_gyver_dict[cle + 40] = valeur
                init_event()
        # if mac gyver is passed on the neddle 
        # +1 to the counter of objects and the needle disappears from the window
        if path_traveled_mac_gyver.count(needle_position) == 1:
            counter_objects = counter_objects + 1
            needle_position = window.blit(needle_picture, (600, 600))
        # if mac gyver is passed on the ether 
        # +1 to the counter of objects and the ether disappears from the window
        if path_traveled_mac_gyver.count(ether_position) == 1:
            counter_objects = counter_objects + 1
            ether_position = window.blit(ether_picture, (600, 600))
        # if mac gyver is passed on the syringe 
        # +1 to the counter of objects and the syringe disappears from the window
        if path_traveled_mac_gyver.count(syringe_position) == 1:
            counter_objects = counter_objects + 1
            syringe_position = window.blit(syringe_picture, (600, 600))
        # if mac gyver have not the 3 objects and arrives at the guardian
        if path_traveled_mac_gyver.count((440, 0)) == 1 and counter_objects != 3:
            # the message "perdu !" is displayed
            background()
            window.blit(guardian_picture, (440, 0))
            window.blit(mac_gyver_picture, (last_location_mac_gyver_tuple))
            window.blit(grave_picture, (200, 200))
            pygame.display.flip()
        # if mac gyver have the 3 objects and arrives at the guardian
        if last_location_mac_gyver_dict == {440: 0} and counter_objects == 3:
            # the message "gagné !" is displayed and the program quits
            background()
            window.blit(ether_picture, ether_position)
            window.blit(needle_picture, needle_position)
            window.blit(syringe_picture, syringe_position)
            window.blit(won_picture, (120, 120))
            pygame.display.flip()
            play = 0
        

  




             
                
            
    

             
                
            
    











