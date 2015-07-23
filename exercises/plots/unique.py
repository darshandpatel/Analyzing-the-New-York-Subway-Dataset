import pandas as pd
import numpy as np
from ggplot import *


def plot_weather_data(turnstile_weather):
    pd.options.mode.chained_assignment = None
    turnstile_weather_grp_by_station_hour = turnstile_weather.groupby(['Hour']).sum()
    turnstile_weather_grp_by_station_hour = turnstile_weather_grp_by_station_hour.reset_index()
    print(ggplot(aes(x='Hour',y='ENTRIESn_hourly'),data=turnstile_weather_grp_by_station_hour) + \
          geom_point() + geom_line() + xlim(0,23) + xlab("Hour") \
          + ylab("Number of Entries") + ggtitle("Number of Entries per Hour"))


if __name__ == '__main__':
    file_path = "../data/turnstile_data_master_with_weather.csv"
    file_pointer = open(file_path)
    turnstile_weather = pd.read_csv(file_pointer)
    plot_weather_data(turnstile_weather)