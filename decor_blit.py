#! /usr/bin/env python3
# coding: utf-8

from labyrinth_position import LabyrinthList
from labyrinth_position import PathPosition
from path_position import Objects
class Personne:

    def __init__(self):
        # load the picture of the Mac Gyver, make the background
        # of the picture transparent and paste the picture
        self.mac_gyver_picture = pygame.image.load("MacGyver.png").convert()
        self.mac_gyver_picture.set_colorkey((255, 255, 255))
        self.moving_mac_gyver = self.mac_gyver_picture.get_rect()
        WINDOW.blit(self.mac_gyver_picture, (0, 520))

        # load the picture of the guardian, make the background
        # of the picture transparent and paste the picture
        self.guardian_picture = pygame.image.load("guardian.png").convert()
        self.guardian_picture.set_colorkey((255, 255, 255))
        WINDOW.blit(self.guardian_picture, (440, 0))

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

        # dictionary that indicates the last position of mac gyver
        self.last_location_mac_gyver_dict = {0: 520}
        # list that indicates the coordinates of the path traveled
        # by mac gyver
        self.path_traveled_mac_gyver = [(0, 520)]
        # counter of objects
        self.counter_objects = 0

    def init_event(self):
        """Function that paste the pictures and refresh the screen"""
        LabyrinthList()
        WINDOW.blit(self.guardian_picture, (440, 0))
        WINDOW.blit(self.mac_gyver_picture, (self.last_location_mac_gyver_tuple))
        WINDOW.blit(self.ether_picture, self.ether_position)
        WINDOW.blit(self.needle_picture, self.needle_position)
        WINDOW.blit(self.plastic_tube_picture, self.plastic_tube_position)
        pygame.display.flip()

    def movement_mac_gyver(self):
        # infinite loop
        self.play = 1
        while play:
            for event in pygame.event.get():
                # if press the right arrow key? mac gyver goes right
                # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    for cle, valeur in last_location_mac_gyver_dict.items():
                        self.moving_mac_gyver = self.moving_mac_gyver.move(40, 0)
                        self.last_location_mac_gyver_tuple = (cle + 40, valeur)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle + 40] = valeur
                        self.path_traveled_mac_gyver.append(last_location_mac_gyver_tuple)
                        init_event()
                # if press the left arrow key, mac gyver goes left
                # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
                if event.type == KEYDOWN and event.key == K_LEFT:
                    for cle, valeur in last_location_mac_gyver_dict.items():
                        self.moving_mac_gyver = self.moving_mac_gyver.move(- 40, 0)
                        self.last_location_mac_gyver_tuple = (cle - 40, valeur)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle - 40] = valeur
                        self.path_traveled_mac_gyver.append(last_location_mac_gyver_tuple)
                        init_event()
                # if press the up arrow key, mac gyver goes up
                # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
                if event.type == KEYDOWN and event.key == K_UP:
                    for cle, valeur in last_location_mac_gyver_dict.items():
                        self.moving_mac_gyver = self.moving_mac_gyver.move(0, - 40)
                        self.last_location_mac_gyver_tuple = (cle, valeur - 40)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle] = valeur -40
                        self.path_traveled_mac_gyver.append(last_location_mac_gyver_tuple)
                        init_event()
                # if press the down arrow key, mac gyver goes down
                # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
                if event.type == KEYDOWN and event.key == K_DOWN:
                    for cle, valeur in last_location_mac_gyver_dict.items():
                        self.moving_mac_gyver = self.moving_mac_gyver.move(0, 40)
                        self.last_location_mac_gyver_tuple = (cle, valeur + 40)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle] = valeur + 40
                        self.path_traveled_mac_gyver.append(last_location_mac_gyver_tuple)
                        init_event()
                # if mac gyver goes down on the coordinates of a wall
                # mac gyver returns to its original position
                if event.type == KEYDOWN and event.key == K_DOWN \
                    and self.path_position_list.count(self.last_location_mac_gyver_tuple) == 0:
                    for cle, valeur in self.last_location_mac_gyver_dict.items():
                        self.moving_mac_gyver = self.moving_mac_gyver.move(0, - 40)
                        del self.path_traveled_mac_gyver[-1]
                        self.last_location_mac_gyver_tuple = (cle, valeur - 40)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle] = valeur - 40
                        init_event()
                # if mac gyver goes up on the coordinates of a wall
                # mac gyver returns to its original position
                if event.type == KEYDOWN and event.key == K_UP \
                    and self.path_position_list.count(self.last_location_mac_gyver_tuple) == 0:
                    for cle, valeur in self.last_location_mac_gyver_dict.items():
                        self.moving_mac_gyver = self.moving_mac_gyver.move(0, 40)
                        del self.path_traveled_mac_gyver[-1]
                        self.last_location_mac_gyver_tuple = (cle, valeur + 40)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle] = valeur + 40
                        init_event()
                # if mac gyver goes right on the coordinates of a wall
                # mac gyver returns to its original position
                if event.type == KEYDOWN and event.key == K_RIGHT \
                    and self.path_position_list.count(self.last_location_mac_gyver_tuple) == 0:
                    for cle, valeur in self.last_location_mac_gyver_dict.items():
                        self.moving_mac_gyver = self.moving_mac_gyver.move(- 40, 0)
                        del self.path_traveled_mac_gyver[-1]
                        self.last_location_mac_gyver_tuple = (cle - 40, valeur)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle - 40] = valeur
                        init_event()
                # if mac gyver goes left on the coordinates of a wall
                # mac gyver returns to its original position
                if event.type == KEYDOWN and event.key == K_LEFT \
                    and self.path_position_list.count(self.last_location_mac_gyver_tuple) == 0:
                    for cle, valeur in self.last_location_mac_gyver_dict.items():
                        del self.path_traveled_mac_gyver[-1]
                        self.moving_mac_gyver = self.moving_mac_gyver.move(40, 0)
                        self.last_location_mac_gyver_tuple = (cle + 40, valeur)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle + 40] = valeur
                        init_event()
                # if the player arrives on the guardien, he can no longer move
                if self.last_location_mac_gyver_dict == {440: - 40}:
                    for cle, valeur in self.last_location_mac_gyver_dict.items():
                        self.last_location_mac_gyver_tuple = (cle, valeur + 40)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle] = valeur + 40
                        init_event()
                if self.path_traveled_mac_gyver.count((440, 0)) == 1 \
                    and self.last_location_mac_gyver_dict == {440: 40}:
                    for cle, valeur in self.last_location_mac_gyver_dict.items():
                        del self.path_traveled_mac_gyver[-1]
                        self.last_location_mac_gyver_tuple = (cle, valeur - 40)
                        self.last_location_mac_gyver_dict.clear()
                        self.last_location_mac_gyver_dict[cle] = valeur - 40
                        init_event()
                # if mac gyver is passed on the neddle
                # +1 to the counter of objects and the needle disappears from the window
                if self.path_traveled_mac_gyver.count(self.needle_position) == 1:
                    self.counter_objects = self.counter_objects + 1
                    self.needle_position = WINDOW.blit(self.needle_picture, (600, 600))
                # if mac gyver is passed on the ether
                # +1 to the counter of objects and the ether disappears from the window
                if self.path_traveled_mac_gyver.count(self.ether_position) == 1:
                    self.counter_objects = self.counter_objects + 1
                    self.ether_position = WINDOW.blit(self.ether_picture, (600, 600))
                # if mac gyver is passed on the plastic_tube
                # +1 to the counter of objects and the syringe disappears from the window
                if self.path_traveled_mac_gyver.count(self.plastic_tube_position) == 1:
                    self.counter_objects = self.counter_objects + 1
                    self.plastic_tube_position = WINDOW.blit(self.plastic_tube_picture, (600, 600))
                # if mac gyver have not the 3 objects and arrives at the guardian
                # the messages "perdu !", "rejouer" and "quitter" is displayed
                # if the player clicks on "rejouer", the program restarts,
                # on "quitter", the program stops
                if self.last_location_mac_gyver_dict == {440: 0} and self.counter_objects != 3:
                    LabyrinthList()
                    WINDOW.blit(self.guardian_picture, (440, 0))
                    WINDOW.blit(self.grave_picture, (200, 200))
                    WINDOW.blit(self.replay_picture, (0, 520))
                    WINDOW.blit(self.quit_picture, (520, 520))
                    pygame.display.flip()
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                        and event.pos[0] > 520 and event.pos[1] > 520:
                        pygame.quit()
                        quit()
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                        and event.pos[0] < 80 and event.pos[1] > 520:
                        Personne()
                # if mac gyver have the 3 objects and arrives at the guardian
                # the message "gagné !" is displayed and the program quits
                if self.last_location_mac_gyver_dict == {440: 0} and self.counter_objects == 3:
                    LabyrinthList()
                    WINDOW.blit(won_picture, (120, 120))
                    pygame.display.flip()
                    pygame.quit()
                    quit()
                return

def main():
    Personne()

if __name__ == "__main__":
    main()