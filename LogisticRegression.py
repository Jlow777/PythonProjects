import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

train = pd.read_csv('titanic_train.csv')

# Heat Map when the values are NULL, so you can see what data gaps exist
# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
# plt.show()

sns.set_style('whitegrid')
# Explore different data categories
# sns.countplot(x='Survived', hue='Pclass', data=train)
# sns.distplot(train['Age'].dropna(),kde=False,bins=30)
# plt.show()

# Cleaning Data
# sns.boxplot(x='Pclass', y='Age', data=train)
# plt.show()

# Below gets rid of all previously missing data for the age column, which had null values prior
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else: return 24

    else:
        return Age

train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis=1)

# Simple column drops or na value drops
train.drop('Cabin', axis=1, inplace=True)
train.dropna(inplace=True)

# sns.heatmap(train.isnull(), yticklabels=False, cbar=False)
# plt.show()

# Convert discrete categories into numerical values and drop duplicate discrete columns + extra junk
sex = pd.get_dummies(train['Sex'], drop_first=True)
embark = pd.get_dummies(train['Embarked'], drop_first=True)
train = pd.concat([train, sex, embark], axis=1)
train.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
train.drop('PassengerId', axis=1, inplace=True)
# print(train.head())

X = train.drop('Survived', axis=1)
y = train['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=101)
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

predictions = logmodel.predict(X_test)

print(classification_report(y_test, predictions))