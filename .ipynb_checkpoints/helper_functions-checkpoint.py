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
            