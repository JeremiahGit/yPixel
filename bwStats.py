# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# bwStats.py or BedWarsStats has useful functions for getting and returning useful information about a player's       #
# bedwars stats.                                                                                                      #
#                                                                                                                     #
# TODO I have encountered and error. If a player does not have a Final Death and it is attempted to access it i get   #
# an error!!!!     also happens with kills                                                                            #
#                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import json

#
# The bedwars mode stats are getting called for. The value passed in is usually index. However, there are some other names that can be used
# 0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4
#
BEDWARS_MODE_DICT = {
    0: "",
    1: "eight_one_final_",
    2: "eight_two_final_",
    3: "four_three_final_",
    4: "four_four_final_",
    5: "two_four_final_",

    "overall": "",
    "solos": "eight_one_final_",
    "doubles": "eight_two_final_",
    "threes": "four_three_final_",
    "fours": "four_four_final_",
    "4v4": "two_four_final_",
    }

#
# Returns the number of stars a player has
#
def getStar(pData):
    if(pData["success"]):
        try:
            return pData["player"]["achievements"]["bedwars_level"]
        except:
            return 0

#
# Returns final kills of a player
# @parameter pData = player data .json file
# @parameter index = What Bedwars mode to get number of final kills from
#
def getFinalKills(pData, index):
    if(pData["success"]):
        try:
            bedwarsMode = BEDWARS_MODE_DICT.get(index)
            return pData["player"]["stats"]["Bedwars"]["%sfinal_kills_bedwars" % (bedwarsMode)]
        except:
            return 0
#
# Returns final deaths of a player
# @parameter pData = player data .json file
# @parameter index = What Bedwars mode to get number of final kills from
#                    0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4, 6 Dreams
# TODO overall Dreams bedwars final deaths
#
def getFinalDeaths(pData, index):
    if(pData["success"]):
        try:
            bedwarsMode = BEDWARS_MODE_DICT.get(index)
            return pData["player"]["stats"]["Bedwars"]["%sfinal_deaths_bedwars" % (bedwarsMode)]
        except:
            return 1
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
#
def getWins(pData, index):
    if(pData["success"]):
        try:
            bedwarsMode = BEDWARS_MODE_DICT.get(index)
            return pData["player"]["stats"]["Bedwars"]["%swins_bedwars" % (bedwarsMode)]
        except:
            return 0
#
# Returns losses of a player
# @parameter pData = player data .json file
# @parameter index = What Bedwars mode to get number of losses from
#                    0 Overall, 1 Solos, 2 Doubles, 3 Threes, 4 Fours, 5 4v4, 6 Dreams
# TODO overall dream losses
#
def getLosses(pData, index):
    if(pData["success"]):
        #try:
        bedwarsMode = BEDWARS_MODE_DICT.get(index)
        print("+++++++++++")
        WL = pData["player"]["stats"]["Bedwars"]["%flosses_bedwars" % (bedwarsMode)]
        print("--------")
        print(WL)
        print("========")
        return WL
        #except:
        #   return 1.0
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
    wl = float(  float(getWins(pData, index)) / float(getLosses(pData, index))  )
    print(";;;;;;;;;;")
    return wl