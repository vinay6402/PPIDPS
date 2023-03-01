import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import m2cgen
# load data from CSV file
data = pd.read_csv('Nor_Mal.csv')

# split data into input (X) and output (y) variables
X = data.iloc[:, :24]
y = data.iloc[:, 25]

# split data into training and testing sets
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = X
X_test = X
y_train = y
y_test = y
# initialize and train the six models
models = [
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    SVC(),
    LogisticRegression(),
    GaussianNB(),
    KNeighborsClassifier()
]

for model in models:
    model.fit(X_train, y_train)

# evaluate each model on several metrics
metrics = ['accuracy_score', 'precision_score', 'recall_score', 'f1_score', 'roc_auc_score']
results = pd.DataFrame(columns=['model', 'metric', 'score'])

for i, model in enumerate(models):
    y_pred = model.predict(X_test)
    scores = [model.__class__.__name__]
    for metric in metrics:
        score = globals()[metric](y_test, y_pred)
        scores.append(score)
        results = results.append({'model': model.__class__.__name__, 'metric': metric, 'score': score}, ignore_index=True)
    print('Model:', model.__class__.__name__)
    print('Metrics:', dict(zip(metrics, scores[1:])))
    print()

# create a table comparing the performance of each model on each metric
table = pd.pivot_table(results, values='score', index=['model'], columns=['metric'])
print(table)

# identify the best-performing model based on the evaluation metrics
best_model = table.mean(axis=1).idxmax()
print('Best model:', best_model)
