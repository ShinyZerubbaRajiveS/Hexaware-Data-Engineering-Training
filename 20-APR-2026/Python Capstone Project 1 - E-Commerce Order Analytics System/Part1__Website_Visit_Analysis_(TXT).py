# Task 1 Read website_visits.txt.
with open("website_visits.txt", "r") as file:
    views = file.read().splitlines()

# Task 2 Print all visitors.
for visitor in views:
    print(visitor)

# Task 3 Find the total number of visits.
total_views = len(views)
print("Total Visits:", total_views)

# Task 4 Find unique visitors using a set.
unique = set(views)
print("Unique Visitors:", unique)

# Task 5 Count how many times each visitor came to the website.
count = {}
for visitor in views:
    if visitor in count:
        count[visitor] += 1
    else:
        count[visitor] = 1
print(count)

# Task 6 Find the most frequent visitor.
max_views = max(count.values())
most_freq = [visitor for visitor, visits in count.items() if visits == max_views]
print("Most Frequent Visitor:", most_freq)