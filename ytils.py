# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# A class that I can import for utility functions. Duh ytils is a shotened version of Yutils or YoungthanaelUtils.    #
#                                                                                                                     #
#                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import requests

#
# I use this to get the json API data from hypixel. 
#
def getInfo(call):
    r = requests.get(call)
    return r.json()

#
# TODO Make way for other people to use their own API Key instead of being hard coded for mine
#
def getAPIKey():
    return "961552cb-f9e4-4f25-b7dd-1cad11fe4f3d"

#
# TODO lol
#
def cleanTempFiles():
    print("I need to still impliment this. Delete all the temporary files in the dir \"tempPlayerJsons\"")