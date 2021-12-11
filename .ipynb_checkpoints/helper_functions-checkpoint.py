import pandas as pd

#Ngarkimi i datasetit ku kthehet si e 'lexuar'
def readDataset():
    return pd.read_csv(r"autoscout24-germany-dataset.csv")

#Ngarkimi i datasetit ku kthehet si e 'lexuar' permes emrit
def readManufacturers():
    return pd.read_csv(r"manufacturers.csv")

