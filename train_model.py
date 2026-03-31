import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy dataset (replace later with your real dataset)
X = np.random.rand(100, 9)   # 9 features (same as your app inputs)
y = np.random.rand(100)

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl created successfully")