#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import HuberRegressor

data = pd.read_csv("clean_data1.csv",header=0)

X = data.loc[:,["Commune","Etage","Superficie","Piece"]].values
Y = data.loc[:,"Prix"].values

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

huber = HuberRegressor(fit_intercept=True, alpha=0.0, max_iter=100,epsilon=3.0)
huber.fit(X_train, Y_train)
score = huber.score(X_test,Y_test)
print(score)