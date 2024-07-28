#5.Visualize the dataset to gain insights using Matplotlib or Seaborn by plotting scatter plots, bar charts(User_data.csv dataset)

data set link = https://drive.google.com/file/d/11ZT6wIImvKe7lpjysRIeWMbydxjjd9Ff/view?usp=sharing

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
user_data=pd.read_csv('User_Data.csv') 
print(user_data.head())
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='EstimatedSalary', data=user_data) 
plt.title('Scatter Plot of Age vs. Income')
plt.xlabel('Age') 
plt.ylabel('EstimatedSalary')
plt.grid(True) 
plt.show()
plt.figure(figsize=(8, 6))
sns.histplot(data=user_data, x= 'Age', bins=20, kde=True, color='skyblue') 
plt.title('Histogram of Age Distribution')
plt.xlabel('Age') 
plt.ylabel('Frequency') 
plt.grid(True) 
plt.show()
plt.figure(figsize=(8, 6)) 
sns.countplot(data=user_data, x='Gender') 
plt.title('Bar Chart of Gender Distribution') 
plt.xlabel('Gender')
plt.ylabel('Count') 
plt.grid(True)
