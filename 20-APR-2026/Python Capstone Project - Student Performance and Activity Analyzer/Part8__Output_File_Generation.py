import json
import csv
from Part6__Functions import get_grade

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

combined_data = {}
for student in students_marks:
    name = student['name']
    marks = student['marks']
    course = student['course']
    attendance = attendance_dict.get(name, 0)
    combined_data[name] = {
        "marks": marks,
        "attendance": attendance,
        "course": course
    }

# Task 37 Write final student summary to report.txt
with open('report.txt', 'w') as f:
    f.write("Student Report\n")
    for name, data in combined_data.items():
        marks = data['marks']
        attendance = data['attendance']
        grade = get_grade(marks)
        f.write(f"{name} - Marks: {marks} - Attendance: {attendance:.1f}% - Grade: {grade}\n")
print("'report.txt' created.")

# Task 38 Write only eligible students to eligible_students.txt
with open('eligible_students.txt', 'w') as f:
    f.write("Eligible Students (Marks >= 75 and Attendance >= 80%)\n")
    eligible_count = 0
    for name, data in combined_data.items():
        if data['marks'] >= 75 and data['attendance'] >= 80:
            marks = data['marks']
            attendance = data['attendance']
            course = data['course']
            grade = get_grade(marks)
            f.write(f"{name} - Marks: {marks} - Attendance: {attendance:.1f}% - Course: {course} - Grade: {grade}\n")
            eligible_count += 1
    if eligible_count == 0:
        f.write("No students are eligible for certification.\n")
    else:
        f.write(f"\nTotal Eligible Students: {eligible_count}")

print("'eligible_students.txt' created.")