#Import the libraries
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
%matplotlib inline
from scipy import stats


#***************************************************************************
def getDataSetFromatted():
    dataset = _task1.preProcessingOfData()
    
    # Create a DataFrame object
    datasetDfObj = pd.DataFrame(dataset, columns=[ 'mileage','make','model','fuel','gear','offerType','price','hp','year'])
    return datasetDfObj



#***************************************************************************
#1. Detect & Remove Outliers

def DetectRemoveOutliers():
    #1. Detect Outliers
    print('=> Detect Outliers\n')

    #Load the data
    dataset = getDataSetFromatted()

    #Find features and target
    x = dataset
    y = dataset['year']

    #Find the dic keys
    print(dataset.keys())

    #find features name
    columns = dataset.keys
    columns



    #Create dataframe
    dataset_df = pd.DataFrame(dataset)
    dataset_df_columns = columns
    dataset_df_o = dataset_df
    dataset_df.shape

    #Oulier detection - Univarite - Boxplot
    sns.boxplot(x=dataset_df['mileage'])

    #Check the correlation between features before multivariate outlier analysis
    %matplotlib inline

    plt.figure(figsize= (10,10), dpi=100)
    sns.heatmap(dataset_df.corr())

    #Multivariate outlier analysis
    fig, ax = plt.subplots(figsize=(16,8))
    ax.scatter(dataset_df['price'], dataset_df['year'])
    ax.set_xlabel('Proportion of non-retail business acres per town')
    ax.set_ylabel('Full-value property-tax rate per $10,000')
    plt.show()

    z = np.abs(stats.zscore(dataset_df))
    print(z)
    z.shape

    threshold = 3
    print(np.where(z > 3))

    #print(dataset_df[np.where(z > 3)])
    print(z[55][1])


    print('\n\n\n')
    print('=> Removing Outliers\n')

    dataset_df_o = dataset_df_o[(z < 3).all(axis=1)]
    dataset_df.shape


    dataset_df_o.shape

    dataset_df_o1 = dataset_df
    Q1 = dataset_df_o1.quantile(0.25)
    Q3 = dataset_df_o1.quantile(0.75)
    IQR = Q3 - Q1
    print(IQR)

    dataset_df_out = dataset_df_o1[~((dataset_df_o1 < (Q1 - 1.5 * IQR)) |(dataset_df_o1 > (Q3 + 1.5 * IQR))).any(axis=1)]

    dataset_df_out.shape

