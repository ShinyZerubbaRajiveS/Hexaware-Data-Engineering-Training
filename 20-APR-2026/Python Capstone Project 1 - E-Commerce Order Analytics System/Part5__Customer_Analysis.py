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

# Task 20 Calculate total spending per customer.
customer_spending = {}
for order in orders:
    customer = order['customer']
    revenue = product_prices[order['product_id']] * order['quantity']
    if customer in customer_spending:
        customer_spending[customer] += revenue
    else:
        customer_spending[customer] = revenue
print("Total spending per customer:")
for customer, amount in customer_spending.items():
    print(f"  {customer}: Rs.{amount}")

# Task 21 Find the highest spending customer.
highest_customer = max(customer_spending, key=customer_spending.get)
highest_amount = customer_spending[highest_customer]
print(f"Highest spending customer:")
print(f"  {highest_customer} with Rs.{highest_amount}")

# Task 22 Find customers who spent more than Rs.50,000.
high_spenders = {customer: amount for customer, amount in customer_spending.items() if amount > 50000}
print(f"Customers who spent more than Rs.50,000:")
if high_spenders:
    for customer, amount in high_spenders.items():
        print(f"  {customer}: Rs.{amount}")
