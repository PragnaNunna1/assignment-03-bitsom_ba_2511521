raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

# 1. Loop through raw_students and for each student, produce a cleaned version
for student in raw_students:
    # Clean the name
    # strip() removes leading and trailing whitespace
    # title() converts the name into title case
    student["name"] = student["name"].strip().title()
    
    # Convert roll number from string to integer
    student["roll"] = int(student["roll"])
    
    # Convert marks_str string into a list of integers
    # use split(", ") to split the string into a list of strings
    # use a list comprehension to iterate over each mark string, and convert it to an integer using int(mark)
    student["marks_str"] = [int(mark) for mark in student["marks_str"].split(", ")]
    
    # Create the cleaned student data
    cleaned_student = {"name": student["name"],
                        "roll": student["roll"],
                        "marks_str": student["marks_str"]}
    
    # Add the cleaned_student data to the cleaned_students list
    cleaned_students.append(cleaned_student)
    
    
    # 2. Verify if the name is valid: check that every word in the name contains only alphabetic characters
    # checking if name contains only alphabets
    words = student["name"].split()
    correct_name = all(word.isalpha() for word in words)
    
    # verifying using if statement and printing the result
    if correct_name:
        print(f"{student['name']} : ✓ Valid name")
    else:
        print(f"{student['name']} : ✗ Invalid name") 
        
    # 3. Print in the given format
    print("================================")
    print(f"Student : {student['name']}")
    print(f"Roll No : {student['roll']}")
    print(f"Marks : {student['marks_str']}")
    print("================================")
    
# 4. Find student with roll number 103 and print name in uppercase and lowercase
for student in cleaned_students:
    if student["roll"] == 103:
        print("\nStudent with roll number 103:")
        print(f"Name in uppercase: {student['name'].upper()}")
        print(f"Name in lowercase: {student['name'].lower()}")
