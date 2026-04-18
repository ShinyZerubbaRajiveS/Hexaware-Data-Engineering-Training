import csv

# 1. Print all employee names
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    employees = list(reader)
print("All employee names:")
for e in employees:
    print(e["name"])

# 2. Find employees working in IT department
print("\nEmployees in IT department:")
for e in employees:
    if e["department"] == "IT":
        print(e["name"])

# 3. Calculate the average salary
salaries = [int(e["salary"]) for e in employees]
avg_salary = sum(salaries) / len(salaries)
print("\nAverage salary:", avg_salary)

# 4. Find the highest salary employee
highest = employees[0]
for e in employees:
    if int(e["salary"]) > int(highest["salary"]):
        highest = e
print("\nHighest salary employee:", highest["name"], "→", highest["salary"])

# 5. Count how many employees belong to each department
dept_count = {}
for e in employees:
    dept = e["department"]
    if dept in dept_count:
        dept_count[dept] += 1
    else:
        dept_count[dept] = 1
print("\nDepartment counts:", dept_count)
