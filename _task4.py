import pandas as pd
import numpy as np
import _task1 as _task1
import time
import helper_functions as hf
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.preprocessing import KBinsDiscretizer

def reductionAndSubset():
    ### READ IN THE 3 DATA SETS ###
    # dataset containing some information on atuoscout240-data/manufacture from the files
    dataset = _task1.preProcessingOfData()
    print("The Shape of Dataset:")
    print(dataset.shape)
    print("Dataset type usage description:")
    print(dataset.describe(exclude='number'))


#Uniform Manifold Approximation and Projection (UMAP)
def uniformedApproximationAndProjection():
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

def getOnlySomeColumnsFromDataSet():
    data = hf.readDataset()
    # generate gaussian data sample
    wanted_data_volume = ['price','year']
    data = data[list(wanted_data_volume)]
    data = data.drop_duplicates(subset=wanted_data_volume,keep=False)
    data.rename(columns={'DisplayName': 'Subset'},inplace=True)
    return data

def discretionOfDataset():
    dataset = getOnlySomeColumnsFromDataSet()
    # summarize the shape of the dataset
    print(dataset.shape)
    # summarize each variable
    print(dataset.describe())
    # histograms of the variables
    dataset.hist()
    pyplot.show()
    
    # perform a k-means discretization transform of the dataset
    trans = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans')
    dataset = trans.fit_transform(dataset)
    print(dataset)



def init_Task4():
    reductionAndSubset()
    uniformedApproximationAndProjection()
    getOnlySomeColumnsFromDataSet()
    discretionOfDataset()



init_Task4()
