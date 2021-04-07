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
    #staticTrackedPlayers #haha I'm pretending that there is a static keyword!!

    def __init__(self, USER_NAME):
        self.temp_file = ytils.getInfo("https://api.hypixel.net/player?key=%s&name=%s" % (ytils.getAPIKey(), USER_NAME))

        self.name = USER_NAME
        self.FileLocation = f".\\tempPlayerJsons\\{self.name}.json"

        if(self.temp_file["success"]):
            self.f = open(self.FileLocation,"w+")
            self.f.write(json.dumps(self.temp_file))
            self.f.close()

        else:
            print("ERROR: Player file likely exists. Cannot retreive new data from API for %s. Using an older version of %s's API data." % (self.name, self.name))


    #def __init__(self, pData):
        # I want to make and access a .json file for each instance of a player. This would be to circumvent 
        # rate limit on the player lookup. 

        # Also I can store the time that I originally looked up the player so that I can know when its okay to
        # look them up again. I would then delete their file and make a new one.
        
        # Also keep track of the mosed used player

        # Also record data points for the bedwars stats of a player and use that to eventually make a graph of
        # the player's stats. I think that would be cool. I can also do this for skywars
        
        #if(pData["success"]):
        #    self.name = pData["player"]["displayname"]
        #    self.uuid = pData["player"]["uuid"]
        #    self.jsonFileName = f"{self.uuid}_{self.name}.json"
        #
        #    self._file = open(f".\\tempPlayerJsons\\{self.jsonFileName}","w+")
        #    self._file.write(json.dumps(pData))
        #    self._file.close()
        #
        #else:
        #    print("ERROR: Player file likely exists. Cannot retreive new data from API.")


    def getPData(self):
        return open(self.FileLocation, "r").read().json()