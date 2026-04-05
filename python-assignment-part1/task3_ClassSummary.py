class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

pass_count = 0
fail_count = 0
total_class_average = 0
topper_average = 0
topper_name = ""

# print the formatted header
print("Name\t\t |Average |Status")
print("-----------------------------------")

# 1. Loop through each student in the class data
for name, marks in class_data:
    average = sum(marks) / len(marks)   # calculate the average marks for the student
    total_class_average += average  # add to total class average for later calculation
    
    if average >= 60:   # determine pass/fail status based on average marks
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1
        
    # check if this student is topper and update topper information if necessary
    if average > topper_average:
        topper_average = average
        topper_name = name

    # 2. Print the student's name, average marks, and pass/fail status in a formatted manner
    print(f"{name}\t |{average:.2f}\t |{status}")
print("-----------------------------------")

# calculate and print the class average
class_average = total_class_average / len(class_data)

# 3. Print summary information about the class performance
print("\n\tCLASS PERFORMANCE SUMMARY")
print(f"Total Students: {len(class_data)}")
print(f"Passed Students: {pass_count}")
print(f"Failed Students: {fail_count}")
print(f"Class Average: {class_average:.2f}")
print(f"Topper: {topper_name} with average of {topper_average:.2f} points")