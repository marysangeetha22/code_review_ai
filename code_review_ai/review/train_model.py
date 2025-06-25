import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load the dataset
df = pd.read_csv("code_quality_dataset.csv")

# Features and target
X = df[["loc", "docstring_present", "indent_issues", "total_pylint_warnings"]]
y = df["score"]

# Split for training and evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"✅ Model trained. MSE on test set: {mse:.2f}")

# Save model
joblib.dump(model, "code_quality_model.pkl")
print("📦 Model saved as code_quality_model.pkl")
