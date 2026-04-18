import json
students={
    "students":[
        {"name":"Zerubba", "marks":88},
        {"name":"Seraphin", "marks":91},
    ]
}
# with open("output.json","w") as file:
#     json.dump(students,file)

with open("output.json","w") as file:
    json.dump(students,file, indent=4)

#json.dump -> Converts Python dictionary → JSON