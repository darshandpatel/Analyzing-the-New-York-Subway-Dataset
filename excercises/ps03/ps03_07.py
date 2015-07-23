import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys
import pandas
import statsmodels.api as sm
from excercises.ps03.ps03_04 import predictions


def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.
    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    '''
    
    # your code here
    data_avg = np.mean(data)
    partial_denominator = data - data_avg
    denominator = np.sum(partial_denominator*partial_denominator)
    partial_numerator = data - predictions
    numerator = np.sum(partial_numerator*partial_numerator)
    r_squared = 1 - float(numerator/denominator)
    return r_squared

if __name__ == '__main__':
    file_path = "../data/turnstile_weather_v2.csv"
    file_pointer = open(file_path)
    turnstile_weather = pandas.read_csv(file_pointer)
    print(compute_r_squared(turnstile_weather['ENTRIESn_hourly'],predictions(turnstile_weather)))