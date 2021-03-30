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
x = 0

for todo_obj in todos:
    if (todo_obj["userId"] == 2):
        x+=1

print(x)