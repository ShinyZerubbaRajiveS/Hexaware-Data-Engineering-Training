import json
import csv

# Task 23 Load visits from TXT
def load_visits(filename):
    visits = []
    with open(filename, 'r') as f:
        for line in f:
            visits.append(line.strip())
    return visits

# Task 24 Load product catalog from JSON
def load_products(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    products = {}
    for product in data['products']:
        products[product['product_id']] = {
            'name': product['name'],
            'price': product['price']
        }
    return products

# Task 25 Load orders from CSV
def load_orders(filename):
    orders = []
    with open(filename, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            orders.append({
                'order_id': int(row['order_id']),
                'customer': row['customer'],
                'product_id': int(row['product_id']),
                'quantity': int(row['quantity'])
            })
    return orders

# Task 26: Calculate product revenue
def calculate_product_revenue(orders, products):
    product_revenue = {}
    for order in orders:
        product_id = order['product_id']
        product_name = products[product_id]['name']
        revenue = products[product_id]['price'] * order['quantity']
        if product_name in product_revenue:
            product_revenue[product_name] += revenue
        else:
            product_revenue[product_name] = revenue
    return product_revenue

# Task 27 Calculate customer spending
def calculate_customer_spending(orders, products):
    """Calculate total spending per customer and return as dictionary"""
    customer_spending = {}
    for order in orders:
        customer = order['customer']
        revenue = products[order['product_id']]['price'] * order['quantity']
        if customer in customer_spending:
            customer_spending[customer] += revenue
        else:
            customer_spending[customer] = revenue
    return customer_spending

# Task 28 Find top customer
def find_top_customer(customer_spending):
    top_customer = max(customer_spending, key=customer_spending.get)
    return (top_customer, customer_spending[top_customer])


if __name__ == "__main__":
    visits = load_visits('website_visits.txt')
    products = load_products('products.json')
    orders = load_orders('orders.csv')

    print("Task 23 - Loaded visits:")
    print(f"Visits: {visits}")
    print(f"Total visits: {len(visits)}")

    print("Task 24 - Loaded product catalog:")
    for pid, info in products.items():
        print(f"{pid}: {info['name']} - Rs.{info['price']}")

    print("Task 25 - Loaded orders:")
    for order in orders:
        print(f"Order {order['order_id']}: {order['customer']} : {order['product_id']} : {order['quantity']}")

    print("Task 26 - Product revenue:")
    product_revenue = calculate_product_revenue(orders, products)
    for product, revenue in product_revenue.items():
        print(f"{product}: Rs.{revenue}")

    print("Task 27 - Customer spending:")
    customer_spending = calculate_customer_spending(orders, products)
    for customer, amount in customer_spending.items():
        print(f"{customer}: Rs.{amount}")

    print("Task 28 - Find top customer:")
    top_customer, top_amount = find_top_customer(customer_spending)
    print(f"Top customer: {top_customer} with Rs.{top_amount}")