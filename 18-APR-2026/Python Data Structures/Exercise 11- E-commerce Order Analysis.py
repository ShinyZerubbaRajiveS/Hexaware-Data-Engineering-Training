orders = [
    {"order_id": 1, "customer": "Rahul", "amount": 2500},
    {"order_id": 2, "customer": "Sneha", "amount": 1800},
    {"order_id": 3, "customer": "Rahul", "amount": 3200},
    {"order_id": 4, "customer": "Amit", "amount": 1500}
]

# 1. Calculate total spending per customer
spending = {}
count = {}
for order in orders:
    customer = order["customer"]
    amount = order["amount"]
    if customer in spending:
        spending[customer] += amount
        count[customer] += 1
    else:
        spending[customer] = amount
        count[customer] = 1
print("Total spending per customer:", spending)

# 2. Find the highest spending customer
highest_customer = max(spending)
print("Highest spending customer:", highest_customer)

# 3. Count total orders per customer
print("Total orders per customer:", count)
