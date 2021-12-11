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
    
    #clean data inside dataFrame, and treate data


def cleanCarDataSet():
    data = hf.readDataset()
    # fill missing data
    print("Treating missing values")
    data["model"].fillna('Unknown', inplace=True)
    data["gear"].fillna('Unknown', inplace=True)
    data["hp"].fillna('0', inplace=True)

    #drop rows that are duplicates
    print("Duplicate Rows :")
    print(data.duplicated())
    print(data.duplicated().sum())
    print("Removing duplicates....")
    data.drop_duplicates(inplace=True)
    print(data.duplicated().sum())
    print("Duplicates removed successfully!")

    print("Dataset column type definition in process...\n")
    # defining column types: mileage,make,model,fuel,gear,offerType,price,hp,year
    data['mileage'] = data['mileage'].astype(float)
    data['make'] = data['make'].astype("string")
    data['model'] = data['model'].astype("string")
    data['fuel'] = data['fuel'].astype("string")
    data['gear'] = data['gear'].astype("string")
    data['offerType'] = data['model'].astype("string")
    data['price'] = data['mileage'].astype(float)
    data['hp'] = data['mileage'].astype(int)
    data['year'] = data['fuel'].astype("string")

    # fill missing data and transforming data addin , at thousand seperator
    #data['millage'] = f'{data['millage']:,}'

    print("Dataset has successfully gone into the proccess of cleaning.\n")

    return data

cleanCarDataSet()

data = hf.readDataset()
#We check if we have both unkonwn values in make and model, because they'd be useless for us
sameMakeAndModel = data['make'] == data['model']
print(sameMakeAndModel)
sameMakeAndModel[sameMakeAndModel.astype(str).str.contains('True') ]