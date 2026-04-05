import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Subject columns
subject_cols = ['math', 'science', 'english', 'history', 'pe']

# Create average score column
df['avg_score'] = df[subject_cols].mean(axis=1)


# 1. Bar Chart — Average score per subject
avg_scores = df[subject_cols].mean()

plt.figure()
plt.bar(subject_cols, avg_scores)
plt.title("Average Score Per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.savefig("plot1_bar.png")
plt.show()

# 2. Histogram — Distribution of math scores
plt.figure()
plt.hist(df['math'], bins=5)

# Calculate mean math score
mean_math = df['math'].mean()

# Add vertical dashed line for mean
plt.axvline(mean_math, linestyle='dashed', label=f"Mean = {mean_math:.2f}")

plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.legend()

plt.savefig("plot2_histogram.png")
plt.show()

# 3. Scatter Plot — Study hours vs Avg Score
plt.figure()

# Plot passing students
pass_students = df[df['passed']==1]
plt.scatter(pass_students['study_hours_per_day'],
            pass_students['avg_score'],
            label="Pass")

# Plot failing students
fail_students = df[df['passed']==0]
plt.scatter(fail_students['study_hours_per_day'],
            fail_students['avg_score'],
            label="Fail")

plt.title("Study Hours vs Average Score")
plt.xlabel("Study Hours Per Day")
plt.ylabel("Average Score")
plt.legend()

plt.savefig("plot3_scatter.png")
plt.show()


# 4. Box Plot — Attendance distribution
pass_attendance = df[df['passed']==1]['attendance_pct'].tolist()
fail_attendance = df[df['passed']==0]['attendance_pct'].tolist()

plt.figure()
plt.boxplot([pass_attendance, fail_attendance], labels=['Pass','Fail'])

plt.title("Attendance Distribution (Pass vs Fail)")
plt.ylabel("Attendance Percentage")

plt.savefig("plot4_boxplot.png")
plt.show()

# 5. Line Plot — Math vs Science scores per student
plt.figure()

plt.plot(df['name'], df['math'], marker='o', label="Math")
plt.plot(df['name'], df['science'], marker='s', label="Science")

plt.title("Math vs Science Scores by Student")
plt.xlabel("Student Name")
plt.ylabel("Score")

# Rotate names to prevent overlap
plt.xticks(rotation=45)

plt.legend()

plt.savefig("plot5_lineplot.png")
plt.show()