# Using product prices and order quantities:
import json
import csv
with open('products.json', 'r') as f:
    products_data = json.load(f)
product_prices = {}
for product in products_data['products']:
    product_prices[product['product_id']] = product['price']
orders = []
with open('orders.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        orders.append({
            'order_id': int(row['order_id']),
            'customer': row['customer'],
            'product_id': int(row['product_id']),
            'quantity': int(row['quantity'])
        })

# Task 16 Calculate revenue for each order.
order_revenues = []
for order in orders:
    revenue = product_prices[order['product_id']] * order['quantity']
    order_revenues.append({
        'order_id': order['order_id'],
        'revenue': revenue
    })
    print(f"  Order {order['order_id']}: {revenue}")
print()

# Task 17 Calculate total revenue.
total_revenue = sum(order['revenue'] for order in order_revenues)
print(f"Total Revenue: {total_revenue}")
print()

# Task 18 Calculate total revenue per product.
product_names = {}
for product in products_data['products']:
    product_names[product['product_id']] = product['name']
revenue_per_product = {}
for order in orders:
    product_id = order['product_id']
    product_name = product_names[product_id]
    revenue = product_prices[product_id] * order['quantity']
    if product_name in revenue_per_product:
        revenue_per_product[product_name] += revenue
    else:
        revenue_per_product[product_name] = revenue
print("Revenue per product:")
print(revenue_per_product)
print()

# Task 19 Find the highest selling product by revenue.
highest_product = max(revenue_per_product, key=revenue_per_product.get)
highest_revenue = revenue_per_product[highest_product]
print(f"Highest selling product by revenue:  {highest_product}- {highest_revenue}")