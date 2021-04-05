# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# bwStats.py or BedWarsStats has useful functions for getting and returning useful information about a player's      #
# bedwars stats.                                                                                                      #
#                                                                                                                     #
#                                                                                                                     #
#                                                                                                                     #
#                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import requests
import json

#
# Returns final kills of a player
# @parameter pData = player data .json file
# @parameter index = What Bedwars mode to get number of final kills from
#                    0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4, 6 Dreams
# TODO overall Dreams bedwars final kills
#
def getFinalKills(pData, index):
    if(pData["success"]):
        FINAL_KILLS_DICT = {
            0: pData["player"]["stats"]["Bedwars"]["final_kills_bedwars"],
            1: pData["player"]["stats"]["Bedwars"]["eight_one_final_kills_bedwars"],
            2: pData["player"]["stats"]["Bedwars"]["eight_two_final_kills_bedwars"],
            3: pData["player"]["stats"]["Bedwars"]["four_three_final_kills_bedwars"],
            4: pData["player"]["stats"]["Bedwars"]["four_four_final_kills_bedwars"],
            5: pData["player"]["stats"]["Bedwars"]["two_four_final_kills_bedwars"],
            6: pData["player"]["stats"]["Bedwars"]["final_kills_bedwars"] #TODO
        }
        return FINAL_KILLS_DICT.get(index, "ERROR: Invalid Final Kills index. Use a number in the inclusive range 0-6")
    elif (index > 6):
        print("ERROR: Invalid index, please input index less than 6.")  

        return -1
    else:
        print("ERROR: Invalid Player Data, please input valid player data.")  
        return -1

#
# Returns final deaths of a player
# @parameter pData = player data .json file
# @parameter index = What Bedwars mode to get number of final kills from
#                    0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4, 6 Dreams
# TODO overall Dreams bedwars final deaths
#
def getFinalDeaths(pData, index):
    if(pData["success"]):
        FINAL_KILLS_DICT = {
            0: pData["player"]["stats"]["Bedwars"]["final_deaths_bedwars"],
            1: pData["player"]["stats"]["Bedwars"]["eight_one_final_deaths_bedwars"],
            2: pData["player"]["stats"]["Bedwars"]["eight_two_final_deaths_bedwars"],
            3: pData["player"]["stats"]["Bedwars"]["four_three_final_deaths_bedwars"],
            4: pData["player"]["stats"]["Bedwars"]["four_four_final_deaths_bedwars"],
            5: pData["player"]["stats"]["Bedwars"]["two_four_final_deaths_bedwars"],
            6: pData["player"]["stats"]["Bedwars"]["final_deaths_bedwars"] #TODO
        }
        return FINAL_KILLS_DICT.get(index, "ERROR: Invalid Final Kills index. Use a number in the inclusive range 0-6")
    elif (index > 6):
        print("ERROR: Invalid index, please input index less than 6.")  

        return -1
    else:
        print("ERROR: Invalid Player Data, please input valid player data.")  
        return -1

#
# Returns final kill death ratio aka FKDR
# @parameter pData = player data .json file
# @parameter index = What Bedwars mode to get number of final kills from
#                    0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4, 6 Dreams
# TODO Manually remoce the 4v4 Final Kills and deaths from the calculated overall FKDR.
#      It seems that in the update where 4v4 was removed from stats, the API was not 
#      updated to match
#
def getFKDR(pData, index):
    return float(getFinalKills(pData, index)) / getFinalDeaths(pData,index)
