# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Learning.py is a program file that I am using to learn how to interface with the hypixel api at a basic level.      #
# Thanks to 0x26e on Youtube for making some tutorials [https://www.youtube.com/channel/UC9CpCSR9uFu_1rezA2cUa9g].    #
#                                                                                                                     #
# What else am i supposed to do here? Document my code???                                                             #
# Don't they call it code for a reason though? Im so                                                                  #
# confuseddd.                                                                                                         #
#                                                                                                                     #
# P.S. Look at this fancy box!                                                                                        #
# Look at THIS fancy Documentation website! [https://pkg.go.dev/github.com/t1ra/hypixel/structs]                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# https://hypixel.net/threads/hypixel-api-rate-limit-big-problem.3996327/page-2#post-29013586
import requests
import json
import bwStats

#
# Returns a json
#
def getInfo(call):
    r = requests.get(call)
    return r.json()

name = "Youngthanael"

uuid = "d6544c1c-d8d9-4140-beaf-b52e4e7d09c0"    
uuid_dashed = "d6544c1cd8d94140beafb52e4e7d09c0"

API_KEY = "961552cb-f9e4-4f25-b7dd-1cad11fe4f3d"  # Dont push with this aaaaa. and if I do just get a new key for my acc. Not that hard to do
                                                  # Currently Looking into a way to not have to deal with this.
                                                  # LOL i pushed with this right after I said I wouldn't push with it. I need to change it now...

name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&name={uuid_dashed}"

#pprint(getInfo(name_link))
#print(name_link)
#pprint(uuid_link)
#print(uuid_link)
#playerInfo = getInfo(uuid_link)

playerInfo = json.load(open("EpicJAG.json","rt"))
#print("playerInfo["success"])
print("Overall: %f" % (bwStats.getFKDR(playerInfo, 0)))
print("Solos: %f" % (bwStats.getFKDR(playerInfo, 1)))
print("Doubles: %f" % (bwStats.getFKDR(playerInfo, 2)))
print("Threes: %f" % (bwStats.getFKDR(playerInfo, 3)))
print("Fours: %f" % (bwStats.getFKDR(playerInfo, 4)))
print("4v4: %f" % (bwStats.getFKDR(playerInfo, 5)))



    #print(bwStats.sayHi())
