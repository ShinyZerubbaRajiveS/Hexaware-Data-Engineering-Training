classA = {"Rahul", "Sneha", "Amit", "Neha"}
classB = {"Sneha", "Amit", "Karan", "Riya"}

# 1. Students in both classes
common_stud = classA.intersection(classB)
print("Students in both classes:", common_stud)

# 2. Students only in Class A (difference)
only_classA = classA.difference(classB)
print("Students only in Class A:", only_classA)

# 3. All unique students (union)
all_stud = classA.union(classB)
print("All unique students:", all_stud)
