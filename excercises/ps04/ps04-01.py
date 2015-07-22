from pandas import *
from ggplot import *
import numpy

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    To see all the columns and data points included in the turnstile_weather
    dataframe.

    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    pandas.options.mode.chained_assignment = None
    #turnstile_weather.set_index(['Hour'])
    turnstile_weather_grp_by_hour = turnstile_weather.groupby('Hour').sum()
    turnstile_weather_grp_by_hour = turnstile_weather_grp_by_hour.reset_index()
    '''
    turnstile_weather.is_copy = False
    #print(turnstile_weather_grp_by_unit.head(3))
    turnstile_weather_grp_by_hour.index.name='Hour'
    turnstile_weather_grp_by_hour = turnstile_weather_grp_by_hour.reset_index()
    #print(new.head(3))
    '''

    #print(ggplot(turnstile_weather_grp_by_hour,aes(x='Hour',y='ENTRIESn_hourly')) + geom_point(color='red') +xlim(0,23)+geom_line(color="blue") + \
    #    scale_y_continuous(labels='comma') + ggtitle('Head of Cattle Slaughtered by Decade'))

    print(ggplot(turnstile_weather_grp_by_hour,aes(x='Hour',y='ENTRIESn_hourly'))+geom_bar(stat='identity')+xlim(-0.5,23.5)+xlab("Hour")+ylab("Number of Entries")+\
          ggtitle("Number of Entries per Hour"))
    #print(ggplot(turnstile_weather,aes(x='DATEn',weight='ENTRIESn_hourly',fill='DATEn'))+geom_bar(stat="identity"))

    #plot = # your code here
    #return plot

file_path = "turnstile_data_master_with_weather.csv"
file_pointer = open(file_path)
turnstile_weather = pandas.read_csv(file_pointer)
plot_weather_data(turnstile_weather)