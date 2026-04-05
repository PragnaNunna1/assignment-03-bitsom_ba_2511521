# PART A — WRITE TO FILE

filename = "python_notes.txt" # Define the file name

# List of lines to write initially
notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

# Open file in write mode ('w') which overwrites existing content
# encoding="utf-8" ensures proper character support
with open(filename, "w", encoding="utf-8") as file:
    for line in notes:
        file.write(line + "\n")  # write each line with newline

print("File written successfully.")

# Additional lines to append
extra_notes = [
    "Topic 6: Python is the primary language for machine learning.",
    "Topic 7: Python is a top-tier choice for data analytics."
]

# Open file in append mode ('a') so existing data remains
with open(filename, "a", encoding="utf-8") as file:
    for line in extra_notes:
        file.write(line + "\n")

print("Lines appended successfully.")


# PART B — READ FROM FILE

# Read file and store lines
with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Print numbered lines after stripping newline characters
print("\nNumbered Notes:")

for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

# Count total number of lines
print("\nTotal number of lines:", len(lines))

# Ask user for keyword search
keyword = input("\nEnter a keyword to search: ").lower()

found = False

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No lines found with that keyword.")