#static and inertial visualization, multi-dimensional data visualization
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
from matplotlib import cm
import seaborn as sns
import _task1 as _task1

dataset = _task1.preProcessingOfData()
def visualizationOfData():
    pd.DataFrame(dataset).plot()
    plt.show()

def heatMap():  
    # generating correlation heatmap
    sns.heatmap(dataset.corr(), annot = True)
    # posting correlation heatmap to output console 
    plt.show()
    
def corelation():
    # generating correlation data
    df = dataset.corr()
    df.index = range(0, len(df))
    df.rename(columns = dict(zip(df.columns, df.index)), inplace = True)
    df = df.astype(object)
    ''' Generating coordinates with 
    corresponding correlation values '''
    for i in range(0, len(df)):
        for j in range(0, len(df)):
            if i != j:
                df.iloc[i, j] = (i, j, df.iloc[i, j])
            else :
                df.iloc[i, j] = (i, j, 0)

    df_list = []

    # flattening dataframe values
    for sub_list in df.values:
        df_list.extend(sub_list)

    # converting list of tuples into trivariate dataframe
    plot_df = pd.DataFrame(df_list)

    fig = plt.figure()
    ax = Axes3D(fig)

    # plotting 3D trisurface plot
    ax.plot_trisurf(plot_df[0], plot_df[1], plot_df[2], 
                        cmap = cm.jet, linewidth = 0.2)

    plt.show()

#multidimensional data visualization 
visualizationOfData()
heatMap()
corelation()

