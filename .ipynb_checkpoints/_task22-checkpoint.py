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

#***************************************************************************
def getDataSetFromatted():
    dataset = _task1.preProcessingOfData()
    
    # Create a DataFrame object
    datasetDfObj = pd.DataFrame(dataset, columns=[ 'mileage','make','model','fuel','gear','offerType','price','hp','year'])
    return datasetDfObj


#***************************************************************************
# Function to Detection Outlier on one-dimentional datasets.
#1. Method 1 — Standard Deviation:
def standardDeviationMethod1(col="mileage"):
    dataset = _task1.preProcessingOfData()

    # Create a DataFrame object
    datasetDfObj = pd.DataFrame(dataset, columns=[ 'mileage','make','model','fuel','gear','offerType','price','hp','year'])
    random_data = datasetDfObj[col]

    #define a list to accumlate anomalies
    anomalies = []
    
    # Set upper and lower limit to 3 standard deviation
    random_data_std = np.std(random_data)
    random_data_mean = np.mean(random_data)
    anomaly_cut_off = random_data_std * 1
    
    lower_limit  = random_data_mean - anomaly_cut_off 
    upper_limit = random_data_mean + anomaly_cut_off*3
    print('Lower_limit: ', lower_limit) 
    print('Upper_limit: ', upper_limit)
    # Generate outliers
    for outlier in random_data:
        if outlier > upper_limit or outlier < lower_limit:
            anomalies.append(outlier)
        
    print('Records with anomalies[Found ',len(anomalies),' records]: \n', anomalies)
    return anomalies



#***************************************************************************
#2. Method 2 — Boxplots

def standardDeviationMethod2():
    print('Method 2 — Boxplots(multidimensional):\n\n')
    dataset = getDataSetFromatted()
    sns.boxplot(data=random_data)



#***************************************************************************
#3. Method 3— DBScan Clustering(single or multi-dimensional):
#DBScan has three important concepts:
#    a)Core Points
#    b)Border Points
#    c)Noise Points

def standardDeviationMethod3():
    print('Method 3— DBScan Clustering:\n\n')
    dataset = getDataSetFromatted()
    data = np.array(dataset[['mileage','year']])
    print(data.shape)
    print('Result by DBScan is :')
    outlier_detection = DBSCAN(min_samples = 2, eps = 3)
    clusters = outlier_detection.fit_predict(data)
    list(clusters).count(-1)
    print(clusters)
    print(list(clusters).count(-1))



def init_task21():
    print(standardDeviationMethod1())
    standardDeviationMethod2()
    standardDeviationMethod3()





