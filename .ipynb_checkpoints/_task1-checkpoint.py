import numpy as np
import matplotlib.pyplot as plt
import helper_functions as hf


def preProcessingOfData():
    dataset = hf.readDataset()
    _oldDataSet=dataset
    print('=> Take a look at the first few rows')
    print(dataset.head())
    print(dataset.isnull().sum())

    print('\n')
    print('=> Header tbl:  mileage(analysed before), make,   model,  fuel,  gear, offerType,  price,   hp,  year')
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
    

    print('\n')
    print('Filling a null values using fillna')
    dataset["model"].fillna("Model", inplace = True) 
    dataset["model"].replace(to_replace = 'Model', value ='Other') 
    # Fill NaN values with a mean value
    #dataset['col'] = dataset['model'].fillna(dataset['make'].mean())
    dataset["gear"].fillna("Manual", inplace = True) 
    #dataset["hp"].fillna("0", inplace = True)  
    
    # Rename a column
    dataset = dataset.rename(columns={'make': 'mark'})

    print('Using dropna() function')
    dataset=dataset.dropna()

    
    print('=> Take a look at the first few rows')
    print(dataset.head())
    print(dataset.isnull().sum())
    
    print('\n')
    print("Old data frame length:", len(_oldDataSet))
    print("New data frame length:", len(dataset))
    print("Number of rows with at least 1 NA value: ", (len(_oldDataSet)-len(dataset)))

    
    return dataset
    
    