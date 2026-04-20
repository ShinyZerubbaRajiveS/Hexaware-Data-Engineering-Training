import csv

# Task 13 Read attendance.csv
with open('attendance.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    attendance = list(csv_reader)

# Task 14 Print each student's attendance details
print("Student attendance details:")
for student in attendance:
    print(f"{student['name']}: {student['days_present']}")

# Task 15 Calculate attendance percentage for each student
print("Attendance Percentage:- ")
for student in attendance:
    name = student['name']
    days_present = int(student['days_present'])
    total_days = int(student['total_days'])
    percentage = (days_present / total_days) * 100
    print(f"{name}: {percentage:.2f}%")

# Task 16 Print students whose attendance is below 80%
print("Students with attendance below 80%:")
for student in attendance:
    name = student['name']
    days_present = int(student['days_present'])
    total_days = int(student['total_days'])
    percentage = (days_present / total_days) * 100
    if percentage < 80:
        print(f"{name}")

# Task 17 Find student with best attendance
print("Student with best attendance:")
best_student = max(attendance, key=lambda x: int(x['days_present']) / int(x['total_days']))
days_present = int(best_student['days_present'])
total_days = int(best_student['total_days'])
percentage = (days_present / total_days) * 100
print(f"{best_student['name']} ")