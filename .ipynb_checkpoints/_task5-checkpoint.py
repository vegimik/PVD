#Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import _task1 as _task1
import statsmodels.api as sm

def identifyVariables():
    #Load the data
    dataset = _task1.preProcessingOfData()
    #get an overview of the data
    dataset.head()
    dataset.tail()
    dataset.sample(10)

    #identify variable type
    dataset.dtypes
    dataset.info()
    dataset.describe()

identifyVariables()

#Univariate analysis
#summary statistics of the data
include =['object', 'float', 'int'] 
dataset = _task1.preProcessingOfData()
dataset.describe(include=include)
dataset.describe()

#count of values in a categorical variable
dataset.price.value_counts()
dataset.year.hist(figsize=(10,5))


#UNIVARIATE SCATTER PLOT
plt.scatter(dataset['year'],dataset['price'])
plt.show()

#Bivariate analysis
#create correlation matrix
dataset.corr()

#Simple Linear Regression

#define response variable
y = dataset['price']

#define explanatory variable
x = dataset[['year']]

#add constant to predictor variables
x = sm.add_constant(x)

#fit linear regression model
model = sm.OLS(y, x).fit()

#view model summary
print(model.summary())

dataset.hist(bins=50, figsize=(30,20));