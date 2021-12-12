import pandas as pd
import numpy as np
import helper_functions as hf
import _task1 as _task1
from ydata_quality import DataQuality

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn import cluster
from subprocess import check_output


def init_task2():
    defineDataTypesFunc()
    qualityOfData()
    
    
def defineDataTypesFunc():
    # List of Tuples    
    dataset = _task1.preProcessingOfData() #hf.readDataset()
    
    # Create a DataFrame object
    datasetDfObj = pd.DataFrame(dataset, columns=[ 'mileage','make','model','fuel','gear','offerType','price','hp','year'])
    print("Contents of the Dataframe : ")
    print(datasetDfObj)
    print('*** Get the Data type of each column in Dataframe ***')
    # Get a Series object containing the data type objects of each column of Dataframe.
    # Index of series is column name.
    dataTypeSeries = datasetDfObj.dtypes
    print('Data type of each column of Dataframe :')
    print(dataTypeSeries)
    # Get a Dictionary containing the pairs of column names & data type objects.
    dataTypeDict = dict(datasetDfObj.dtypes)
    print('Data type of each column of Dataframe :')
    print(dataTypeDict)
    print('*** Get the Data type of a single column in Dataframe ***')
    # get data type of column 'Price'
    dataTypeObj = datasetDfObj.dtypes['price']
    print('Data type of each column Price in the Dataframe :')
    print(dataTypeObj)
    print('\n*** Check if Data type of a column is int64 or object etc in Dataframe ***')
    # Check the type of column 'Price' is int64
    if dataTypeObj == np.int64:
        print("Data type of column 'Price' is int64")
    # Check the type of column 'HoursPower' is object i.e string
    if datasetDfObj.dtypes['hp'] == np.float64:
        print("Data type of column 'hp' is float")
    print('Change the data types for multiple fields to boolean')
    datasetDfObj=datasetDfObj.astype({'make': 'string', 'model': 'string', 'fuel':'string', 'gear':'string',  'offerType':'string', 'hp':'int64', 'price':'float64', 'mileage':'float64'})
    print('\nDetermine count of unique values for each column in the dataframe')
    print(dataset.nunique())
    print('\n*** Get the Data type of each column in Dataframe using info() ***')
    # Print complete details about the data frame, it will also print column count, names and data types.
    datasetDfObj.info()
    return dataset
    
    
    
    
#===================================================================================================
# Quality of data

def qualityOfData():
    #Load in the data
    df = defineDataTypesFunc()[0:100] #_task1.preProcessingOfData()[0:100]

    print('Number of rows and columns as a tuple (number of rows, number of columns)')
    print(df.shape) 
    print(df.duplicated(subset='model').sum())
    print(len(df))
    df = df.drop_duplicates(subset='model')
    print(len(df))
    
    print('Show the relations between prices and mark/brand')
    df = df.sort_values('mark', ascending=True)
    df.plot(x='mark',y='price',style='o',alpha=0.4,legend=False)
    plt.xticks(rotation='horizontal')
    plt.xlabel('Mark(Brand)', fontsize=12)
    plt.ylabel('Price', fontsize=12)
    plt.show()
    
    #print(df.isnull().sum())

    print('Here we can see the variations price of cars for itself mileages')
    df['Group'] = df['year'].apply(lambda x: hf.group_years(x))
    colors = {'A':'#080707','B':'#282626','C':'#3d3939','D':'#686666','E':'#797777','F':'#a9a9a3','G':'#bebfc1','H':'#d2d2d2'}
    fig, ax = plt.subplots()
    ax.scatter(df['price'],df['mileage'], c=df['Group'].apply(lambda x: colors[x]),alpha=0.6)
    plt.xlabel('PriceS', fontsize=12)
    plt.ylabel('Mileages', fontsize=12)
    plt.show()

    df=df.dropna()
    df.info()

    # create a DataQuality object from the main class that holds all quality modules
    #dq = DataQuality(df=df)

    # run the tests and outputs a summary of the quality tests
    #result=dq.evaluate()
