# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The Players.py class will be a manager of the players. Players contains a data structure, maybe an                  #
# arraylist idk yet which data structure would be best in python. I'm new to python :P!                               #
#                                                                                                                     #
# Anyway there will be get set and add remove and reset functions for the player to be used in mass. muhahahahahaha   #
#                                                                                                                     #
#                                                                                                                     #
#                                                                                                                     #
#                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import json
from Player import Player
import ytils

playerList = []

class Players:
    
    def __init__(self):
        print("Initalizing Players Class") #idk if this will ever be usefull

    def add(self, name):
        temp = Player(name)
        playerList.append(temp)

    def clear(self, name):
        playerList.clear()

    def getPlayers(self):
        return playerList.copy()
    
    def getPlayersCount(self):
        return playerList.count()

    def removePlayer(self, name):
        temp = Player(name)
        playerList.remove(temp)



    
    
        