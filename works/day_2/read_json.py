# Python program to read JSON data
import json

with open("colors.json",'r',encoding="utf-8") as file:
    data = json.load(file)

print(data)