student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# 1. Print each subject, marks and grade in a format
for i in range(len(subjects)):
    subject = subjects[i]
    mark = marks[i]
    
    # Determine the grade based on the mark
    if 90 <= mark <= 100:
        grade = 'A+'
    elif 80 <= mark <= 89:
        grade = 'A'
    elif 70 <= mark <= 79:
        grade = 'B'
    elif 60 <= mark <= 69:
        grade = 'C'
    else:
        grade = 'F'
    
    print(f"{subject:10}: {mark} marks -> Grade {grade}")
    
# 2. Calculate required parameters

# total marks using sum() function
total_marks = sum(marks)

# average marks rounded to 2 decimal places
average_marks = round(total_marks / len(marks), 2)

# highest scoring subject
highest_mark = max(marks)
highest_subject = subjects[marks.index(highest_mark)]

# lowest scoring subject
lowest_mark = min(marks)
lowest_subject = subjects[marks.index(lowest_mark)]

# Print the calculated parameters
print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Subject: {highest_subject} with {highest_mark} marks")
print(f"Lowest Subject: {lowest_subject} with {lowest_mark} marks")

# 3. Entering marks using while loop

new_subject_count = 0   # counter for new subjects

print("\nEnter new subjects (type 'done' to finish):")

while True:
    new_subject = input("Enter subject name: ") # input for new subject name
    
    if new_subject.lower() == 'done':   # if user types 'done', exit the loop
        break
    
    new_mark_input = input("Enter marks for the subject: ") # input for new subject marks
    
    # using try-except to handle invalid input for marks
    try:
        new_mark = float(new_mark_input)
        if 0 <= new_mark <= 100:    # check if the mark is within valid range
            subjects.append(new_subject)    # add new subject and its's marks to the subjects and marks lists
            marks.append(new_mark)
            new_subject_count += 1
            print(f"Subject added successfully\n")
        else:
            print("Invaild Entry!!\nMarks must be between 0 and 100.\n")
    except ValueError:
        # If the input cannot be converted to a float, print an error message
        print("Invalid input. Please enter a numeric value for marks.")
        
# 4. Updated results after adding new subjects

print("\nUPDATED RESULTS")
print(f"New subjects added: {new_subject_count}\n")

# recalculate updated average marks
updated_total_marks = sum(marks)
updated_average_marks = round(updated_total_marks / len(marks), 2)

print(f"Updated Average Marks: {updated_average_marks}")