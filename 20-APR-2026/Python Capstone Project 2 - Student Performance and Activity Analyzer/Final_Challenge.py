from Part6__Functions import load_marks, load_attendance, calculate_average_marks, find_topper

students = load_marks('marks.json')
attendance_data = load_attendance('attendance.csv')

attendance_dict = {}
for student in attendance_data:
    name = student['name']
    days_present = int(student['days_present'])
    total_days = int(student['total_days'])
    attendance_dict[name] = (days_present / total_days) * 100

best_attendance_name = max(attendance_dict, key=attendance_dict.get)

eligible = []
improvement = []
for student in students:
    name = student['name']
    marks = student['marks']
    attendance = attendance_dict[name]

    if marks >= 75 and attendance >= 80:
        eligible.append(name)
    else:
        improvement.append(name)

# Task 39 : Generate this nal console output:
# Task 40 Make the program modular using functions and keep the code clean.
print(f"Topper: {find_topper(students)['name']}")
print(f"Best Attendance: {best_attendance_name}")
print(f"Average Marks: {calculate_average_marks(students):.1f}")
print(f"Eligible Students: {', '.join(eligible)}")
print(f"Students Needing Improvement: {', '.join(improvement)}")
