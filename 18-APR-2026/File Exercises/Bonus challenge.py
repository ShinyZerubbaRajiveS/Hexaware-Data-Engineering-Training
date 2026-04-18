import csv

with open("sales.csv", "r") as f:
    reader = csv.DictReader(f)
    sales = list(reader)

for s in sales:
    s["quantity"] = int(s["quantity"])
    s["price"] = int(s["price"])

summary = {}
for s in sales:
    product = s["product"]
    qty = s["quantity"]
    revenue = qty * s["price"]

    if product in summary:
        summary[product]["qty"] += qty
        summary[product]["revenue"] += revenue
    else:
        summary[product] = {"qty": qty, "revenue": revenue}

print("Product Sales Summary")
for product, stats in summary.items():
    print(f"{product} → Qty: {stats['qty']} Revenue: {stats['revenue']}")
