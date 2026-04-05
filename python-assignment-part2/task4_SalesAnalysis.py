sales_log = {
    "2025-01-01": [
        {"order_id": 1, "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2, "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3, "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4, "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5, "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
}


daily_revenue = {}
# Calculate total revenue per day
for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total

# Print revenue per day
for date, revenue in daily_revenue.items():
    print(date, "₹", revenue)

# Best selling day
best_day = max(daily_revenue, key=daily_revenue.get)
print("\nBest Selling Day:", best_day)

# Find most ordered item
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:     # loop through items in each order to count occurrences
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)

print("Most Ordered Item:", most_ordered)

# Add new sales day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

# Print numbered orders using enumerate
print("\nAll Orders:")

counter = 1
# Loop through sales log to print each order with a counter
for date, orders in sales_log.items(): 

    for order in orders: # loop through orders for each date
        items = ", ".join(order["items"])

        print(f"{counter}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {items}")

        counter += 1