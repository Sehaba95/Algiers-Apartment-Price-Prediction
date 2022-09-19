#!/usr/bin/env python

import pandas as pd 

#load data: ["City","Url","Date","Temps","Quartier", "Piece", "Etage", "Superficie", "Specification", "Price"]
data = pd.read_csv("data.csv")

#Delete all the rows which doesn't conatin price 
#Delete unlabeled rows
data = data[pd.notnull(data.Price)]

#Delete duplicates rows
data1 = data.drop_duplicates()

#Split : - X (Features)		- Y (Labels)
X = data1.loc[:,["City","Date", "Piece", "Etage", "Superficie"]].values
Y = data1.loc[:,"Price"].values

#Convert the price if its in Milliards and add it to the price list or add it directly if its not the case
price = []
for value in Y:
	if (value.split())[1] == "Milliards":
		p = float((value.split())[0]) * 1000 
		price.append( str (int (p) )) 
	else: 
		if float((value.split())[0]) > 100:
			price.append((value.split())[0])

#Convert both of Features and Labels to DataFrame
Y = pd.DataFrame(price)
X = pd.DataFrame(X)

#Concatenate the result and export it to a csv file
finalDF = pd.concat([X,Y],axis=1)
finalDF.to_csv("features_labels.csv",header=["City","Date", "Piece", "Etage", "Superficie", "Price"],index=False)



