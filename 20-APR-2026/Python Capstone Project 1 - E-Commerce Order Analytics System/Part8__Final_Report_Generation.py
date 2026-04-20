from Part6__Functions import load_visits, load_products, load_orders, calculate_product_revenue, calculate_customer_spending, \
    find_top_customer

# Load data
visits = load_visits('website_visits.txt')
products = load_products('products.json')
orders = load_orders('orders.csv')

# Calculate required data
unique_visitors = set(visits)
total_visits = len(visits)
total_revenue = sum(calculate_product_revenue(orders, products).values())
customer_spending = calculate_customer_spending(orders, products)
top_customer, top_amount = find_top_customer(customer_spending)
product_revenue = calculate_product_revenue(orders, products)

# Create sales report
with open('sales_report.txt', 'w') as f:
    f.write("E-Commerce Sales Report\n\n")
    #f.write("=" * 50 + "\n")
    f.write(f"Total Website Visits: {total_visits}\n")
    f.write(f"Unique Visitors: {len(unique_visitors)}\n\n")
    f.write(f"Total Revenue: {total_revenue}\n\n")
    f.write(f"Top Customer: {top_customer}\n\n")
    f.write("Product Sales\n")
    #f.write("-" * 30 + "\n")

    for product, revenue in product_revenue.items():
        f.write(f"{product:<10} -> {revenue}\n")

print("sales_report.txt has been created successfully!")