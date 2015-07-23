import numpy as np
import scipy
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
import sys
from excercises.ps03.ps03_04 import predictions

"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''


    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).plot(kind="hist",bins=10)
    plt.title("Histogram of Residuals")
    plt.ylabel("Frequency")
    plt.xlabel("Prediction Error")
    plt.show()

    '''
    # QQ Plot
    z = (turnstile_weather['ENTRIESn_hourly'] - np.mean(turnstile_weather['ENTRIESn_hourly']))/np.std(turnstile_weather['ENTRIESn_hourly'])
    stats.probplot(z,dist="norm",plot=plt)
    plt.show()
    '''


if __name__ == '__main__':
    file_path = "../data/turnstile_weather_v2.csv"
    file_pointer = open(file_path)
    turnstile_weather = pandas.read_csv(file_pointer)
    plot_residuals(turnstile_weather,predictions(turnstile_weather))