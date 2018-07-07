#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

data = pd.read_csv("clean_data1.csv",header=0)

X = data.loc[:,["Commune","Etage","Superficie","Piece"]].values
Y = data.loc[:,"Prix"].values

poly = preprocessing.PolynomialFeatures(degree=2)
X =  poly.fit_transform(X)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)

regressor = LinearRegression()
regressor.fit(X_train,Y_train)
score = regressor.score(X_test,Y_test)
print(score)