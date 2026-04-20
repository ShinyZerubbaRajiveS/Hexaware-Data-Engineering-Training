import json

# Task 6 Read marks.json
with open('marks.json', 'r') as f:
    data = json.load(f)
    students = data['students']

# Task 7: Print all student names and marks
for student in students:
    print(f"{student['name']}: {student['marks']}")

# Task 8: Find student with highest marks
print("Student with highest marks:")
highest = max(students, key=lambda x: x['marks'])
print(f"{highest['name']} : {highest['marks']} ")

# Task 9: Find student with lowest marks
print("Student with lowest marks:")
lowest = min(students, key=lambda x: x['marks'])
print(f"{lowest['name']} : {lowest['marks']} ")

# Task 10: Calculate average marks
total_marks = sum(student['marks'] for student in students)
average = total_marks / len(students)
print(f"Average marks: {average:.2f}")

# Task 11: Print only students enrolled in Python course
print("Students enrolled in Python course:")
python_students = [student for student in students if student['course'] == 'Python']
for student in python_students:
    print(f"{student['name']}")

# Task 12: Count students in each course using dictionary
course_count = {}
for student in students:
    course = student['course']
    if course in course_count:
        course_count[course] += 1
    else:
        course_count[course] = 1
for course, count in course_count.items():
    print(f"{course}: {count} ")