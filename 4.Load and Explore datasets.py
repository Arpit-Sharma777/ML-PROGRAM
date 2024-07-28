#4.Load and Explore datasets (sample_data csv & sample_data.xlsx data sets)

csv file download = https://drive.google.com/file/d/1iyv2x5lXKrb6uUzYUO6zY0K3q4I7_4Av/view?usp=sharing
excel file download = https://docs.google.com/spreadsheets/d/1vsD8jRBym10-EaJCkKB71ZG7eEJnEAgp/edit?usp=sharing&ouid=110708829562479262129&rtpof=true&sd=true
import pandas as pd
# Define the file paths
csv_file_path = '/content/sample_data.csv' 
excel_file_path ='/content/sample_data.xlsx'
#Load the CSV file
data_csv = pd.read_csv(csv_file_path)
print("CSV File Data:")
print(data_csv)
#Load the Excel file
data_excel = pd.read_excel(excel_file_path)
print("\nExcel File Data:")
print(data_excel)
# Basic Data Exploration 
print("\nData Descriptions:") 
print("CSV Data Description:")
print(data_csv.describe())
print("\nExcel Data Description:")
print(data_excel.describe())
# Displaying data types 
print("\nData Types in CSV File:") 
print(data_csv.dtypes)
print("\nData Types in Excel File:")
print(data_excel.dtypes)
