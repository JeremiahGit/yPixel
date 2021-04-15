import requests
import json
import bwStats
from pprint import pprint
from Player import Player # How werid is this... I need to do this for some reason...
#
# Returns a json
#
def getInfo(call):
    r = requests.get(call)
    return r.json()

name = "EpicJAG"

uuid = "d6544c1c-d8d9-4140-beaf-b52e4e7d09c0"    
uuid_dashed = "d6544c1cd8d94140beafb52e4e7d09c0"

API_KEY = "961552cb-f9e4-4f25-b7dd-1cad11fe4f3d"  # Dont push with this aaaaa. and if I do just get a new key for my acc. Not that hard to do
                                                  # Currently Looking into a way to not have to deal with this.
                                                  # LOL i pushed with this right after I said I wouldn't push with it. I need to change it now...

name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&name={uuid_dashed}"

#playerInfo = json.load(open("EpicJAG.json","rt"))
p = Player("Chazm")
#print(uuid_link)
#pprint(obj1.getPData())
for i in range (5):
    #print("%d: %f" % (i, bwStats.getFKDR( p.getPData(), i) ))
    print ("%d: %f" % (i, p.getFKDR(i) )) 
#print(obj1.name)
#print(obj1.uuid)

