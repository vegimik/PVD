import pandas as pd
import numpy as np
import helper_functions as hf
import _task1 as _task1
from ydata_quality import DataQuality
import time
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#%matplotlib inline

# Driver method
def ini_task3():
    integrationAndaggregationFunc()
    sampleCleaningIdentifyingStrategies()

def integrationAndaggregationFunc():
    ### READ IN THE 3 DATA SETS ###
    # dataset containing some information on atuoscout240-data/manufacture from the files
    dataset = _task1.preProcessingOfData()
    # dataset containing information on returned orders
    #returns = pd.read_excel('autoscout24-germany-dataset-merged.csv')
    # dataset containing information on the managers for each region in the orders dataset
    brands =  hf.readManufacturers()
    datasetDfObj = pd.DataFrame(brands, columns=[ 'mark','country','year'])
    datasetDfObj=datasetDfObj.astype({'mark': 'string', 'country': 'string', 'year':'int64'})

    ###  Merge the datasets together ###

    ###  Merge the datasets together ###
    print('--------------------MERGING DATA-------------------------')

    # merged_df = (dataset.merge(brands, how='left', on=['mark', 'country']))
    merged_df=pd.merge(dataset, brands, how="right", on=["mark"])
    merged_df.to_csv('autoscout24-germany-dataset-merged.csv', index=False)

    print('Merged data output to data/output_data/merged_data.csv')
    print('---------------------------------------------------------')

    ### FILTERING EXAMPLES ###
    print('----------FILTERING EXAMPLE 1: NOT RETURNED--------------')

    #not_returned_df = merged_df.loc[merged_df['country'].isna(), :]
    not_returned_df=merged_df.dropna()

    #not_returned_df.to_csv('autoscout24-germany-dataset-merged-filtered.csv', index=False)

    print('Result output to autoscout24-germany-dataset-merged-filtered.csv')
    print('---------------------------------------------------------')



    ### AGGREGATION?GROUPBY EXAMPLES ###

    print('----------AGGREGATION EXAMPLE 1: MEAN()-----------------')

    agg_example_1 = not_returned_df.groupby(by='country')['price'].mean()

    print(agg_example_1)

    print('---------------------------------------------------------')


    print('------------AGGREGATION EXAMPLE 2: AGG()-----------------')

    agg_example_2 = not_returned_df.groupby(by='country').agg({'mileage':'mean','year_x':'median'})

    print(agg_example_2)

    print('---------------------------------------------------------')
    
    
# Mostrimi, pastrimi, identifikimi dhe strategjia e trajtimit për vlerat e zbrazëta
def sampleCleaningIdentifyingStrategies():
    filteredDataset =  hf.readMergedDataset()
    # generating one row 
    sample1 = filteredDataset.sample(n = 5)  
    # display
    print(sample1)

    # generating another row
    sample2 = filteredDataset.sample(frac =.25)
    # display
    print(sample2)

    print('Checking if sample is 0.25 times data or not')
    if (0.25*(len(filteredDataset))== len(sample2)):
        print( "Checked, sample is 0.25 times data!")
        print(len(filteredDataset), len(sample2))

    # Chose how many index include for random selection
    chosen_idx = np.random.choice(4, replace = True, size = 6)
    print(filteredDataset.iloc[chosen_idx])    
    hf.missing_cols(filteredDataset)

    print('\n Decsibe filter dataset for price')
    filteredDataset['price'].describe()

    print('\n In this histogram, you can see that most of the data is around 0 to 5000')
    plt.figure(figsize=(10, 6))
    filteredDataset['price'].hist(bins=100)

    print('\n As you can see, the price column has multiple data points that are outliers (above of the maximum in the boxplot)')
    plt.figure(figsize=(10, 6))
    filteredDataset.boxplot(column=['price'])
    plt.figure(figsize=(10, 6))
    filteredDataset['mark'].value_counts().plot.bar()
    print(filteredDataset.isnull())
    filteredDataset1 = filteredDataset[filteredDataset.isna().any(axis=1)]
    print(filteredDataset1)

    print('\n Clean up filtered dataset, deleted null values')
    filteredDataset=filteredDataset.dropna()
    hf.missing_cols(filteredDataset)



    
    
