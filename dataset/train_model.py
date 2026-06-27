# ==========================================================
# SMART CITY TRAFFIC FORECASTING PROJECT
# Complete Machine Learning Code
# ==========================================================

# -----------------------------
# Step 1: Import Libraries
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import joblib

# -----------------------------
# Step 2: Load Dataset
# -----------------------------
df = pd.read_csv("dataset/train_aWnotuB.csv")

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== DATASET INFO ==========")
print(df.info())

# -----------------------------
# Step 3: Convert DateTime
# -----------------------------
df["DateTime"] = pd.to_datetime(df["DateTime"])

# -----------------------------
# Step 4: Feature Engineering
# -----------------------------
df["Year"] = df["DateTime"].dt.year
df["Month"] = df["DateTime"].dt.month
df["Day"] = df["DateTime"].dt.day
df["Hour"] = df["DateTime"].dt.hour

# Remove unwanted columns
df.drop(["ID", "DateTime"], axis=1, inplace=True)

print("\n========== UPDATED DATASET ==========")
print(df.head())

# -----------------------------
# Step 5: Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# Step 6: Prepare Features
# -----------------------------
X = df[["Junction", "Year", "Month", "Day", "Hour"]]

y = df["Vehicles"]

print("\nFeatures Shape :", X.shape)
print("Target Shape :", y.shape)

# -----------------------------
# Step 7: Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Data :", X_train.shape)
print("Testing Data :", X_test.shape)

# -----------------------------
# Step 8: Train Model
# -----------------------------
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Model Training Completed!")

# -----------------------------
# Step 9: Prediction
# -----------------------------
predictions = model.predict(X_test)

# -----------------------------
# Step 10: Evaluation
# -----------------------------
mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = mse ** 0.5

r2 = r2_score(y_test, predictions)

print("\n========== MODEL PERFORMANCE ==========")

print("Mean Absolute Error :", round(mae,2))

print("Mean Squared Error :", round(mse,2))

print("Root Mean Squared Error :", round(rmse,2))

print("R2 Score :", round(r2,4))

# -----------------------------
# Step 11: Save Model
# -----------------------------
joblib.dump(model, "traffic_model.pkl")

print("\nModel Saved Successfully!")

print("File Name : traffic_model.pkl")

# -----------------------------
# Step 12: Sample Prediction
# -----------------------------
sample = [[1,2017,6,15,18]]

prediction = model.predict(sample)

print("\n========== SAMPLE PREDICTION ==========")

print("Input")

print("Junction :", sample[0][0])
print("Year :", sample[0][1])
print("Month :", sample[0][2])
print("Day :", sample[0][3])
print("Hour :", sample[0][4])

print("\nPredicted Vehicles :", round(prediction[0]))