# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
path = r"C:\Users\shali\Desktop\DS_Road_Map\Project\student mark prediction\student_info.csv"
df = pd.read_csv(path)


# ✅ Remove missing values
df = df.dropna()

print("✅ Dataset Loaded Successfully")
print(df.head(), "\n")
print("Shape:", df.shape, "\n")
print(df.info(), "\n")

# Feature & Target
X = df[["study_hours"]]
y = df[["student_marks"]]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("✅ Data Split Completed")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test), "\n")

# Train model
lr = LinearRegression()
lr.fit(X_train, y_train)

print("✅ Model Training Completed")
print("Training Accuracy:", lr.score(X_train, y_train))
print("Testing Accuracy:", lr.score(X_test, y_test), "\n")

# Plot results
plt.scatter(X_train, y_train)
plt.scatter(X_test, y_test)
plt.plot(X_train, lr.predict(X_train))
plt.title("Student Marks Prediction")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Save model
joblib.dump(lr, "student_mark_predictor.pkl")
print("✅ Model Saved as student_mark_predictor.pkl", "\n")

# Load model & predict
model = joblib.load("student_mark_predictor.pkl")
sample_prediction = model.predict([[5]])[0][0]
print("✅ Predicted Marks for 5 Hours of Study:", sample_prediction)
