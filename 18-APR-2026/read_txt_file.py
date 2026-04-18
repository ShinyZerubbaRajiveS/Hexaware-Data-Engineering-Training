with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("data.txt", "r") as file:
    students=file.readlines()
print("Total Students:" ,len(students))

total=0
with open("data.txt","r") as file:
    for line in file:
        total+=int(line.strip())
print("Total=",total)