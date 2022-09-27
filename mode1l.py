# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:01:42 2022

@author: AKammari
"""

import numpy as np
import pickle 
import pandas as pd

data=pd.read_csv("C:\\Users\\AKammari\\Downloads\\advertising.csv")
dataset = pd.DataFrame(data)
Q1=dataset.quantile(0.25)
Q3=dataset.quantile(0.75)
iqr=Q3-Q1
data_clean=dataset[~((dataset<(Q1-1.5*iqr))|(dataset>Q3+1.5*iqr)).any(axis=1)]

X = data_clean.iloc[:,:-1].values
y = data_clean.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.3, random_state = 1 )
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
pickle.dump(regressor,open("model.pkl","wb"))
