import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import m2cgen as m2c

# Load the data from the csv file
df = pd.read_csv("Nor_Mal.csv")

# Extract the input features (1st to 25th column)
X = df.iloc[:, 0:24].values

# Extract the target column (26th column)
y = df.iloc[:, 25].values

# Train the Decision Tree model
dt_model = DecisionTreeClassifier()
dt_model.fit(X, y)

# Make predictions using the Decision Tree model
dt_predictions = dt_model.predict(X)

# Calculate the accuracy of the Decision Tree model
dt_accuracy = accuracy_score(y, dt_predictions)
print("Decision Tree accuracy:", dt_accuracy)

# Convert the Decision Tree model to Python code using m2cgen
dt_code = m2c.export_to_python(dt_model)
with open("decision_tree_model.py", "w") as f:
    f.write(dt_code)