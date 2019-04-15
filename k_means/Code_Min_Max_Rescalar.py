# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:13:03 2019

@author: Guru
"""

""" quiz materials for feature scaling clustering """
import numpy as np

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    dataSorted = sorted(arr)
    Xmin = dataSorted[0]
    Xmax = dataSorted[-1]
    print(Xmax-Xmin)
    rescaledData = [ (data-Xmin)/(Xmax-Xmin)  for data in dataSorted]
    return rescaledData

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print(featureScaling(data))

