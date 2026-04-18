import csv

# 1. Calculate total sales revenue
with open("sales.csv", "r") as f:
    reader = csv.DictReader(f)
    sales = list(reader)
for s in sales:
    s["quantity"] = int(s["quantity"])
    s["price"] = int(s["price"])

total_revenue = sum(s["quantity"] * s["price"] for s in sales)
print("Total sales revenue:", total_revenue)

# 2. Find total quantity sold per product
quantity_per_product = {}
for s in sales:
    product = s["product"]
    qty = s["quantity"]
    if product in quantity_per_product:
        quantity_per_product[product] += qty
    else:
        quantity_per_product[product] = qty
print("\nTotal quantity per product:", quantity_per_product)

# 3. Find the product with highest sales (by revenue)
revenue_per_product = {}
for s in sales:
    product = s["product"]
    revenue = s["quantity"] * s["price"]
    if product in revenue_per_product:
        revenue_per_product[product] += revenue
    else:
        revenue_per_product[product] = revenue

highest_product = max(revenue_per_product, key=revenue_per_product.get)
print("\nProduct with highest sales:", highest_product, "→", revenue_per_product[highest_product])

# 4. Calculate total revenue per product
print("\nRevenue per product:", revenue_per_product)

# 5. Print products with sales above 50,000
print("\nProducts with sales above 50,000:")
for product, revenue in revenue_per_product.items():
    if revenue > 50000:
        print(product, "→", revenue)
