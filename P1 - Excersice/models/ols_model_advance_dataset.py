import numpy as np
import pandas
import statsmodels.api as sm

"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""

# Normalisation function used to ensure that each numerical variable has mean = 0
# and standard deviation = 1. Does the same as the function in Lesson 3 of Intro to DS.
def normalise(data):
    mean = data.mean()
    stdev = data.std()
    return (data - mean)/stdev

def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.

    This can be the same code as in the lesson #3 exercise.
    """

    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################

    features = sm.add_constant(features)
    model = sm.log(values,features)
    result = model.fit()
    print(result.summary())
    intercept = result.params[0]
    params = result.params[1:]

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
    features = dataframe[['tempi']].copy()
    features['tempi'] = normalise(features.loc[:,'tempi'])
    #print(features.corr())

    # Hour as dummy feature
    dummy_hour = pandas.get_dummies(dataframe['hour'], prefix='hour')
    dummy_hour.drop(['hour_16'],axis=1,inplace=True)
    features = features.join(dummy_hour)
    #features = dummy_hour
    # Day of week as dummy feature
    dummy_day = pandas.get_dummies(dataframe['day_week'], prefix='day_week')
    dummy_day.drop(['day_week_0'],axis=1,inplace=True)
    features = features.join(dummy_day)
    #features = dummy_day

    # UNIT as dummy features
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    dummy_units.drop(['unit_R003'],axis=1,inplace=True)
    features = features.join(dummy_units)

    '''
    dummy_station = pandas.get_dummies(dataframe['station'], prefix='station')
    dummy_station.drop(['station_CYPRESS HILLS'],axis=1,inplace=True)
    features = features.join(dummy_station)
    '''

    '''
    dummy_conds = pandas.get_dummies(dataframe['conds'], prefix='conds')
    features = features.join(dummy_conds)
    features.drop(['conds_Clear'],axis=1,inplace=True)
    '''

    # Values
    values = dataframe['ENTRIESn_hourly']

    # Perform linear regression
    intercept, params = linear_regression(features, values)

    predictions = intercept + np.dot(features, params)
    return predictions
if __name__ == '__main__':
    file_path = "../data/turnstile_weather_v2.csv"
    file_pointer = open(file_path)
    turnstile_weather = pandas.read_csv(file_pointer)
    print(predictions(turnstile_weather))
    print("Process Completed !!")