#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

data = pd.read_csv("dataset.csv",header=0)

X = data.loc[:,["Commune","Etage","Piece","Superficie"]].values
Y = data.loc[:,"Prix"].values

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
max = 0

for depth in range(2,10):
	print(depth)
	for i in range(0,100):
		regressor = AdaBoostRegressor(DecisionTreeRegressor(max_depth=depth),n_estimators=100)
		regressor.fit(X_train,Y_train)
		score = regressor.score(X_test,Y_test)
		#print(score)

		if max < score:
			max = score

print(max)