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
import _task4 as _task4
from ydata_quality import DataQuality

# ==================================================================
#	1.	Para-procesimi për pregaditjen e të dhënave për analizë
print('TASK 1')
_task1.preProcessingOfData()


# ==================================================================


# ==================================================================
#	2. Mbledhja e të dhënave, definimi i tipeve të të dhënave,kualiteti i të dhënave.
print('TASK 2')

# Define Data Types for dataset
_task2.init_task2()


# ==================================================================


# ==================================================================
#	3.	Integrimi, agregimi, mostrimi, pastrimi, identifikimi dhe strategjia e trajtimit për vlerat e zbrazëta.
print('TASK 3')
_task3.ini_task3()


# ==================================================================


# ==================================================================
#	4.	Reduktimi i dimensionit, zgjedhja e nënbashkësisë së vetive, krijimi i vetive, diskretizimi dhe binarizimi, transformimi.
print('TASK 4')
_task4.ini_task4()


# ==================================================================





