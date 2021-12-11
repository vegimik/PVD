import pandas as pd
import numpy as np
import helper_functions as hf
import _task1 as _task1
from ydata_quality import DataQuality

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
        print("Data type of column 'Age' is int64")
    # Check the type of column 'HoursPower' is object i.e string
    if datasetDfObj.dtypes['hp'] == np.float64:
        print("Data type of column 'hp' is float")
    print('Change the data types for multiple fields to boolean')
    datasetDfObj=datasetDfObj.astype({'make': 'string', 'model': 'string', 'fuel':'string', 'gear':'string', 'offerType':'string'})
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

    # create a DataQuality object from the main class that holds all quality modules
    dq = DataQuality(df=df)

    # run the tests and outputs a summary of the quality tests
    result=dq.evaluate()
