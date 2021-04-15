# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# bwStats.py or BedWarsStats has useful functions for getting and returning useful information about a player's       #
# bedwars stats.                                                                                                      #
#                                                                                                                     #
# TODO I have encountered and error. If a player does not have a Final Death and it is attempted to access it i get   #
# an error!!!!                                                                                                        #
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
        return FINAL_KILLS_DICT.get(index, "ERROR: Invalid index. Use a number in the inclusive range 0-6")
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
        FINAL_DEATHS_DICT = {
            0: pData["player"]["stats"]["Bedwars"]["final_deaths_bedwars"],
            1: pData["player"]["stats"]["Bedwars"]["eight_one_final_deaths_bedwars"],
            2: pData["player"]["stats"]["Bedwars"]["eight_two_final_deaths_bedwars"],
            3: pData["player"]["stats"]["Bedwars"]["four_three_final_deaths_bedwars"],
            4: pData["player"]["stats"]["Bedwars"]["four_four_final_deaths_bedwars"],
            5: pData["player"]["stats"]["Bedwars"]["two_four_final_deaths_bedwars"],
            6: pData["player"]["stats"]["Bedwars"]["final_deaths_bedwars"] #TODO
        }
        return FINAL_DEATHS_DICT.get(index, "ERROR: Invalid Final deaths index. Use a number in the inclusive range 0-6")
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

#
# Returns wins of a player
# @parameter pData = player data .json file
# @parameter index = What Bedwars mode to get number of wins from
#                    0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4, 6 Dreams
# TODO overall dream wins
#
def getWins(pData, index):
    if(pData["success"]):
        WINS_DICT = {
            0: pData["player"]["stats"]["Bedwars"]["wins_bedwars"],
            1: pData["player"]["stats"]["Bedwars"]["eight_one_wins_bedwars"],
            2: pData["player"]["stats"]["Bedwars"]["eight_two_wins_bedwars"],
            3: pData["player"]["stats"]["Bedwars"]["four_three_wins_bedwars"],
            4: pData["player"]["stats"]["Bedwars"]["four_four_wins_bedwars"],
            5: pData["player"]["stats"]["Bedwars"]["two_four_wins_bedwars"],
            6: pData["player"]["stats"]["Bedwars"]["wins_bedwars"] #TODO
        }
        return WINS_DICT.get(index, "ERROR: Invalid index. Use a number in the inclusive range 0-6")
    else:
        print("ERROR: Invalid Player Data, please input valid player data.")  
        return -1

#
# Returns losses of a player
# @parameter pData = player data .json file
# @parameter index = What Bedwars mode to get number of losses from
#                    0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4, 6 Dreams
# TODO overall dream losses
#
def getLosses(pData, index):
    if(pData["success"]):
        LOSSES_DICT = {
            0: pData["player"]["stats"]["Bedwars"]["losses_bedwars"],
            1: pData["player"]["stats"]["Bedwars"]["eight_one_losses_bedwars"],
            2: pData["player"]["stats"]["Bedwars"]["eight_two_losses_bedwars"],
            3: pData["player"]["stats"]["Bedwars"]["four_three_losses_bedwars"],
            4: pData["player"]["stats"]["Bedwars"]["four_four_losses_bedwars"],
            5: pData["player"]["stats"]["Bedwars"]["two_four_losses_bedwars"],
            6: pData["player"]["stats"]["Bedwars"]["losses_bedwars"] #TODO
        }
        try:
            return LOSSES_DICT.get(index, "ERROR: Invalid index. Use a number in the inclusive range 0-6")
        except KeyError:
            return 1
    else:
        print("ERROR: Invalid Player Data, please input valid player data.")  
        return -1

#
# Returns the win loss ratio aka FKDR
# @parameter pData = player data .json file
# @parameter index = What Bedwars mode to get number of final kills from
#                    0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4, 6 Dreams
# TODO Manually remoce the 4v4 wins and losses from the calculated overall FKDR.
#      It seems that in the update where 4v4 was removed from stats, the API was not 
#      updated to match
#
def getWLRatio(pData, index):
    return float(getWins(pData, index)) / getLosses(pData,index)