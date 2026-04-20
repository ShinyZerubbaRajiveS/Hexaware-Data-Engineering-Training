# Task 7 Read products.json .
import json
with open("products.json", "r") as file:
    data = json.load(file)

# Task 8 Print all product names and prices.
for product in data["products"]:
    print(product["name"], ":", product["price"])

# Task 9 Store product information in a dictionary.
product_dict = {}
for product in data["products"]:
    product_dict[product["product_id"]] = {
        "name": product["name"],
        "price": product["price"]
    }
print(product_dict)

# Task 10 Find the most expensive product.
most_expensive = max(data["products"], key=lambda p: p["price"])
print("Most Expensive Product:", most_expensive["name"],most_expensive["price"])

# Task 11 Find the least expensive product.
least_expensive = min(data["products"], key=lambda p: p["price"])
print("Least Expensive Product:", least_expensive["name"],least_expensive["price"])