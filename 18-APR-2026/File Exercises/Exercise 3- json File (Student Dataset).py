import json

# 1. Print all student names
with open("students.json", "r") as f:
    data = json.load(f)
students = data["students"]
print("All student names:")
for s in students:
    print(s["name"])

# 2. Print students enrolled in Python course
print("\nStudents in Python course:")
for s in students:
    if s["course"] == "Python":
        print(s["name"])

# 3. Find the student with the highest marks
topper = students[0]
for s in students:
    if s["marks"] > topper["marks"]:
        topper = s
print("\nTopper:", topper["name"])

# 4. Calculate average marks
average = sum(s["marks"] for s in students) / len(students)
print("\nAverage marks:", average)

# 5. Count how many students are enrolled in each course
count = {}
for s in students:
    course = s["course"]
    if course in count:
        count[course] += 1
    else:
        count[course] = 1

print("\nCourse enrollment counts:",count)
