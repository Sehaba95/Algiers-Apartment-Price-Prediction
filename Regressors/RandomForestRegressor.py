#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("final_dataset.csv",header=0)

X = data.loc[:,["Commune","Etage","Superficie","Piece","Electricite","Gaz","Eau","Acte notarie","Jardin","Livret foncier","Meuble","Garage","Prix M2"]].values
Y = data.loc[:,"Prix"].values

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

regressor = RandomForestRegressor(max_depth=4, random_state=0)
regressor.fit(X_train,Y_train)
score = regressor.score(X_test,Y_test)
print(score)