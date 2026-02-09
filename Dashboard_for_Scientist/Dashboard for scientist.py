import numpy as np
import pandas as pd

Diabetes_df = pd.read_csv("diabetes copy.csv")
print(f" The first five entries are: \n{Diabetes_df.head()}")
print(f"Number of Rows: \n{Diabetes_df.shape[0]}")
print(f"Number of Columns: \n{Diabetes_df.shape[1]}")
print(f"Overall Shape: \n{Diabetes_df.shape}")
print(f"All Columns Names and their Data Types of Columns:  \n{Diabetes_df.dtypes}")
print(f"Total Null Values : \n{Diabetes_df.isnull().sum().sum()}")
print(f" Column Wise Null Values Are: \n{Diabetes_df.isnull().sum()}")
