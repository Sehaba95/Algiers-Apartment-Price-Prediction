#!/usr/bin/env python

import pandas as pd 

data = pd.read_csv("data.csv")

#Delete all the rows which doesn't conatin price 
#Delete unlabeled rows
Y = data[pd.notnull(data.Price)]

print(data.head(10))
print(Y.head(10))

Y.to_csv("clean_data.csv",header=False,index=False)

