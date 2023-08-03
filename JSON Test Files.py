import json
import datetime

item1 = {
    "name" : "Cheese",
    "tags" : ["Dairy", "Yellow", "Expensive"],
    "amt" : 5,
    "unit" : "units",
    "recentDate" : "08/03/2023",
    "expDate" : "09/04/2024"
}

item2 = {
    "name" : "Butter",
    "tags" : ["Condiment", "Yellow", "Cheap"],
    "amt" : 4,
    "unit" : "tbsp",
    "recentDate" : "08/03/2023",
    "expDate" : "09/04/2024"
}

item3 = {
    "name" : "Ground Beef",
    "tags" : ["Meat", "Red", "Expensive"],
    "amt" : 2.8,
    "unit" : "lbs",
    "recentDate" : "08/03/2023",
    "expDate" : None
}

item4 = {
    "name" : "Ground Pork",
    "tags" : ["Meat", "Brown", "Cheap"],
    "amt" : 1.4,
    "unit" : "lbs",
    "recentDate" : "08/03/2023",
    "expDate" : None
}


itemList = {
    0 : item1,
    1 : item2,
    2 : item3,
    3 : item4
}
testJson = json.dumps(itemList, indent = 4)

with open("test1.json", "w") as newFile:
    newFile.write(testJson)

'''
# Access nested dictionaries
with open("test1.json", "r") as openFile:
    readJson = json.load(openFile)

# Even if the key was initially an int, it will be converted as string, so use str(<int>) to access index
for i in range(len(readJson)):
    print(readJson[str(i)])
'''
