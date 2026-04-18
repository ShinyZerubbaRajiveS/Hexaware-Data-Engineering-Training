# 1. Read the file and print all names
with open("logins.txt", "r") as f:
    names = f.read().splitlines()

print("All names:")
for name in names:
    print(name)

# 2. Count the total number of login records
print("\nTotal login records:", len(names))

# 3. Find how many times each user logged in
count = {}
for name in names:
    if name in count:
        count[name] += 1
    else:
        count[name] = 1
print("\nLogin counts:", count)

# 4. Find the user who logged in the most
most_user = max(count, key=count.get)
print("\nUser with most logins:", most_user)

# 5. Print the unique users
print("\nUnique users:", set(names))
