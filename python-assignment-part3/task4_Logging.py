import requests
from datetime import datetime

LOG_FILE = "error_log.txt"


# Function to write log entries
def log_error(location, error_type, message):

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format log entry
    entry = f"[{timestamp}] ERROR in {location}: {error_type} — {message}\n"

    # Append log to file
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(entry)

# Trigger connection error by making request to invalid URL
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)

except requests.exceptions.ConnectionError as e:
    print("Connection failed.")
    log_error("fetch_products", "ConnectionError", str(e))

# Trigger timeout error by making request to a URL that takes too long to respond
try:
    response = requests.get("https://dummyjson.com/products/999", timeout=5)

    if response.status_code != 200:
        print("Product not found.")
        log_error("lookup_product", "HTTPError", "404 Not Found for product ID 999")

except Exception as e:
    log_error("lookup_product", "Exception", str(e))


# Print log contents to verify entries
try:
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        print("\nError Log Contents:")
        print(file.read())

except FileNotFoundError:
    print("No logs found.")