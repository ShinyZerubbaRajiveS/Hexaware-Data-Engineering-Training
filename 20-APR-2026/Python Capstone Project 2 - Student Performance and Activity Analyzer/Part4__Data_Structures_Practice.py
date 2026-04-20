import json
import csv

with open('marks.json', 'r') as f:
    data = json.load(f)
    students_marks = data['students']

with open('attendance.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    attendance_data = list(csv_reader)

# Task 18 Store all marks in a list and print: highest, lowest, sum
marks_list = [student['marks'] for student in students_marks]
print(f"Marks list: {marks_list}")
print(f"Highest marks: {max(marks_list)}")
print(f"Lowest marks: {min(marks_list)}")
print(f"Sum of marks: {sum(marks_list)}")

# Task 19 Create a tuple of all courses and print it
courses_list = [student['course'] for student in students_marks]
courses_tuple = tuple(courses_list)
print(f"{courses_tuple}")

# Task 20 Create a set of all courses to show unique courses
unique_courses = set(courses_list)
print(f"Unique courses: {unique_courses}")

# Task 21 Create dictionary where key = student name, value = marks
name_marks_dict = {}
for student in students_marks:
    name_marks_dict[student['name']] = student['marks']
print(f"{name_marks_dict}")

# Task 22 Create dictionary where key = student name, value = attendance percentage
name_attendance_dict = {}
for student in attendance_data:
    name = student['name']
    days_present = int(student['days_present'])
    total_days = int(student['total_days'])
    percentage = (days_present / total_days) * 100
    name_attendance_dict[name] = round(percentage, 2)
print(f"{name_attendance_dict}")