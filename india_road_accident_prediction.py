# -*- coding: utf-8 -*-
"""India Road Accident Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Eqaxdn9I7yA8HTxxvJ0FvOeKOiztAwu2
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('accident_prediction_india.csv')

df.head()

df.shape

df.columns

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()

df['Accident Severity'].value_counts(normalize=True)

sns.set_style('whitegrid')
plt.figure(figsize=(10,5))
sns.countplot(x=df['Accident Severity'], palette=['red', 'green', 'blue'])  # One color per bar
plt.title('Distribution of Accident Severity', fontsize=15)
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(x=df['Accident Severity'], hue=df['Driver Gender'], palette='Reds')
plt.title('Distribtution of Accident Severity vs Driver Gender', fontsize=15)
plt.show()

plt.figure(figsize=(10,5))
plt.title('Distribtution of Accident Severity Over Year', fontsize=15)
sns.lineplot(x=df['Year'], y=df['Accident Severity'], color='orange')
plt.show()

plt.figure(figsize=(10,5))
plt.title('Distribtution of Accident Severity Over Day of Week', fontsize=15)
sns.lineplot(x=df['Day of Week'], y=df['Accident Severity'], color='skyblue')
plt.show()

plt.figure(figsize=(10,5))
plt.title('Distribtution of Accident Severity Over Month' , fontsize=15)
sns.lineplot(x=df['Month'] , y = df['Accident Severity'] , color='tomato')
plt.show()

df['Vehicle Type Involved'].value_counts()

plt.figure(figsize=(10,5))
plt.title('Vehicle Type Involved VS Accident Severity', fontsize=15)
sns.countplot(x=df['Vehicle Type Involved'],hue=df['Accident Severity'], palette='summer')
plt.show()

plt.figure(figsize=(10,5))
plt.title('Road Type  VS Accident Severity', fontsize=15)
sns.countplot(x=df['Road Type'],hue=df['Accident Severity'], palette='magma')
plt.show()

plt.figure(figsize=(10,5))
plt.title('Alcohol Involvement VS Accident Severity', fontsize=15)
sns.countplot(x=df['Alcohol Involvement'],hue=df['Accident Severity'], palette='copper')
plt.show()

df.head()

plt.figure(figsize=(10,5))
plt.title('Light Condition  VS Road Condition', fontsize=15)
sns.countplot(x=df['Lighting Conditions'], hue=df['Road Condition'])
plt.show()

plt.figure(figsize=(10,5))
top_vehicles = df['Vehicle Type Involved'].value_counts().nlargest(10)
sns.barplot(x=top_vehicles.index, y=top_vehicles.values , palette="rocket_r")
plt.xticks(rotation=45)
plt.title

plt.figure(figsize=(10,5))
plt.title('Corrlation of Numerical Colums' , fontsize=15)
num_df = df.select_dtypes(include=['number'])
sns.heatmap(num_df.corr(), cmap = 'copper',annot=True)
plt.xticks(rotation=75)
plt.show()

num_df.hist(figsize=(13,10))
plt.show()

df.columns

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, classification_report, recall_score, f1_score, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

le = LabelEncoder()

for col in ['State Name', 'City Name', 'Month', 'Day of Week',
       'Time of Day', 'Accident Severity',
       'Vehicle Type Involved',
       'Weather Conditions', 'Road Type', 'Road Condition',
       'Lighting Conditions', 'Traffic Control Presence',
       'Driver Gender', 'Driver License Status',
       'Alcohol Involvement', 'Accident Location Details']:
    df[col] =  le.fit_transform(df[col])

X = df.drop(columns='Accident Severity')
y = df['Accident Severity']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(),
    "Bagging Classifier": BaggingClassifier(),
    'Adaboost Classifier': AdaBoostClassifier(),
    'KNN': KNeighborsClassifier()
}

results = []
for name, model in models.items():
    model.fit(X_train,y_train)
    y_preds = model.predict(X_test)
    score = accuracy_score(y_test, y_preds)
    pre = precision_score(y_test, y_preds, average='macro')

    print(f"\n{name} Performance:")
    print("Accuracy:", score)
    print("Precision Score:", pre)


    results.append({
        'Model': name,
        'Accuracy': score,
        'Precision': pre
    })
    results_df = pd.DataFrame(results)

print("\nModel Evaluation Summary:")
results_df