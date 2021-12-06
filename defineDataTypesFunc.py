import pandas as pd
import numpy as np
import helper_functions as hf



def defineDataTypesFunc():
    # List of Tuples    
    dataset = hf.readDataset()
    
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
    print('*** Check if Data type of a column is int64 or object etc in Dataframe ***')
    # Check the type of column 'Price' is int64
    if dataTypeObj == np.int64:
        print("Data type of column 'Age' is int64")
    # Check the type of column 'Name' is object i.e string
    if datasetDfObj.dtypes['make'] == np.object:
        print("Data type of column 'Make' is object")
    print('** Get list of pandas dataframe columns based on data type **')
    # Get  columns whose data type is object i.e. string
    filteredColumns = empDfObj.dtypes[datasetDfObj.dtypes == np.object]
    # list of columns whose data type is object i.e. string
    listOfColumnNames = list(filteredColumns.index)
    print(listOfColumnNames)
    print('*** Get the Data type of each column in Dataframe using info() ***')
    # Print complete details about the data frame, it will also print column count, names and data types.
    datasetDfObj.info()
    
    
    
    