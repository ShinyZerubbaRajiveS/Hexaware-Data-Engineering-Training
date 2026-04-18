student={
    "name":"Zerubba",
    "age":21,
    "course":"Python"
}

#key-value pairs, majorly used for API and JSON Handling

print(student) #{'name': 'Zerubba', 'age': 21, 'course': 'Python'}
print(student.keys()) #dict_keys(['name', 'age', 'course'])
print(student.values()) #dict_values(['Zerubba', 21, 'Python'])
print(student.items()) # dict_items([('name', 'Zerubba'), ('age', 21), ('course', 'Python')])
print(student["name"])
print(student["age"])
print(student["course"]) #Python
print(student.get("name"))
print(student.get("age"))
print(student.get("course")) #Python

# add a new pair
student["city"]="Chennai"
print(student) # {'name': 'Zerubba', 'age': 21, 'course': 'Python', 'city': 'Chennai'}