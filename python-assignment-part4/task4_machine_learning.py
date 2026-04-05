import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("students.csv")

# Features and target
features = ['math','science','english','history','pe','attendance_pct','study_hours_per_day']

X = df[features]
y = df['passed']

# 1. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 2. Scale features
scaler = StandardScaler()

# Fit on training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data
X_test_scaled = scaler.transform(X_test)

# 3. Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Training accuracy
train_acc = model.score(X_train_scaled, y_train)
print("Training Accuracy:", train_acc)

# 4. Evaluate Model
predictions = model.predict(X_test_scaled)

test_acc = accuracy_score(y_test, predictions)
print("Test Accuracy:", test_acc)

# Print prediction results with names
for i, pred in enumerate(predictions):

    student_name = df.loc[X_test.index[i], 'name']
    actual = y_test.iloc[i]

    correct = "✅" if pred == actual else "❌"

    print(student_name,
          "| Actual:", actual,
          "| Predicted:", pred,
          correct)

# 5. Feature Importance
coefficients = model.coef_[0]

# Pair feature names with coefficients
feature_importance = list(zip(features, coefficients))

# Sort by absolute value
feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)

print("\nFeature Importance:")
for feature, coef in feature_importance:
    print(feature, ":", coef)

# Plot coefficients
names = [f[0] for f in feature_importance]
values = [f[1] for f in feature_importance]

colors = ['green' if v > 0 else 'red' for v in values]

plt.figure()
plt.barh(names, values, color=colors)

plt.title("Feature Importance (Logistic Regression)")
plt.xlabel("Coefficient Value")
plt.ylabel("Feature")

plt.show()


# 6. Predict for New Student
new_student = [[75,70,68,65,80,82,3.2]]

scaled_student = scaler.transform(new_student)

prediction = model.predict(scaled_student)[0]
probability = model.predict_proba(scaled_student)

result = "Pass" if prediction == 1 else "Fail"

print("\nNew Student Prediction:", result)
print("Probability:", probability)