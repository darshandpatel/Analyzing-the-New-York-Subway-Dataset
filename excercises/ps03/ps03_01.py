import numpy as np
import pandas
import matplotlib.pyplot as plt


def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.

    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()

    Your histograph may look similar to bar graph in the instructor notes below.

    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms

    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''

    # Create a new data frame from the given turnstile_weather data frame
    # Which has only two columns
    # 1) number of entries per hour on rainy days
    # 2) number of entries per hour on non rainy days
    data_frame = pandas.DataFrame({'Rain' : turnstile_weather[turnstile_weather['rain'] == 1]['ENTRIESn_hourly'],
                                   'No Rain' : turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly']})

    # Find the maximum number of entries on any given day to set the y-axix limit in plot
    y_max_limit = max(data_frame['Rain'].max(),data_frame['No Rain'].max())
    plt.figure()
    data_frame.plot(kind="hist",bins=40)
    plt.xlabel("Entries per Hour")
    plt.ylim(0,y_max_limit)
    plt.title("Histogram of Entries per Hour")
    plt.show()

if __name__ == '__main__':
    file_path = "../data/turnstile_data_master_with_weather.csv"
    file_pointer = open(file_path)
    turnstile_weather = pandas.read_csv(file_pointer)
    entries_histogram(turnstile_weather)