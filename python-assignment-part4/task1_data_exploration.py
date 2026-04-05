# task1_data_exploration.py
import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv(r"C:\Users\pragna.nunna_jindals\assignment-03-bitsom_ba_2511521\python-assignment-part4\students.csv")

# 1. Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# 2. Print dataset shape and column data types
print("\nDataset Shape (rows, columns):")
print(df.shape)

print("\nData Types of each column:")
print(df.dtypes)

# 3. Summary statistics for numeric columns
print("\nSummary Statistics:")
print(df.describe())

# 4. Count students who passed vs failed
print("\nPass/Fail Count:")
print(df['passed'].value_counts())

# 5. Average score per subject for pass/fail
# List of subject columns
subject_cols = ['math', 'science', 'english', 'history', 'pe']

# Average scores for students who passed
pass_avg = df[df['passed'] == 1][subject_cols].mean()

# Average scores for students who failed
fail_avg = df[df['passed'] == 0][subject_cols].mean()

print("\nAverage Subject Scores (Passed Students):")
print(pass_avg)

print("\nAverage Subject Scores (Failed Students):")
print(fail_avg)

# 6. Find student with highest overall average
# Create a temporary column calculating average score across subjects
df['avg_score'] = df[subject_cols].mean(axis=1)

# Find row with maximum average
top_student = df.loc[df['avg_score'].idxmax()]

print("\nTop Performing Student:")
print(top_student['name'], "with average score:", round(top_student['avg_score'],2))