import numpy as np
import matplotlib.pyplot as plt
import helper_functions as hf

# Importing the class called SimpleImputer from impute model in sklearn
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

#2. 
import defineDataTypes as defineDataTypes


    
dataset = hf.readDataset()

# Take a look at the first few rows
print(dataset.head())
print(dataset.isnull().sum())



#header tbl:  mileage(analysed before), make,   model,  fuel,  gear, offerType,  price,   hp,  year
print(
    dataset['make'].isnull().head(),
    dataset['model'].isnull().head(),
    dataset['fuel'].isnull().head(),
    dataset['gear'].isnull().head(),
    dataset['offerType'].isnull().head(),
    dataset['price'].isnull().head(),
    dataset['hp'].isnull().head(),
    dataset['year'].isnull().head(),
)

print(dataset['mileage'])
print(dataset['mileage'].isnull())
print(dataset['mileage'].isnull().head())


# ==================================================================

#	2. Mbledhja e të dhënave, definimi i tipeve të të dhënave,kualiteti i të dhënave.

# Define Data Types for dataset
defineDataTypeObj.defineDataTypes()




# ==================================================================