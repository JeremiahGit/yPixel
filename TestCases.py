import requests
import json
import bwStats
import ytils
from pprint import pprint
from Player import Player # How werid is this... I need to do this for some reason...
from Players import Players

name = "EpicJAG"

uuid = "d6544c1c-d8d9-4140-beaf-b52e4e7d09c0"    
uuid_dashed = "d6544c1cd8d94140beafb52e4e7d09c0"

API_KEY = "961552cb-f9e4-4f25-b7dd-1cad11fe4f3d"
name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&name={uuid_dashed}"
ppl = Players()
#ppl.add("grhigrakn;sgr")

#ppl.add("EpicJAG")
ppl.add("Youngthanael")
#ppl.add("Gamerboy80")
#ppl.add("Manhal_iq_")
ppl.add("Purpled")
#ppl.add("Vixon")
#ppl.add("Chazm")
#ppl.add("b0mbies")
#ppl.add("wqlff")
#ppl.add("dogcatwhat")
#ppl.add("luvonox")
pl = ppl.getPlayers()

for gamer in pl:
    print(f"================ [✫ {gamer.getBWStar()}] {gamer.name} {gamer.getBWAbyssScore()} ================")
    for i in range (1):
        #print("%d: %f" % (i, bwStats.getFKDR( p.getPData(), i) ))
        #print(gamer.getBWStar())
        print("FKDR: %f" % (gamer.getFKDR(i) )) 
        #print ("Finals: %f" % (gamer.getBWFinalKills(i) )) 
        #print ("FDeaths: %f" % (gamer.getBWFinalDeaths(i) )) 
        #print ("Wins: %f" % (gamer.getBWWins(i) )) 
        #print ("Losses: %f" % (gamer.getBWLosses(i) )) 
        print("W/L: %f" % (gamer.getBWWL(i) ))
        print(gamer.isLadderUser())
#print(obj1.name)
#print(obj1.uuid)

