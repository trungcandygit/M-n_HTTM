# SOURCE: https://github.com/AnjanaAbY/Drug-Classification-Model
# Notebook: MachineLearning_Task_2.ipynb
# 6 models: LogisticRegression, DecisionTree, RandomForest, KNN, SVM, NaiveBayes
# Accuracy results: DT=98.33%, RF=98.33%, LR=90%, NB=85%, SVM=70%, KNN=63.33%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

# Load & preprocess
ds = pd.read_csv("drug200.csv")
print("Null values:\n", ds.isnull().sum())

sex_encoding = preprocessing.LabelEncoder()
ds['Sex'] = sex_encoding.fit_transform(ds['Sex'])
BP_encoding = preprocessing.LabelEncoder()
ds['BP'] = BP_encoding.fit_transform(ds['BP'])
Cholesterol_encoding = preprocessing.LabelEncoder()
ds['Cholesterol'] = Cholesterol_encoding.fit_transform(ds['Cholesterol'])

xcols = [col for col in ds.columns if col not in ['Drug']]
x = ds[xcols]
y = ds['Drug']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=3)

# Helper function
def calculate_additional_metrics(model_name, y_true, y_pred):
    precision = metrics.precision_score(y_true, y_pred, average='weighted')
    recall = metrics.recall_score(y_true, y_pred, average='weighted')
    f1_score = metrics.f1_score(y_true, y_pred, average='weighted')
    print(f"{model_name} - Additional Metrics:")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-Score: {f1_score}\n")

# Logistic Regression
logireg = LogisticRegression()
logireg.fit(x_train, y_train)
lr_prediction = logireg.predict(x_test)
print("LogisticRegression's Accuracy: ", metrics.accuracy_score(y_test, lr_prediction))
calculate_additional_metrics('Logistic Regression', y_test, lr_prediction)

# Decision Tree
dectree = DecisionTreeClassifier()
dectree.fit(x_train, y_train)
dr_prediction = dectree.predict(x_test)
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_test, dr_prediction))
calculate_additional_metrics('Decision Tree', y_test, dr_prediction)

# Random Forest
ranforest = RandomForestClassifier()
ranforest.fit(x_train, y_train)
rf_prediction = ranforest.predict(x_test)
print("Random Forest's Accuracy:", metrics.accuracy_score(y_test, rf_prediction))
calculate_additional_metrics('Random Forest', y_test, rf_prediction)

# KNN
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
knn_prediction = knn.predict(x_test)
print("KNN's Accuracy:", metrics.accuracy_score(y_test, knn_prediction))
calculate_additional_metrics('KNN', y_test, knn_prediction)

# SVM
svm = SVC()
svm.fit(x_train, y_train)
svm_prediction = svm.predict(x_test)
print("SVM's Accuracy:", metrics.accuracy_score(y_test, svm_prediction))
calculate_additional_metrics('SVM', y_test, svm_prediction)

# Naive Bayes
naivebayes = GaussianNB()
naivebayes.fit(x_train, y_train)
nb_prediction = naivebayes.predict(x_test)
print("Naive Bayes' Accuracy:", metrics.accuracy_score(y_test, nb_prediction))
calculate_additional_metrics('Naive Bayes', y_test, nb_prediction)

# New patient prediction
new_patient_data = pd.DataFrame({'Age':[30], 'Sex':'F', 'BP':['NORMAL'],
                                 'Cholesterol':['HIGH'], 'Na_to_K':[15.0]})
new_patient_data['Sex'] = sex_encoding.fit_transform(new_patient_data['Sex'])
new_patient_data['BP'] = BP_encoding.fit_transform(new_patient_data['BP'])
new_patient_data['Cholesterol'] = Cholesterol_encoding.fit_transform(new_patient_data['Cholesterol'])
