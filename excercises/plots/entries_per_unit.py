from pandas import *
from ggplot import *
import numpy

def plot_weather_data(turnstile_weather):

    turnstile_weather_grp_by_hour = turnstile_weather.groupby('UNIT').sum()
    turnstile_weather_grp_by_hour = turnstile_weather_grp_by_hour.reset_index()


    print(ggplot(turnstile_weather_grp_by_hour,aes(x='UNIT',y='ENTRIESn_hourly'))+geom_bar(stat='identity')+xlab("UNIT")+ylab("Number of Entries")+\
          ggtitle("Number of Entries per UNIT"))


if __name__ == '__main__':
    file_path = "turnstile_data_master_with_weather.csv"
    file_pointer = open(file_path)
    turnstile_weather = pandas.read_csv(file_pointer)
    plot_weather_data(turnstile_weather)