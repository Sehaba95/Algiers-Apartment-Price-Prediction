#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score,ShuffleSplit
from sklearn import preprocessing

data = pd.read_csv("clean_data.csv",sep=",",index_col=None, prefix=None,skip_blank_lines=True,header=0)

X = data.loc[:,["Quartier","Commune","Etage","Superficie","Piece","Electricite" ,  "Gaz" ,  "Eau" ,  "Acte notarie","Jardin" , "Livret foncier", "Meuble", "Garage"]].values
Y = data.loc[:,"Prix"].values

X = pd.DataFrame(X)


le = preprocessing.LabelEncoder()
X = X.apply(le.fit_transform)


scaler = preprocessing.StandardScaler().fit(X)
X = scaler.transform(X)
scaler = preprocessing.Normalizer().fit(X)
X = scaler.transform(X)
binarizer = preprocessing.Binarizer(threshold=0.0).fit(X)
X = binarizer.transform(X)

regressor = LinearRegression()
shuffle = ShuffleSplit(n_splits=10,test_size=0.3)

scores = cross_val_score(regressor,X,Y,cv=shuffle)

max = 0
for score in scores:
	if max < score:
		max = score
print(max)