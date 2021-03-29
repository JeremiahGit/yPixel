# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# https://realpython.com/python-json/                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import json
import requests
from pprint import pprint

responce = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(responce.text)
#pprint(type(todos))
#pprint(todos[:3])

