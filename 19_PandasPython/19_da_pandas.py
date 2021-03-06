# -*- coding: utf-8 -*-
"""19_DA_Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xLwmHbvC1wyJgV4u2mpwPTo_FSd_fM4J

# 19_DA_Pandas

### Import Library
"""

!pip install pandas
import pandas
pandas.__version__

"""###Loading Data-Series"""

import pandas as pd
a = [7,9,4]
dataset = pd.Series(a)
print(dataset)

import pandas as pd
a = [7,9,4]
dataset = pd.Series(a, index = ["No.1","No.2","No.3"])
print(dataset)

"""###Loading Data-DataFrame"""

import pandas as pd
data = {"Name":["Champ","Mr.X","Mr.y"],"Color":["Red","Black","White"]}
dataset = pd.DataFrame(data)
print(dataset)

"""###Loading Dataset from File"""

import pandas as pd
dataset1 = pd.read_csv("dataset.csv")
print(dataset1.head(5))

import pandas as pd
dataset2 = pd.read_excel("dataset.xlsx")
print(dataset2.head(5))

import pandas as pd
dataset3 = pd.read_csv("dataset.txt")
print(dataset3.head(5))

"""###Dataset Details"""

print(dataset1.shape) #No.of Rows and Columns
print(dataset1.describe()) #Detailed info about Dataset

"""###Data Slicing

"""

print(dataset1.columns) #To get only Column Title
print(dataset1["Name"]) #To get data based on the specific Title
print(dataset1[["Name","Speed"]]) #To get data based on the multiple Title
print(dataset1["Name"][0:6]) #To get data based on the specific Title with Specific Count

print(dataset1.iloc[0]) #integer location-acquire complete info about certain index
print(dataset1.iloc[1:5]) #acquire complete info about range of index
print(dataset1.iloc[1,2]) #acquire specific cell data

for index,row in dataset1.iterrows():
  print(index,row["Name"])

"""###Data Slicing with Filter"""

print(dataset1.loc[dataset1["Type 2"]>90])

"""### Slicing - Sorting Data"""

dataset1.sort_values(["Speed"],ascending=False)

"""###Editing Data"""

dataset1["Power"] = dataset1["HP"] + dataset1["Attack"]
print(dataset1.head(5))

dataset1 = dataset1.drop(columns=["Power"]) #removing Column
print(dataset1.head(5))

"""###Save Dataset in new file"""

dataset1.to_csv("newDataset.csv")
dataset1.to_excel("newDataset.xlsx")
dataset1.to_csv("newDataset.csv",index=False, sep="\t")

"""### Checking Null values in Dataset"""

dataset1.isna().any()

"""###Acquiring Dataset without NaN Value, by removing the entire column"""

dataset1 = dataset1[dataset1["Type 2"].notna()]

"""###Filling NaN with mean of that specific Column"""

MeandatasetNotNan = dataset1["Speed"].fillna(dataset1["Speed"].mean())
MeandatasetNotNan

"""### Mapping certain Data to another value"""

print(dataset1.head(5))
Generation = set(dataset1['Generation'])
dataset1['Generation'] = dataset1['Generation'].map({1: "one", 2: "two",3: "three", 4: "four",5: "five", 6: "six"}).astype(str)
print(dataset1.head(5))