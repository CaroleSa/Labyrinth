import os
from labyrinth_position import *

path_position=[]

i=0
for i, elt in enumerate(line_0):
    if elt=="6":
        path_position.append((i*40, 0))  
for i, elt in enumerate(line_1):
    if elt=="6":
        path_position.append((i*40, 40))
for i, elt in enumerate(line_2):
    if elt=="6":
        path_position.append((i*40, 80))
for i, elt in enumerate(line_3):
    if elt=="6":
        path_position.append((i*40, 120))
for i, elt in enumerate(line_4):
    if elt=="6":
        path_position.append((i*40, 160))  
for i, elt in enumerate(line_5):
    if elt=="6":
        path_position.append((i*40, 200))
for i, elt in enumerate(line_6):
    if elt=="6":
        path_position.append((i*40, 240))
for i, elt in enumerate(line_7):
    if elt=="6":
        path_position.append((i*40, 280))  
for i, elt in enumerate(line_8):
    if elt=="6":
        path_position.append((i*40, 320))  
for i, elt in enumerate(line_9):
    if elt=="6":
        path_position.append((i*40, 360))
for i, elt in enumerate(line_10):
    if elt=="6":
        path_position.append((i*40, 400))
for i, elt in enumerate(line_11):
    if elt=="6":
        path_position.append((i*40, 440))
for i, elt in enumerate(line_12):
    if elt=="6":
        path_position.append((i*40, 480))
for i, elt in enumerate(line_13):
    if elt=="6":
        path_position.append((i*40, 520))
for i, elt in enumerate(line_14):
    if elt=="6":
        path_position.append((i*40, 560))               
i+=1

print(path_position)