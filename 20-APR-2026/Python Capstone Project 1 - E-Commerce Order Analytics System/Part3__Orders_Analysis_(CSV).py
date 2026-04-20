# Task 12 Read orders.csv .
import csv
with open("orders.csv", "r") as file:
    reader = csv.reader(file)

# Task 13 Print each order.
    for row in reader:
        print(row)

# Task 14 Calculate the total quantity sold per product.
product_sales = {}
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product_id"]
        qty = int(row["quantity"])
        if product in product_sales:
            product_sales[product] += qty
        else:
            product_sales[product] = qty
print("Total quantity sold per product:", product_sales)

# Task 15 Calculate total orders per customer.
customer_orders = {}
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        customer = row["customer"]
        if customer in customer_orders:
            customer_orders[customer] += 1
        else:
            customer_orders[customer] = 1
print("Total orders per customer:", customer_orders)