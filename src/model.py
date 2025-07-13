import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os
import numpy as np  # ✅ Add this

# Step 1: Load cleaned data
df = pd.read_csv('data/traffic_cleaned.csv')

# Step 2: Features and Target
X = df.drop(columns=['vehicle_count', 'timestamp'])
y = df['vehicle_count']

# Step 3: Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Predict and evaluate
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # ✅ Fixed for older sklearn
r2 = r2_score(y_test, y_pred)

print(f"✅ Model Trained Successfully!")
print(f"📊 MAE: {mae:.2f}")
print(f"📊 RMSE: {rmse:.2f}")
print(f"📊 R² Score: {r2:.2f}")

# Step 6: Save the model
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/traffic_model.pkl')
print("📦 Model saved to model/traffic_model.pkl")
