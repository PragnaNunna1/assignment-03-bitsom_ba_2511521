# ASSIGNMENT 4 - Python Programming Tasks — Data Processing & Analysis 🐍

## Overview

This project contains **four Python tasks** that demonstrate practical programming skills used in real-world data processing.
The tasks focus on **data cleaning, analysis using loops and conditionals, class performance reporting, and string manipulation**.

Each task highlights important Python concepts such as:

* Data parsing and normalization
* Loops (`for`, `while`)
* Conditional statements (`if / elif / else`)
* List and string operations
* Exception handling
* Formatted output using f-strings

---

# Task 1 — Data Parsing & Profile Cleaning 🧹

### Objective

Raw data from forms or spreadsheets often contains **inconsistent formatting**.
This task focuses on cleaning and structuring student data.

### Given Data

Student records contain:

* Names with inconsistent casing and spaces
* Roll numbers stored as **strings**
* Marks stored as a **comma-separated string**

### Operations Performed

1. Loop through each student record.
2. Clean the student name:

   * Remove extra spaces using `strip()`
   * Convert to **Title Case** using `title()`.
3. Convert roll numbers from **string → integer**.
4. Convert the marks string into a **list of integers** using `split()` and list comprehension.
5. Validate that each word in the name contains only alphabetic characters.
6. Print a **formatted student profile card**.
7. Find the student with **roll number 103** and display their name in:

   * **UPPERCASE**
   * **lowercase**

### Concepts Demonstrated

* Data cleaning
* String manipulation
* List comprehension
* Input validation
* Formatted printing

---

# Task 2 — Marks Analysis Using Loops & Conditionals 📊

### Objective

Analyze a student's marks and simulate a marks entry system.

### Given Data

```python
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]
```

### Part 1 — Grade Calculation

Each subject mark is assigned a grade using this scale:

| Marks    | Grade |
| -------- | ----- |
| 90–100   | A+    |
| 80–89    | A     |
| 70–79    | B     |
| 60–69    | C     |
| Below 60 | F     |

A **for loop** prints each subject with its grade.

### Part 2 — Statistics

The program calculates:

* **Total marks**
* **Average marks (rounded to 2 decimal places)**
* **Highest scoring subject**
* **Lowest scoring subject**

### Part 3 — Marks Entry System

A **while loop** allows users to add new subjects:

1. User enters a subject name.
2. User enters marks between **0 and 100**.
3. Typing **"done"** stops the system.

Invalid inputs are handled using:

* `try / except`
* Range validation

### Final Output

After entry ends:

* Number of new subjects added
* Updated class average

### Concepts Demonstrated

* `for` loops
* `while` loops
* Conditional grading logic
* Input validation
* Exception handling

---

# Task 3 — Class Performance Summary 👩‍🎓👨‍🎓

### Objective

Generate a **performance report for an entire class**.

### Given Data

```python
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]
```

### Operations Performed

For each student:

1. Compute **average marks**
2. Assign result status:

   * **Pass** if average ≥ 60
   * **Fail** otherwise
3. Print a formatted report table.

### Example Output

```
Name              | Average | Status
----------------------------------------
Ayesha Sharma     | 78.60   | Pass
Rohit Verma       | 61.00   | Pass
Priya Nair        | 87.40   | Pass
Karan Mehta       | 49.00   | Fail
Sneha Pillai      | 75.60   | Pass
```

### After the Table

The program also prints:

* Number of students who **passed**
* Number of students who **failed**
* **Class topper** (highest average)
* **Class average**

### Concepts Demonstrated

* Tuple unpacking
* Aggregation using loops
* Maximum value tracking
* Table formatting

---

# Task 4 — String Manipulation Utility ✍️

### Objective

Practice common **string processing operations**.

### Given Essay

```
"  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "
```

### Steps Performed

#### 1️⃣ Remove Extra Spaces

Use `strip()` to remove leading and trailing whitespace.

#### 2️⃣ Convert to Title Case

Use `title()` to capitalize the first letter of each word.

#### 3️⃣ Count Word Occurrences

Count how many times `"python"` appears using:

```python
count("python")
```

#### 4️⃣ Replace Words

Replace `"python"` with:

```
Python 🐍
```

using:

```python
replace("python", "Python 🐍")
```

#### 5️⃣ Sentence Splitting

Split the essay into sentences using:

```python
split(". ")
```

#### 6️⃣ Number Sentences

Print each sentence:

* On a new line
* Numbered starting from **1**
* Ensure each sentence ends with `"."`

### Concepts Demonstrated

* String cleaning
* Word counting
* Text replacement
* Sentence parsing
* Enumeration with `enumerate()`

---

# Skills Demonstrated Across All Tasks 🚀

This project demonstrates:

* Python data cleaning techniques
* List and string manipulation
* Loop structures (`for`, `while`)
* Conditional logic
* Input validation
* Exception handling
* Data summarization
* Clean formatted output

---

# Conclusion ✅

The four tasks together provide a **solid foundation in Python fundamentals**, especially for working with **real-world messy data, structured analysis, and text processing**.

