# Use:
# list → store orders
# dictionary → store product prices
# set → store unique visitors
# tuple → represent (product_name, revenue) pairs

from Part6__Functions import load_visits, load_products, load_orders, calculate_product_revenue

visits = load_visits('website_visits.txt')
products = load_products('products.json')
orders = load_orders('orders.csv')

print("LIST (orders):")
print(orders)
print()

product_prices = {}
for pid, info in products.items():
    product_prices[pid] = info['price']
print("DICTIONARY (product prices):")
print(product_prices)
print()

unique_visitors = set(visits)
print("SET (unique visitors):")
print(unique_visitors)
print()

product_revenue = calculate_product_revenue(orders, products)
revenue_tuples = []
for name, revenue in product_revenue.items():
    revenue_tuples.append((name, revenue))
print("TUPLE (product, revenue) pairs:")
print(revenue_tuples)