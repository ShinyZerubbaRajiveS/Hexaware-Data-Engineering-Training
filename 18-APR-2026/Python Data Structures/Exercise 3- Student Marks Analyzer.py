students = {
    "Rahul": 85,
    "Sneha": 92,
    "Arjun": 78,
    "Priya": 88
}

# 1. Print the topper
topper = max(students)
print("Topper:", topper)

# 2. Print average marks
average = sum(students.values()) / len(students)
print("Average Marks:", average)

# 3. Print students scoring above 85
for name, marks in students.items():
    if marks > 85:
        print(name, ":", marks ,"- scores above 85")