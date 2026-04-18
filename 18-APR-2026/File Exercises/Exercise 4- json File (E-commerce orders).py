import json

# 1. Print all orders
with open("orders.json", "r") as f:
    data = json.load(f)
orders = data["orders"]
print("All orders:")
for o in orders:
    print(o)

# 2. Calculate total revenue
total_revenue = sum(o["amount"] for o in orders)
print("\nTotal revenue:", total_revenue)

# 3. Find total spending per customer
spending = {}
count = {}
for o in orders:
    customer = o["customer"]
    amount = o["amount"]
    if customer in spending:
        spending[customer] += amount
        count[customer] += 1
    else:
        spending[customer] = amount
        count[customer] = 1
print("\nTotal spending per customer:", spending)

# 4. Find the highest spending customer
highest_customer = max(spending, key=spending.get)
print("\nHighest spending customer:", highest_customer, "→", spending[highest_customer])

# 5. Count total orders per customer
print("\nTotal orders per customer:", count)
