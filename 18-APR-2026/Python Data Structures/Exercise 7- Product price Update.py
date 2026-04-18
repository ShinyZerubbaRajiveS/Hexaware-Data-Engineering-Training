products = {
    "Laptop": 75000,
    "Mobile": 30000,
    "Tablet": 25000
}

# 1. Increase all prices by 10%
for prod in products:
    products[prod] = products[prod] * 1.10

# 2. Print updated prices
for prod, price in products.items():
    print(prod, ":", price)
