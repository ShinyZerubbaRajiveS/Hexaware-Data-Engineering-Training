sales = [
    {"product": "Laptop", "qty": 5},
    {"product": "Mouse", "qty": 20},
    {"product": "Laptop", "qty": 3},
    {"product": "Keyboard", "qty": 10}
]

# 1. Calculate total sales per product
count = {}
for sale in sales:
    product = sale["product"]
    qty = sale["qty"]
    if product in count:
        count[product] += qty
    else:
        count[product] = qty
print("Total sales per product:", count)

# 2. Find highest selling product
highest_prod = max(count)
print("Highest selling product:", highest_prod)
