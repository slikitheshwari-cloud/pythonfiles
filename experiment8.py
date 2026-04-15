import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
x = np.array([1,2,3,4,5,6,7]).reshape(-1,1)
y = np.array([50,55,65,70,75,85,95])

# Create and train model
model = LinearRegression()
model.fit(x, y)

# Predict values
y_pred = model.predict(x)

# Plot graph
plt.figure(figsize=(6,5))
plt.scatter(x, y, label="Actual Data")
plt.plot(x, y_pred, label="Regression Line")

# Show predicted values on graph
for i in range(len(x)):
    plt.text(x[i][0], y_pred[i], f"{y_pred[i]:.1f}")

# Labels and title
plt.title("Regression Plot with Predicted Values")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.legend()

# Display plot
plt.show()
