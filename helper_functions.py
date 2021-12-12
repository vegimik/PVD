import pandas as pd

#Ngarkimi i datasetit ku kthehet si e 'lexuar'
def readDataset():
    return pd.read_csv(r"autoscout24-germany-dataset.csv")

#Ngarkimi i datasetit ku kthehet si e 'lexuar' permes emrit
def readManufacturers():
    return pd.read_csv(r"manufacturers.csv")

#Ngarkimi i datasetit ku kthehet si e 'lexuar' permes emrit
def readMergedDataset():
    return pd.read_csv(r"autoscout24-germany-dataset-merged.csv")



def missing_cols(df):
    '''prints out columns with its amount of missing values'''
    total = 0
    for col in df.columns:
        missing_vals = df[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {df[col].isnull().sum()}")
    
    if total == 0:
        print("no missing values left")
            
            
            
            
def group_years(year):
    if year in [1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978]:
        group = 'A'
    elif year in [1979,1980,1981,1982,1983,1984]:
        group = 'B'
    elif year in [1985,1986,1987,1988,1989]:
        group = 'C'
    elif year in [1990,1991,1992,1993,1994]:
        group = 'D'
    elif year in [1995,1996,1997,1998,1999]:
        group = 'E'
    elif year in [2000,2001,2002,2003,2004]:
        group = 'F'
    elif year in [2005,2006,2007,2008,2009,2010]:
        group = 'G'
    elif year in [2011,2012,2013,2014,2015,2016,2017]:
        group = 'H'
    else:
        group = ''
    return group

