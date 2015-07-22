import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys
import pandas
import statsmodels.api as sm

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


def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.

    This can be the same code as in the lesson #3 exercise.
    """

    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
    features = sm.add_constant(features)
    model = sm.OLS(values,features)
    result = model.fit()
    intercept = result.params[0]
    params = result.params[1:]
    print(result.params)
    return intercept, params

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.

    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe.
    We recommend that you don't use the EXITSn_hourly feature as an input to the
    linear model because we cannot use it as a predictor: we cannot use exits
    counts as a way to predict entry counts.

    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~10%) of the data contained in
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with
    this exercise on your own computer, locally. If you do, you may want to complete Exercise
    8 using gradient descent, or limit your number of features to 10 or so, since ordinary
    least squares can be very slow for a large number of features.

    If you receive a "server has encountered an error" message, that means you are
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number of features.
    '''
    ################################ MODIFY THIS SECTION #####################################
    # Select features. You should modify this section to try different features!             #
    # We've selected rain, precipi, Hour, meantempi, and UNIT (as a dummy) to start you off. #
    # See this page for more info about dummy variables:                                     #
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html          #
    ##########################################################################################

    '''
    features = dataframe[['rain', 'precipi', 'hour', 'meantempi']]
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)

    # Values
    values = dataframe['ENTRIESn_hourly']
    '''

    features = dataframe[['fog','rain' ,'tempi','wspdi','precipi','hour']]

    # Normalize the features.
    '''
    features['tempi'] = features['tempi'] - features['tempi'].mean()
    features['wspdi'] = features['wspdi'] - features['wspdi'].mean()
    features['precipi'] = features['precipi'] - features['precipi'].mean()
    '''
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)

    dummy_conds = pandas.get_dummies(dataframe['conds'], prefix='conds')
    features = features.join(dummy_conds)

    dummy_station = pandas.get_dummies(dataframe['station'], prefix='station')
    features = features.join(dummy_station)

    # Values
    values = dataframe['ENTRIESn_hourly']

    # Perform linear regression
    intercept, params = linear_regression(features, values)

    predictions = intercept + np.dot(features, params)
    return predictions

if __name__ == '__main__':
    #file_path = "turnstile_data_master_with_weather.csv"
    file_path = "turnstile_weather_v2.csv"
    file_pointer = open(file_path)
    turnstile_weather = pandas.read_csv(file_pointer)
    print(compute_r_squared(turnstile_weather['ENTRIESn_hourly'],predictions(turnstile_weather)))