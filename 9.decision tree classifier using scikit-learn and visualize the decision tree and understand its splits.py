#9.decision tree classifier using scikit-learn and visualize the decision tree and understand its splits. (User_Data.csv dataset)

data set link = https://drive.google.com/file/d/11ZT6wIImvKe7lpjysRIeWMbydxjjd9Ff/view?usp=sharing

import numpy as nm
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
#importing datasets 
data_set=pd.read_csv('User_Data.csv') 
#Extracting Independent and dependent Variable 
x=data_set.iloc[:, [2,3]].values
y=data_set.iloc[:, 4].values
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0) 
from sklearn.preprocessing import StandardScaler
st_x=StandardScaler() 
x_train=st_x.fit_transform(x_train) 
x_test=st_x.transform(x_test) 
print(len(x_train)) 
print(len(x_test))
from sklearn.tree import DecisionTreeClassifier 
classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(x_train, y_train)
y_pred=classifier.predict(x_test)
from sklearn.metrics import confusion_matrix 
cm=confusion_matrix(y_test,y_pred) 
print(cm)
from sklearn import tree
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(25, 20))
tree.plot_tree(classifier, filled=True, feature_names=['Age', 'EstimatedSalary'], class_names=['No', 'Yes'], fontsize=10)
plt.show()
