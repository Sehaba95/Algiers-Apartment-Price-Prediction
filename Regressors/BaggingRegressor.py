#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn import preprocessing

data = pd.read_csv("final_dataset.csv",header=0)

X = data.loc[:,["Commune","Etage","Superficie","Piece","Electricite","Gaz","Eau","Acte notarie","Jardin","Livret foncier","Meuble","Garage","Prix M2"]].values
Y = data.loc[:,"Prix"].values

scaler = preprocessing.StandardScaler().fit(X)
X = scaler.transform(X)


max = 0 

for depth in range(2,10):
	print(depth)
	for i in range(0,100):
		X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

		regressor = BaggingRegressor(DecisionTreeRegressor(max_depth=4))
		regressor.fit(X_train,Y_train)
		score = regressor.score(X_test,Y_test)
		print score

		if max < score:
			max = score

print(max)
