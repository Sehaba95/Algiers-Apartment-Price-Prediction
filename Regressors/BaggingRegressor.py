#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn import preprocessing

data = pd.read_csv("clean_data.csv",sep=",",index_col=None, prefix=None,skip_blank_lines=True,header=0)

X = data.loc[:,["Quartier","Commune","Etage","Superficie","Piece","Electricite" ,  "Gaz" ,  "Eau" ,  "Acte notarie","Jardin" , "Livret foncier", "Meuble", "Garage"]].values
Y = data.loc[:,"Prix"].values

X = pd.DataFrame(X)


le = preprocessing.LabelEncoder()
X = X.apply(le.fit_transform)


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

regressor = BaggingRegressor(DecisionTreeRegressor(max_depth=4))
regressor.fit(X_train,Y_train)
score = regressor.score(X_test,Y_test)
print score