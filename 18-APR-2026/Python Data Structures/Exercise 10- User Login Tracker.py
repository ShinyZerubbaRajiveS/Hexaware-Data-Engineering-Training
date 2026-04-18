logins = [
    ("Rahul", "10:00"),
    ("Sneha", "10:10"),
    ("Rahul", "11:00"),
    ("Arjun", "11:15"),
    ("Sneha", "11:30")
]

# 1:  Count how many times each user logged in
count = {}
for user, time in logins:
    if user in count:
        count[user] += 1
    else:
        count[user] = 1

# 2. Show results in dictionary
print(count)
