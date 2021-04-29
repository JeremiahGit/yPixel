# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# bwStats.py or BedWarsStats has useful functions for getting and returning useful information about a player's       #
# bedwars stats.                                                                                                      #
#                                                                                                                     #
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

# # # # # # # # # # # # # # # # # # # # # Essential Stats # # # # # # # # # # # # # # # # # # # # # # #
# Returns [STATISTICS] of a player                                                                    #
# @parameter pData = player data .json file                                                           #
# @parameter index = What Bedwars mode to get STATS from. As axplained in BEDWARS_MODE_DICT.          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def getFinalKills(pData, index):
    if(pData["success"]):
        try:
            bedwarsMode = BEDWARS_MODE_DICT.get(index)
            return pData["player"]["stats"]["Bedwars"]["%sfinal_kills_bedwars" % (bedwarsMode)]
        except:
            return 0

def getFinalDeaths(pData, index):
    if(pData["success"]):
        try:
            bedwarsMode = BEDWARS_MODE_DICT.get(index)
            return pData["player"]["stats"]["Bedwars"]["%sfinal_deaths_bedwars" % (bedwarsMode)]
        except:
            return 0

def getWins(pData, index):
    if(pData["success"]):
        try:
            bedwarsMode = BEDWARS_MODE_DICT.get(index)
            return pData["player"]["stats"]["Bedwars"]["%swins_bedwars" % (bedwarsMode)]
        except:
            return 0

def getLosses(pData, index):
    if(pData["success"]):
        try:
            bedwarsMode = BEDWARS_MODE_DICT.get(index)
            return pData["player"]["stats"]["Bedwars"]["%slosses_bedwars" % (bedwarsMode)]
        except:
           return 0
#
# Win Loss Ratio
# TODO Manually remoce the 4v4 wins and losses from the calculated overall FKDR.
#      It seems that in the update where 4v4 was removed from stats, the API was not 
#      updated to match
#
def getWLRatio(pData, index):
    try:
       return float(  getWins(pData, index) / getLosses(pData, index)  )
    except:
        return float( getWins(pData, index) )

#
# Returns final kill death ratio aka FKDR
# TODO Manually remoce the 4v4 Final Kills and deaths from the calculated overall FKDR.
#      It seems that in the update where 4v4 was removed from stats, the API was not 
#      updated to match
#
def getFKDR(pData, index):
    try:
        return float( getFinalKills(pData, index)) / getFinalDeaths(pData,index )
    except:
        return float( getFinalKills(pData, index) )


# # # # # # # # # # # # # # # # # # # # # Accessory Stats # # # # # # # # # # # # # # # # # # # # # # #
# Returns [STATISTICS] of a player                                                                    #
# @parameter pData = player data .json file                                                           #
# @parameter index = What Bedwars mode to get STATS from. As axplained in BEDWARS_MODE_DICT.          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def getWinstreak(pData, index):
    try:
        bedwarsMode = BEDWARS_MODE_DICT.get(index)
        return pData["player"]["stats"]["Bedwars"]["%swinstreak" % (bedwarsMode)]
    except:
        return 0

def getBedsBroken(pData, index):
    try:
        bedwarsMode = BEDWARS_MODE_DICT.get(index)
        return pData["player"]["stats"]["Bedwars"]["%sbeds_broken_bedwars" % (bedwarsMode)]
    except:
        return 0

def getBedsLost(pData, index):
    try:
        bedwarsMode = BEDWARS_MODE_DICT.get(index)
        return pData["player"]["stats"]["Bedwars"]["%sbeds_lost_bedwars" % (bedwarsMode)]
    except:
        return 0

def getKills(pData, index):
    try:
        bedwarsMode = BEDWARS_MODE_DICT.get(index)
        return pData["player"]["stats"]["Bedwars"]["%skills_bedwars" % (bedwarsMode)]
    except:
        return 0

def getDeaths(pData, index):
    try:
        bedwarsMode = BEDWARS_MODE_DICT.get(index)
        return pData["player"]["stats"]["Bedwars"]["%sdeaths_bedwars" % (bedwarsMode)]
    except:
        return 0

def getBBRLRatio(pData, index):
    try:
        return float( getBedsBroken(pData, index)) / getBedsLost(pData,index )
    except:
        return float( getBedsBroken(pData, index) )

def getKDRatio(pData, index):
    try:
        return float( getKills(pData, index)) / getDeaths(pData,index )
    except:
        return float( getKills(pData, index) )

#
# TODO OMG IDEA. USING THE QUICKSHOP YOU CAN SEE WHAT TYPES OF ITEMS A PLAYER BUYS. AKA LADDERS LADDERS LADDER SWEAT, LADDER USER DETECTOR???????? ACTUALLY OP????????????
# LADDER USER LADDER USER LADDER USER?????? 
# Use an array to do things?
#
def getquickshop(pData):
    try:
        return pData["player"]["stats"]["Bedwars"]["favourites_2"]
    except:
        return 0

def gethotbar(pData):
    try:
        return pData["player"]["stats"]["Bedwars"]["favorite_slots"]
    except:
        return 0
#
# TODO, use quick shop to find out
#
def isLadderUser(pData):
    return (getquickshop(pData).find("ladder") > -1)

def getBedDefenceBlocks(pdata):
    return -1