#! /usr/bin/env python3
# coding: utf-8

"""Set of lists that represent the game window: each number is associated with an image :
0 wall top left
1 wall top right
2 wall low right
3 wall low left
4 wall horizontal
5 wall vertical
6 ground"""

class LabyrinthList:
    """ Creates the window and paste the background """
    
    def __init__(self):
        self.LINE_0 = ["0", "4", "4", "4", "4", "4", "4", "4", "4", "4", "2", "6", "3", "4", "1"]
        self.LINE_1 = ["5", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "5"]
        self.LINE_2 = ["5", "6", "0", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "5"]
        self.LINE_3 = ["5", "6", "5", "6", "6", "6", "6", "6", "6", "6", "5", "6", "6", "6", "5"]
        self.LINE_4 = ["5", "6", "5", "6", "0", "4", "4", "6", "4", "4", "4", "4", "1", "6", "5"]
        self.LINE_5 = ["5", "6", "5", "6", "5", "6", "6", "6", "6", "6", "6", "6", "5", "6", "5"]
        self.LINE_6 = ["5", "6", "5", "6", "5", "6", "0", "4", "4", "4", "4", "6", "5", "6", "5"]
        self.LINE_7 = ["5", "6", "5", "6", "5", "6", "5", "6", "6", "6", "6", "6", "6", "6", "5"]
        self.LINE_8 = ["5", "6", "5", "6", "5", "6", "5", "6", "5", "6", "4", "4", "4", "4", "5"]
        self.LINE_9 = ["5", "6", "6", "6", "5", "6", "5", "6", "5", "6", "6", "6", "6", "6", "5"]
        self.LINE_10 = ["5", "6", "5", "6", "5", "6", "5", "6", "5", "4", "4", "4", "4", "6", "5"]
        self.LINE_11 = ["5", "6", "5", "6", "5", "6", "5", "6", "5", "6", "5", "6", "6", "6", "5"]
        self.LINE_12 = ["3", "4", "4", "4", "4", "4", "2", "6", "5", "6", "3", "4", "4", "4", "5"]
        self.LINE_13 = ["6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "6", "5"]
        self.LINE_14 = ["4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "2"]

        self.coordinates_number_picture_list = []

    def load_ground_picture():   
        # load the pictures of the wall and the ground
        ground_picture = pygame.image.load("ground.png").convert_alpha()
        return ground_picture
    
    def load_wall_top_left_picture():   
        # load the pictures of the wall and the ground
        wall_top_left_picture = pygame.image.load("top_left.png").convert_alpha()
        return wall_top_left_picture

    def load_wall_top_right_picture():   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        wall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        return wall_top_right_picture

    def load_wall_low_right_picture():   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        wall_low_right_picture = pygame.image.load("low_right.png").convert_alpha()
        return wall_low_right_picture

    def load_wall_low_left_picture():   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
        wall_low_left_picture = pygame.image.load("low_left.png").convert_alpha()
        return wall_low_left_picture
        
    def load_wall_vertical_picture():   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
        wall_vertical_picture = pygame.image.load("vertical.png").convert_alpha()
        return wall_vertical_picture

    def load_wall_horizontal_picture():   
        # load the pictures of the wall and the groundwall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
        wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
        return wall_horizontal_picture

    def creation_window():
        # creates the window
        WINDOW = pygame.display.set_mode((600, 600))
        return WINDOW
    
    def decor_blit(self, line_number, index, number_picture, picture):
        for i, elt in enumerate(line_number):
            if elt == number_picture:
                self.coordinates_number_picture_list.append(((i*40), index))
        for location in self.coordinates_number_picture_list:
            WINDOW.blit(picture, (location))
    
    def call_decor_blit(self):
        # call the function with different parameters
        decor_blit(self.LINE_0, 0, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_1, 40, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_2, 80, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_3, 120, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_4, 160, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_5, 200, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_6, 240, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_7, 280, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_8, 320, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_9, 360, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_10, 400, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_11, 440, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_12, 480, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_13, 520, "0", self.wall_top_left_picture)
        decor_blit(self.LINE_14, 560, "0", self.wall_top_left_picture)

        decor_blit(self.LINE_0, 0, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_1, 40, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_2, 80, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_3, 120, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_4, 160, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_5, 200, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_6, 240, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_7, 280, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_8, 320, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_9, 360, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_10, 400, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_11, 440, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_12, 480, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_13, 520, "1", self.wall_top_right_picture)
        decor_blit(self.LINE_14, 560, "1", self.wall_top_right_picture)

        decor_blit(self.LINE_0, 0, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_1, 40, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_2, 80, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_3, 120, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_4, 160, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_5, 200, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_6, 240, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_7, 280, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_8, 320, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_9, 360, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_10, 400, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_11, 440, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_12, 480, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_13, 520, "2", self.wall_low_right_picture)
        decor_blit(self.LINE_14, 560, "2", self.wall_low_right_picture)

        decor_blit(self.LINE_0, 0, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_1, 40, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_2, 80, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_3, 120, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_4, 160, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_5, 200, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_6, 240, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_7, 280, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_8, 320, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_9, 360, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_10, 400, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_11, 440, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_12, 480, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_13, 520, "3", self.wall_low_left_picture)
        decor_blit(self.LINE_14, 560, "3", self.wall_low_left_picture)

        decor_blit(self.LINE_0, 0, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_1, 40, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_2, 80, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_3, 120, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_4, 160, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_5, 200, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_6, 240, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_7, 280, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_8, 320, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_9, 360, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_10, 400, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_11, 440, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_12, 480, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_13, 520, "4", self.wall_horizontal_picture)
        decor_blit(self.LINE_14, 560, "4", self.wall_horizontal_picture)

        decor_blit(self.LINE_0, 0, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_1, 40, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_2, 80, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_3, 120, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_4, 160, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_5, 200, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_6, 240, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_7, 280, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_8, 320, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_9, 360, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_10, 400, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_11, 440, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_12, 480, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_13, 520, "5", self.wall_vertical_picture)
        decor_blit(self.LINE_14, 560, "5", self.wall_vertical_picture)

        decor_blit(self.LINE_0, 0, "6", self.ground_picture)
        decor_blit(self.LINE_1, 40, "6", self.ground_picture)
        decor_blit(self.LINE_2, 80, "6", self.ground_picture)
        decor_blit(self.LINE_3, 120, "6", self.ground_picture)
        decor_blit(self.LINE_4, 160, "6", self.ground_picture)
        decor_blit(self.LINE_5, 200, "6", self.ground_picture)
        decor_blit(self.LINE_6, 240, "6", self.ground_picture)
        decor_blit(self.LINE_7, 280, "6", self.ground_picture)
        decor_blit(self.LINE_8, 320, "6", self.ground_picture)
        decor_blit(self.LINE_9, 360, "6", self.ground_picture)
        decor_blit(self.LINE_10, 400, "6", self.ground_picture)
        decor_blit(self.LINE_11, 440, "6", self.ground_picture)
        decor_blit(self.LINE_12, 480, "6", self.ground_picture)
        decor_blit(self.LINE_13, 520, "6", self.ground_picture)
        decor_blit(self.LINE_14, 560, "6", self.ground_picture)
"""Function that pastes multiple images to create the wallpaper"""
"""Searchs each list for the coordinates of each image to paste them"""

class PathPosition:
    # empty list that will indicate the coordinates of the labyrinth path
    def __init__(self):
        self.path_position_list = []

    def incrementation(self):
        # we get in each line, the coordinates of the path and add it to the empty list
        for i, elt in enumerate(self.LINE_0):
            if elt == "6":
                self.path_position_list.append((i*40, 0))
        for i, elt in enumerate(self.LINE_1):
            if elt == "6":
                self.path_position_list.append((i*40, 40))
        for i, elt in enumerate(self.LINE_2):
            if elt == "6":
                self.path_position_list.append((i*40, 80))
        for i, elt in enumerate(self.LINE_3):
            if elt == "6":
                self.path_position_list.append((i*40, 120))
        for i, elt in enumerate(self.LINE_4):
            if elt == "6":
                self.path_position_list.append((i*40, 160))
        for i, elt in enumerate(self.LINE_5):
            if elt == "6":
                self.path_position_list.append((i*40, 200))
        for i, elt in enumerate(self.LINE_6):
            if elt == "6":
                self.path_position_list.append((i*40, 240))
        for i, elt in enumerate(self.LINE_7):
            if elt == "6":
                self.path_position_list.append((i*40, 280))
        for i, elt in enumerate(self.LINE_8):
            if elt == "6":
                self.path_position_list.append((i*40, 320))
        for i, elt in enumerate(self.LINE_9):
            if elt == "6":
                self.path_position_list.append((i*40, 360))
        for i, elt in enumerate(self.LINE_10):
            if elt == "6":
                self.path_position_list.append((i*40, 400))
        for i, elt in enumerate(self.LINE_11):
            if elt == "6":
                self.path_position_list.append((i*40, 440))
        for i, elt in enumerate(self.LINE_12):
            if elt == "6":
                self.path_position_list.append((i*40, 480))
        for i, elt in enumerate(self.LINE_13):
            if elt == "6":
                self.path_position_list.append((i*40, 520))
        for i, elt in enumerate(self.LINE_14):
            if elt == "6":
                self.path_position_list.append((i*40, 560))
        return self.path_position_list

def main():
    LabyrinthList()
    PathPosition()

if __name__ == "__main__":
    main()
