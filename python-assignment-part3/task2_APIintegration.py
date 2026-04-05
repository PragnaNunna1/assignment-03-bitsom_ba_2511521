import requests

BASE_URL = "https://dummyjson.com/products"

# 1. Fetch products and display in table format
try:
    # Send GET request to fetch 20 products
    response = requests.get(f"{BASE_URL}?limit=20", timeout=5)

    # Convert JSON response to Python dictionary
    data = response.json()

    products = data["products"]

    print("\nProduct List") # Display header for product table
    print("ID | Title | Category | Price | Rating")
    print("-------------------------------------------")

    # Loop through products and print formatted table
    for product in products:
        print(f"{product['id']} | {product['title']} | {product['category']} | ${product['price']} | {product['rating']}")

except requests.exceptions.ConnectionError:     # Handle connection errors
    print("Connection failed. Please check your internet.")

except requests.exceptions.Timeout:     # Handle request timeout
    print("Request timed out. Try again later.")

except Exception as e:      # Handle any other unexpected exceptions
    print("Unexpected error:", e)

# 2. Filter and sort products by rating and price
try:
    # Filter products with rating >= 4.5
    filtered = [p for p in products if p["rating"] >= 4.5]

    # Sort filtered products by price descending
    filtered_sorted = sorted(filtered, key=lambda x: x["price"], reverse=True)

    print("\nFiltered Products (Rating >= 4.5) Sorted by Price Desc:")

    for product in filtered_sorted: # Print title and price of filtered products
        print(product["title"], "-", product["price"])

except Exception as e:
    print("Error during filtering/sorting:", e)

# 3. Fetch products in "laptops" category
try:
    response = requests.get(f"{BASE_URL}/category/laptops", timeout=5)

    laptops = response.json()["products"]

    print("\nLaptop Products:")

    for laptop in laptops:
        print(laptop["title"], "-", laptop["price"])

except requests.exceptions.ConnectionError:
    print("Connection failed.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except Exception as e:
    print("Unexpected error:", e)

# 4. Create a new product via POST request
try:
    payload = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"
    }

    response = requests.post(f"{BASE_URL}/add", json=payload, timeout=5)

    print("\nPOST Response:")
    print(response.json())

except requests.exceptions.ConnectionError:
    print("Connection failed.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except Exception as e:
    print("Unexpected error:", e)