from Part6__Functions import load_visits, load_orders

visits = load_visits('website_visits.txt')
orders = load_orders('orders.csv')
all_visitors = set(visits)
customers = set(order['customer'] for order in orders)

# Task 29 Visitors who visited but never ordered
visited_not_ordered = all_visitors - customers
print("Visitors who visited but never ordered:")
print(visited_not_ordered)

# Task 30 Customers who ordered but never visited more than once
from collections import Counter
visit_count = Counter(visits)
customers_never_visited_more_than_once = []
for customer in customers:
    if visit_count.get(customer, 0) <= 1:
        customers_never_visited_more_than_once.append(customer)
print("Customers who ordered but never visited more than once:")
print(customers_never_visited_more_than_once)