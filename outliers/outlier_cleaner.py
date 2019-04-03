#!/usr/bin/python

import numpy as np
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = predictions - net_worths
    percentile_value = np.percentile(error,90)
    #print(error,percentile_value)
    #[(age, net_worth, error) for age, net_worth, error in zip(ages, net_worths, errors) if abs(error) <= threshold]
    cleaned_data = [(age, net_worth, error) for age, net_worth, error in zip(ages, net_worths, error) if abs(error) <= percentile_value]
    return cleaned_data

