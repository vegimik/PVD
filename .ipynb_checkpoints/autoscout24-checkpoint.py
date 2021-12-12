import numpy as np
import matplotlib.pyplot as plt
import helper_functions as hf

# Importing the class called SimpleImputer from impute model in sklearn
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline

#2. 
import _task1 as _task1
import _task2 as _task2 
import _task3 as _task3
from ydata_quality import DataQuality

# ==================================================================

#	1.	Para-procesimi për pregaditjen e të dhënave për analizë

# Define Data Types for dataset
_task1.preProcessingOfData()




# ==================================================================

# ==================================================================

#	2. Mbledhja e të dhënave, definimi i tipeve të të dhënave,kualiteti i të dhënave.

# Define Data Types for dataset
_task2.init_task2()




# ==================================================================

# ==================================================================

#	3.	Integrimi, agregimi, mostrimi, pastrimi, identifikimi dhe strategjia e trajtimit për vlerat e zbrazëta.
_task3.ini_task3()

# ==================================================================







