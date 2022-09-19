#!/usr/bin/env python

import pandas as pd
import numpy as np  

#replace cities with their codes 
data = pd.read_csv("features_labels.csv")

#["City","Piece","Etage","Superficie","Price"]
X = data.loc[:,["City","Piece","Superficie","Price"]].values
Y = data.loc[:,"Etage"].values

#Convert the price if its in Milliards and add it to the price list or add it directly if its not the case
etage = []
for value in Y:
	if value > 20 :
		etage.append(np.nan)
	else: 
		etage.append(value)

Y = pd.DataFrame(etage)
X = pd.DataFrame(X)

finalDF = pd.concat([Y,X],axis=1)
finalDF.to_csv("features_labels.csv",header=["Etage","Piece","Superficie","City","Prix"],index=False)

'''
X = data.loc[:,["City", "Piece", "Etage", "Price","Date"]].values
Y = data.loc[:,"Superficie"].values

Superficie = []
for value in Y:
	Superficie.append(value.split(" ")[0])
'''

'''
data = data.loc[:,["City", "Piece","Superficie","Etage","Prix"]].values
data = pd.DataFrame(data)
data.to_csv("finald_datasets.csv",header=["City", "Piece","Superficie","Etage","Prix"],index=False)
'''


'''
Y = data.loc[:,"Prix"].values
X = pd.DataFrame(X)
Y = pd.DataFrame(Y)
floor = []
for value in Y:
	if pd.isnull(value):
		floor.append(1)
	else:
		floor.append(value)
#Convert both of Features and Labels to DataFrame
Y = pd.DataFrame(floor)
X = pd.DataFrame(X)
#Concatenate the result and export it to a csv file
finalDF = pd.concat([X,Y],axis=1)
finalDF.to_csv("features_labels.csv",header=["City", "Piece","Date","Superficie", "Etage", "Prix"],index=False)
'''