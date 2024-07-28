#8.implement a linear regression model for regression tasks and Train the model on a dataset with continuous target variables.(sales.csv dataset)

data set link : https://drive.google.com/file/d/1saEPOz3__YKBIT8Z4sb5eXzqCpwsobBv/view?usp=sharing

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
data = pd.read_csv('sales.csv')
x = data[['Temperature']] 
y = data['Sales']
model = linear_model.LinearRegression()
model.fit(x,y)
predictions=model.predict(x)
plt.scatter(x, y) 
plt.plot(x,predictions,color='red') 
plt.xlabel('Temperature') 
plt.ylabel('Sales')
plt.show()
print('Coefficients:', model.coef_) 
print('Intercept:',model.intercept_)
