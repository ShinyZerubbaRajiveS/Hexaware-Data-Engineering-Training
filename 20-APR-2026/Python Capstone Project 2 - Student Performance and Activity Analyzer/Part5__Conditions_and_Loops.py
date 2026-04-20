import json
import csv

with open('marks.json', 'r') as f:
    data = json.load(f)
    students_marks = data['students']

with open('attendance.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    attendance_data = list(csv_reader)

attendance_dict = {}
for student in attendance_data:
    name = student['name']
    days_present = int(student['days_present'])
    total_days = int(student['total_days'])
    attendance_dict[name] = (days_present / total_days) * 100

# Task 23 Print Pass/Fail based on marks
for student in students_marks:
    name = student['name']
    marks = student['marks']
    if marks >= 50:
        print(f"{name}: Pass")
    else:
        print(f"{name}: Fail")

# Task 24 Assign grades based on marks
for student in students_marks:
    name = student['name']
    marks = student['marks']
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    print(f"{name}: Grade {grade}")

# Task 25 Print students with marks > 80 AND attendance > 85%
print("Students with marks above 80 and attendance above 85%:")
for student in students_marks:
    name = student['name']
    marks = student['marks']
    attendance = attendance_dict.get(name, 0)
    if marks > 80 and attendance > 85:
        print(f"{name}")