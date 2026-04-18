emails = [
    "user1@gmail.com",
    "user2@yahoo.com",
    "user3@gmail.com",
    "user4@outlook.com"
]

# 1: Extract domains
domains = [email.split("@")[1] for email in emails]

# 2: Count users per domain
count = {}
for d in domains:
    if d in count:
        count[d] += 1
    else:
        count[d] = 1
print(count)
