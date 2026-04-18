
# 1. Read all numbers from the file
with open("numbers.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]
print("All numbers:", numbers)

# 2. Calculate the sum of all numbers
print("Sum of numbers:", sum(numbers))

# 3. Find the maximum number
print("Maximum number:", max(numbers))

# 4. Find the minimum number
print("Minimum number:", min(numbers))

# 5. Count how many numbers are greater than 50
great = sum(1 for n in numbers if n > 50)
print("Numbers greater than 50:", great)

