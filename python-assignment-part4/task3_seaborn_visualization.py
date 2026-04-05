import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Create avg_score column
subject_cols = ['math', 'science', 'english', 'history', 'pe']
df['avg_score'] = df[subject_cols].mean(axis=1)


# 1. Seaborn Bar Plots
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))

# Average math score by pass/fail
sns.barplot(data=df, x='passed', y='math', ax=ax1)
ax1.set_title("Average Math Score (Pass vs Fail)")

# Average science score by pass/fail
sns.barplot(data=df, x='passed', y='science', ax=ax2)
ax2.set_title("Average Science Score (Pass vs Fail)")

plt.savefig("seaborn_barplots.png")
plt.show()


# 2. Scatter Plot with Regression Lines
plt.figure()

# Pass students
sns.regplot(data=df[df['passed']==1],
            x='attendance_pct',
            y='avg_score',
            label="Pass")

# Fail students
sns.regplot(data=df[df['passed']==0],
            x='attendance_pct',
            y='avg_score',
            label="Fail")

plt.legend()
plt.title("Attendance vs Average Score")
plt.xlabel("Attendance Percentage")
plt.ylabel("Average Score")

plt.savefig("seaborn_scatter.png")
plt.show()


# Comparison Comment

# Seaborn automatically applies statistical plotting features
# and produces visually appealing graphs with less code.
# Matplotlib provides more flexibility and control but
# requires more manual configuration for styling and layout.