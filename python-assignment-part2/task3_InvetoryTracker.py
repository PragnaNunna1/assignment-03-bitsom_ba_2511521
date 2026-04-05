import copy  # Import copy module for deep copy

# Given inventory with stock and reorder levels
inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock": 8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock": 6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock": 5, "reorder_level": 2},
    "Rasgulla":       {"stock": 4, "reorder_level": 3},
    "Ice Cream":      {"stock": 7, "reorder_level": 4},
}

# Example final cart from Task 2
cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]

# Create deep copy backup
inventory_backup = copy.deepcopy(inventory)

# Demonstrate deep copy
inventory["Paneer Tikka"]["stock"] = 5

print("Modified Inventory:", inventory["Paneer Tikka"])
print("Backup Inventory:", inventory_backup["Paneer Tikka"])

# Restore original state
inventory = copy.deepcopy(inventory_backup)

# Deduct items from inventory
for item in cart:

    name = item["item"]
    quantity = item["quantity"]

    # Check available stock
    available = inventory[name]["stock"]

    if available < quantity:
        print(f"Warning: Only {available} units available for {name}")
        inventory[name]["stock"] = 0
    else:
        inventory[name]["stock"] -= quantity

# Reorder alerts
for item, details in inventory.items():

    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

# Print final inventories
print("\nInventory:", inventory)
print("\nInventory Backup:", inventory_backup)