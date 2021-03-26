import requests
import json
from pprint import pprint

def getInfo(call):
    r = requests.get(call)
    return r.json()

name = "Youngthanael"

uuid = "string"
uuid_dashed = "str-ing"

API_KEY = "Youngthanael API Key"

name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&name={uuid_dashed}"

#pprint(getInfo(name_link))
print(name_link)