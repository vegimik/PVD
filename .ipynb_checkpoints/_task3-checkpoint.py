import pandas as pd
import numpy as np
import helper_functions as hf
import _task1 as _task1
from ydata_quality import DataQuality
import time

    

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

    merged_df = (dataset.merge(brands, how='left', on='mark').merge(brands, how='left', on='country'))
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

    agg_example_2 = not_returned_df.groupby(by='country').agg({'mileage':'mean','year':'median'})

    print(agg_example_2)

    print('---------------------------------------------------------')

