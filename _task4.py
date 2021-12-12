import pandas as pd
import numpy as np
import _task1 as _task1
import time
import helper_functions as hf

def reductionAndSubset():
    ### READ IN THE 3 DATA SETS ###
    # dataset containing some information on atuoscout240-data/manufacture from the files
    dataset = _task1.preProcessingOfData()
    print("The Shape of Dataset:")
    print(dataset.shape)
    print("Dataset type usage description:")
    print(dataset.describe(exclude='number'))
    
reductionAndSubset()

#Uniform Manifold Approximation and Projection (UMAP)
dataset = _task1.preProcessingOfData()

print("Data Reduction started for Main Data Set.")
wanted_data_volume = ['mark', 'model','fuel','gear','offerType']
print("Dimensionality reduction.")
print(f"Wanted columns:\n {wanted_data_volume}")
print("Data Reduction has been successfully reducted.\n")
dataset = dataset[list(wanted_data_volume)]

print("Subset Properties \nDropping same row vaules of new subset...")
dataset = dataset.drop_duplicates(subset=wanted_data_volume,keep=False)

print("Showing up the subset...")
dataset.rename(columns={'DisplayName': 'Subset'},inplace=True)
print(dataset)

filter = "COUNT > 500"
field_properties = "Field1 FLOAT true;Field2 STRING true;Field3 DOUBLE true"
file_extenstion = "csv"
has_header_row = True
file_encoding = "UTF-8"

