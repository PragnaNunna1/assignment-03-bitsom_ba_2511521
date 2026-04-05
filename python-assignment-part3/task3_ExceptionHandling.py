import requests

# 1. Self divided function with exception handling
def safe_divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

    except TypeError:
        return "Error: Invalid input types"

# 2. Test cases for safe_divide function
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

# 3. Safe file reading function with exception handling
def read_file_safe(filename):
    try:        # Attempt to open and read the file
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    finally:
        print("File operation attempt complete.")


print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))

# 4. Input validation with exception handling
while True:
    user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ")
    # Check if user wants to quit
    if user_input.lower() == "quit":
        break

    try:
        product_id = int(user_input)
        # Validate product ID range
        if product_id < 1 or product_id > 100:
            print("Invalid range. Enter ID between 1 and 100.")
            continue

        response = requests.get(f"https://dummyjson.com/products/{product_id}", timeout=5)

        if response.status_code == 404:   # Handle case where product ID does not exist
            print("Product not found.")

        elif response.status_code == 200:  # Successful response, parse and display product info
            product = response.json()
            print(product["title"], "-", product["price"])

    except ValueError:
        print("Invalid input. Please enter a number.")