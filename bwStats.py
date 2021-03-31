# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# bwStats.py or BedWarsStats has usefull functions for getting and returning useful information about a player's      #
# bedwars stats.                                                                                                      #
#                                                                                                                     #
#                                                                                                                     #
#                                                                                                                     #
#                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import requests
import json

FINAL_KILLS_DICT = 
    {
        0:
        1:
        2:
        3:
        4:
        5:
        6:
    }

def sayHi():
    return "hi"

#
# Returns final Kills of a player
# @paramater pData = player data .json file
# @paramater index = What Bedwars mode to get number of final kills from
#                    0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4, 6 Dreams
#
def getFinalKills(pData, index):
    if(pdata["success"]):
    {
        return FINAL_KILLS_DICT.get(index, "ERROR: Invalid Final Kills index. Use a number in the inclusive range 0-6")
    }
    else
    {
        print("ERROR: Invalid Player Data, please input valid player data.")
        return none
    }
    
    return 0

#
# Input should be a json file. Returns overall FKDR of a player
#
def getOverallFKDR(input):
    return "yeet"
