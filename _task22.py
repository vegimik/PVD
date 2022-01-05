import pandas as pd
import numpy as np
import _task1 as _task1
import time
import helper_functions as hf
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

from sklearn.linear_model import LinearRegression



#***************************************************************************
def getDataSetFromatted():
    dataset = _task1.preProcessingOfData()
    
    # Create a DataFrame object
    datasetDfObj = pd.DataFrame(dataset, columns=[ 'mileage','make','model','fuel','gear','offerType','price','hp','year'])
    return datasetDfObj



#***************************************************************************
#1. Detrend by Differencing

def DetrendByDifferencing():
    dataset = getDataSetFromatted()
    data = np.array(dataset[['mileage','year']])
    #series = read_csv(data, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    X = data#.values
    diff = list()
    for i in range(1, len(X)):
        value = X[i] - X[i - 1]
        diff.append(value)
    pyplot.plot(diff)
    pyplot.show()

    
    
#***************************************************************************
#2. Detrend by Model Fitting

def DetrendByModelFitting():
    dataset = getDataSetFromatted()
    data = np.array(dataset[['mileage','year']])
    #series = read_csv(data, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    #X = #.values

    series =data #read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    # fit linear model
    X = [i for i in range(0, len(series))]
    X = np.reshape(X, (len(X), 1))
    y = series#.values
    model = LinearRegression()
    model.fit(X, y)
    # calculate trend
    trend = model.predict(X)
    # plot trend
    pyplot.plot(y)
    pyplot.plot(trend)
    pyplot.show()
    # detrend
    detrended = [y[i]-trend[i] for i in range(0, len(series))]
    # plot detrended
    pyplot.plot(detrended)
    pyplot.show()



def init_task22():
    DetrendByDifferencing()
    DetrendByModelFitting()

init_task22()









