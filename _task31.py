#Import the libraries
import pandas as pd
import numpy as np
import _task1 as _task1
import time
import helper_functions as hf
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from scipy import stats


#***************************************************************************
def getDataSetFromatted():
    dataset = _task1.preProcessingOfData()
    
    # Create a DataFrame object
    datasetDfObj = pd.DataFrame(dataset, columns=[ 'mileage','make','model','fuel','gear','offerType','price','hp','year'])
    return datasetDfObj



#***************************************************************************
#1.

dataset=getDataSetFromatted()


def scatterplot(x_data, y_data, x_label="", y_label="", title="", color = "r", yscale_log=False):

    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 10, color = color, alpha = 0.75)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)



scatterplot(dataset['mileage'], dataset['year'], x_label="Mileage", y_label="Year", title="Cars mileage over theirs years", color = "r", yscale_log=False)

def lineplot(x_data, y_data, x_label="", y_label="", title=""):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

lineplot(dataset['mileage'], dataset['price'], x_label="Mileage", y_label="Price", title="Car price over its mileages")

sns.histplot(dataset['mileage'], kde=True)
plt.show()
print('Distribution of autoscout24\'s cars mileages.')







