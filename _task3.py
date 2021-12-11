from csv import reader
import pandas as pd
import statistics
import numpy as np
import helper_functions as hf
from datetime import datetime

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