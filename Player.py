# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The player class is an object that will allow me to access the same player multiple times without having to deal    #
# with the rate limit on looking up the same player endpoint multiple times.                                          #
#                                                                                                                     #
# https://api.hypixel.net/player?key={API_KEY}&name={PLAYER_NAME}                                                     #
#                                                                                                                     #
#                                                                                                                     #
#                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import ytils
import json
import bwStats

class Player:

    #
    # Sets name, creates a file with name, sets a file location to be accessed later.
    # Also want to record data points for the bedwars stats of a player and use that to eventually make a graph of
    # the player's stats. I think that would be cool. I can also do this for skywars
    #
    def __init__(self, USER_NAME):

        self.name = USER_NAME
        self.temp_file = ytils.getInfo("https://api.hypixel.net/player?key=%s&name=%s" % (ytils.getAPIKey(), self.name))
        self.FileLocation = f".\\tempPlayerJsons\\{self.name}.json"

        if(self.temp_file["success"]):
            self.f = open(self.FileLocation,"w+")
            self.f.write(json.dumps(self.temp_file))
            self.f.close()

        else:
            print("WARNING: Cannot create a new file %s. Using an older version of %s's API data." % (self.name, self.name))

    #
    # A call to getPData() will return the player endpoint of the hypixel API as a json. The file should already be 
    # created upon initialization.
    #
    def getPData(self):
        return json.loads(open(self.FileLocation, "r").read()) #haha i hope this does not cause memory leaks because i dont explicitly close the file...

    #
    # Get bedwars stats. bwStats.py has the source file and has documentation for the functions.
    #
    def getFKDR(self, index):
        return round( bwStats.getFKDR(self.getPData(), index), 2)

    def getBWFinalKills(self, index):
        return round( bwStats.getFinalKills(self.getPData(), index), 2)

    def getBWFinalDeaths(self, index):
        return round( bwStats.getFinalDeaths(self.getPData(), index), 2)

    def getBWWL(self, index):
        return round( bwStats.getWLRatio(self.getPData(), index), 2)

    def getBWWins(self, index):
        return round( bwStats.getWins(self.getPData(), index), 2)

    def getBWLosses(self, index):
        return round( bwStats.getLosses(self.getPData(), index), 2)

    def getBWStar(self):
        return bwStats.getStar(self.getPData)

    #
    # Abyss Scre is a special way for measuring the skill and experence of a bedwars player. It comes from the
    # hypixel guild ABYSS and is calculated by the following formula:   Score = FKDR^2 * STAR
    #
    def getBWAbyssScore(self):
        return int(pow(  bwStats.getFKDR( self.getPData(), 0 ), 2  ) * bwStats.getStar(self.getPData()))


    #
    #
    #