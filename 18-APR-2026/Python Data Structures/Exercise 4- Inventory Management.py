inventory = {"laptop": 10,
             "mouse": 25,
             "keyboard": 15,
             "monitor": 8}

# 1. Add "monitor":8
print(inventory)

# 2. Reduce laptop stock by 2
inventory["laptop"] -= 2
print(inventory)

# 3. Print items with stock less than 10
for item, stock in inventory.items():
    if stock < 10:
        print(item, ":", stock, " - stock less than 10")
