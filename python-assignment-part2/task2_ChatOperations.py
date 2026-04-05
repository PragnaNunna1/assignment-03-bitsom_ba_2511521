menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

cart = []

# 1. Add an item to the cart using a function.
def add_to_cart(item_name, quantity=1):
    if item_name not in menu:   # check if the item is on the menu
        print(f"{item_name} is not on the menu.")
        return
    
    if not menu[item_name]["available"]:    # check item availability
        print(f"Sorry, {item_name} is currently not available.")
        return
        
    for item in cart:   # Check if item already exists in cart
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return

    cart.append({       # If item not already in cart, add new entry
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })

    print(f"Added {item_name} x{quantity}")

# Function to remove item from cart
def remove_from_cart(item_name):

    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"{item_name} removed from cart")
            return

    print(f"{item_name} not found in cart.")

# Function to print cart
def print_cart():
    print("\nCurrent Cart:", cart)

# Simulated sequence
add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)
print_cart()

add_to_cart("Mystery Burger", 1)
print_cart()

add_to_cart("Chicken Wings", 1)
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()

# 5. Final Order Summary
print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    total_price = item["price"] * item["quantity"]
    subtotal += total_price
    print(f"{item['item']:<18} x{item['quantity']}   ₹{total_price:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):                ₹{gst:.2f}")
print(f"Total Payable:           ₹{total:.2f}")
print("====================================")
        