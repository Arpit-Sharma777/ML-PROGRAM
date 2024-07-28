#6.Handle missing data, encode categorical variables, and perform feature scaling.

!pip install category_encoders
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler 
from category_encoders import OneHotEncoder 
data={'age': [25, 30, None, 35, 40],
      'gender': ['Male', 'Female', 'Male', 'Female', None], 
      'income': [50000, 60000, 70000, None, 80000],
      'education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master']}
df=pd.DataFrame(data) 
imputer=SimpleImputer(strategy='mean')
df[['age', 'income']] = imputer.fit_transform(df[['age', 'income']])
encoder=OneHotEncoder(cols =['gender', 'education'], use_cat_names=True) 
df_encoded=encoder.fit_transform(df)
scaler=StandardScaler()
df_scaled=pd.DataFrame(scaler.fit_transform(df_encoded[['age', 'income']]), columns=['age', 'income']) 
df_final=pd.concat([df_scaled, df_encoded.drop(['age', 'income'], axis=1)], axis=1)
print("Final DataFrame:")
print(df_final)
