
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


df = pd.read_csv('Classified Data', index_col=0)

scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
# Standard scale transformation, which is more apparent when values are significantly larger / smaller
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))
# This step gives you the standardized version of the data, ready for ML algorithm
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])

X = df_feat
y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit(X_train, y_train)
#
# pred = knn.predict(X_test)
# print(confusion_matrix(y_test, pred))
# print(classification_report(y_test, pred))

# error_rate = []
#
# for i in range(1,40):
#
#     knn = KNeighborsClassifier(n_neighbors=i)
#     knn.fit(X_train, y_train)
#     pred_i = knn.predict(X_test)
#     error_rate.append(np.mean(pred_i != y_test))
#
# plt.figure(figsize=(10,6))
# plt.plot(range(1,40), error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
# plt.title('Error Rate vs K Value')
# plt.xlabel('K')
# plt.ylabel('Error Rate')
# plt.show()
# k = 17 ends up being close to a minimum error rate value


knn = KNeighborsClassifier(n_neighbors=17)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))