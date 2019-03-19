from random import *             # import the random library
from labyrinth_position import LabyrinthList # import lists that represent the game background

class Objet:
        def __init__(self):
                # load the picture of the needle, make the background
                # of the picture transparent and paste the picture
                self.needle_picture = pygame.image.load("needle.png").convert()
                self.needle_picture.set_colorkey((255, 255, 255))
                WINDOW.blit(self.needle_picture, needle_position)

                # load the picture of the ether, make the background
                # of the picture transparent and paste the picture
                self.ether_picture = pygame.image.load("ether.png").convert()
                self.ether_picture.set_colorkey((255, 255, 255))
                WINDOW.blit(self.ether_picture, ether_position)

                # load the picture of the plastic tube, make the background
                # of the picture transparent and paste the picture
                self.plastic_tube_picture = pygame.image.load("plastic_tube.png").convert()
                self.plastic_tube_picture.set_colorkey((255, 255, 255))
                WINDOW.blit(self.plastic_tube_picture, plastic_tube_position)

                # load the picture of the grave and make the background
                # of the picture transparent
                self.grave_picture = pygame.image.load("grave.png").convert()
                self.grave_picture.set_colorkey((255, 255, 255))

                # load the picture of the won and make the background
                # of the picture transparent
                self.won_picture = pygame.image.load("won.png").convert()
                self.won_picture.set_colorkey((255, 255, 255))

                # load the picture of the quit and make the background
                # of the picture transparent
                self.quit_picture = pygame.image.load("quit.png").convert()
                self.quit_picture.set_colorkey((255, 255, 255))

                # load the picture of the replay and make the background
                # of the picture transparent
                self.replay_picture = pygame.image.load("replay.png").convert()
                self.replay_picture.set_colorkey((255, 255, 255))

                self.line_list = [LINE_1, LINE_2, LINE_3, LINE_4, LINE_5, LINE_6, LINE_7, LINE_8,
                     LINE_9, LINE_10, LINE_11, LINE_12, LINE_13]
                self.path_position_of_random_line = []

        def random_position(self):
                """Class that determines a random line and a random number in this line"""
                self.random_line = choice(line_list) # determines a random line
                # add in path_position_of_random_line the path coordinates of the random list
                for i, elt in enumerate(self.random_line):
                        if elt == "6":
                                self.index_random_line = self.line_list.index(self.random_line)
                                self.path_position_of_random_line.append(((i * 40), (self.index_random_line + 1) * 40))
                # determines a random coordinates
                self.random_location = choice(self.path_position_of_random_line)

        def call_function_random_position(self):
                # creating variables with random coordinates for each objects
                self.needle_location = random_position()
                self.ether_location = random_position()
                self.plastic_tube_location = random_position()
                self.needle_position = self.needle_location.self.random_location
                self.ether_position = self.ether_location.self.random_location
                self.plastic_tube_position = self.plastic_tube_location.self.random_location

        def recall_function_random_position(self):
                # while the objects overlap, we determine a new random coordinates
                while self.needle_position == self.ether_position or self.ether_position == self.plastic_tube_position \
                        or self.plastic_tube_position == self.needle_position:
                        self.needle_location = random_position()
                        self.ether_location = random_position()
                        self.plastic_tube_location = random_position()
                        self.needle_position = self.needle_location.self.random_location
                        self.ether_position = self.ether_location.self.random_location
                        self.plastic_tube_position = self.plastic_tube_location.self.random_location
                # while the objects overlap the characters, we determine a new random coordinates
                while self.needle_position == (0, 520) or self.ether_position == (0, 520) or self.plastic_tube_position == (0, 520):
                        self.needle_location = random_position()
                        self.ether_location = random_position()
                        self.plastic_tube_location = random_position()
                        self.needle_position = self.needle_location.self.random_location
                        self.ether_position = self.ether_location.self.random_location
                        self.plastic_tube_position = self.plastic_tube_location.self.random_location
