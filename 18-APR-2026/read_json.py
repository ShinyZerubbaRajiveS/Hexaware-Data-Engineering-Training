import json #JSON tool kit
#→ helps convert between JSON ↔ Python

with open("data.json", "r") as file:
    data = json.load(file)
print(data)
for student in data["students"]:
    print(student["name"],student["marks"])
