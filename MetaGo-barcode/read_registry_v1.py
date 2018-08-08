import json


f = open("food_registry.txt", 'r')

file_str = f.read()
file_json = json.loads(file_str)


print(file_json)
print(file_json["51000001"]["name"])

f.close()