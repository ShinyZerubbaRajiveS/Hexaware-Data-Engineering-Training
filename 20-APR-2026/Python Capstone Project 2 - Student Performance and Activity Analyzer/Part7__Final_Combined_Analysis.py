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

# Task 33 Combine marks and attendance data
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
print(combined_data)

# Task 34 Print name, marks, attendance, course, grade
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
for name, data in combined_data.items():
    marks = data['marks']
    attendance = data['attendance']
    course = data['course']
    grade = get_grade(marks)
    print(f"{name}: Marks={marks}, Attendance={attendance:.1f}%, Course={course}, Grade={grade}")

# Task 35 Students eligible for certification (marks >= 75 and attendance >= 80)
print("Students eligible for certification:")
eligible = []
for name, data in combined_data.items():
    if data['marks'] >= 75 and data['attendance'] >= 80:
        eligible.append(name)
        print(f"{name} ")

# Task 36 Students who need improvement (marks < 75 or attendance < 80)
print("Students who need improvement:")
improvement = []
for name, data in combined_data.items():
    if data['marks'] < 75 or data['attendance'] < 80:
        improvement.append(name)
        print(f"{name} ")