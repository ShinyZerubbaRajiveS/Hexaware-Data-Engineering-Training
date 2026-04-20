# Task 1 Read students.txt and print all names
with open('students.txt', 'r') as f:
    names = [line.strip() for line in f]
    print(names)

# Task 2 Count total number of entries in students.txt
total_entries = len(names)
print("Total entries:",total_entries)

# Task 3 Find unique student names using a set
unique_names = set(names)
print("Unique names: ",unique_names)

# Task 4 Count how many times each student name appears
name_count = {}
for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1
print(name_count)

# Task 5 Write unique student names into a new file
with open('unique_students.txt', 'w') as f:
    for name in unique_names:
        f.write(name + '\n')
print("unique_students.txt' created.")