import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('kyphosis.csv')


X = df.drop('Kyphosis', axis=1)
y = df['Kyphosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# Single decision tree model creation
# dtree = DecisionTreeClassifier()
# dtree.fit(X_train, y_train)
# predictions = dtree.predict(X_test)
# print(confusion_matrix(y_test, predictions))
# print('/n')
# print(classification_report(y_test, predictions))


# Random forest classifier model
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)
print(confusion_matrix(y_test, rfc_pred))
print('/n')
print(classification_report(y_test, rfc_pred))
