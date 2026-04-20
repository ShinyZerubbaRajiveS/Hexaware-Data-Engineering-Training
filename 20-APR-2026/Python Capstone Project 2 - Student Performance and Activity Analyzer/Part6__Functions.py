import json
import csv

# Task 26: Function to read names from students.txt
def read_student_names(filename):
    with open(filename, 'r') as f:
        names = [line.strip() for line in f]
    return names

# Task 27: Function to load student marks from marks.json
def load_marks(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['students']

# Task 28: Function to load attendance from attendance.csv
def load_attendance(filename):
    with open(filename, 'r') as f:
        csv_reader = csv.DictReader(f)
        attendance = list(csv_reader)
    return attendance

# Task 29: Function to calculate average marks
def calculate_average_marks(students):
    total = sum(student['marks'] for student in students)
    average = total / len(students)
    return average

# Task 30: Function to calculate attendance percentage
def calculate_attendance_percentage(days_present, total_days):
    percentage = (days_present / total_days) * 100
    return percentage

# Task 31: Function to return the topper
def find_topper(students):
    topper = max(students, key=lambda x: x['marks'])
    return topper

# Task 32: Function to generate grade for a mark
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"


if __name__ == "__main__":
    names = read_student_names('students.txt')
    print(f"Task 26 - Student names: {names}")

    students = load_marks('marks.json')
    print(f"Task 27 - Marks data: {students}")

    attendance = load_attendance('attendance.csv')
    print(f"Task 28 - Attendance data: {attendance}")

    avg_marks = calculate_average_marks(students)
    print(f"Task 29 - Average marks: {avg_marks:.2f}")

    for student in attendance:
        days_present = int(student['days_present'])
        total_days = int(student['total_days'])
        percentage = calculate_attendance_percentage(days_present, total_days)
        print(f"Task 30 - {student['name']} attendance: {percentage:.2f}%")

    topper = find_topper(students)
    print(f"Task 31 - Topper: {topper['name']} with {topper['marks']} marks")

    print("Task 32 - Grade examples:")
    test_marks = [92, 85, 78, 70, 45]
    for mark in test_marks:
        print(f"Marks {mark} -> Grade {get_grade(mark)}")