# Week 1 Project - IoT Sensor Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# =======================
# Load datasets
# =======================
relay_temp = pd.read_csv("25th Relay and Temp measurement.csv")
solar_irr = pd.read_csv("SolarIradOutdoorIndoor.csv")
doublet_data = pd.read_excel("DoubletTestDataSet.ods", engine="odf")

# =======================
# Data Cleaning
# =======================
relay_temp['time'] = pd.to_datetime(relay_temp['time'])

print("Relay & Temp Data Summary:")
print(relay_temp.describe())

print("\nSolar Irradiance Data Summary:")
print(solar_irr.describe())

print("\nDoublet Data Summary:")
print(doublet_data.describe())

# =======================
# Visualization
# =======================
# Indoor Temperature over Time
plt.figure(figsize=(12, 5))
plt.plot(relay_temp['time'], relay_temp['y (Tin)'], label="Indoor Temp")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Indoor Temperature vs Time")
plt.legend()
plt.show()

# Solar Irradiance vs Outdoor Temp
plt.figure(figsize=(8, 5))
sns.scatterplot(x=solar_irr['Solar irradiance'], y=solar_irr['OutTemp'])
plt.title("Solar Irradiance vs Outdoor Temperature")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(solar_irr.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix - Solar Data")
plt.show()

# =======================
# Machine Learning Model
# =======================
# Predict Outdoor Temp from Solar Irradiance + Wind Speed
X = solar_irr[['Solar irradiance', 'Wind speed [m/s]']]
y = solar_irr['OutTemp']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nModel Evaluation:")
print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

# Plot predictions vs actual
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.xlabel("Actual Temperature (°C)")
plt.ylabel("Predicted Temperature (°C)")
plt.title("Actual vs Predicted Outdoor Temperature")
plt.show()
