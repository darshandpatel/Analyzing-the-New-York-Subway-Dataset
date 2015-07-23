from pandas import *
from ggplot import *


def plot_weather_data(turnstile_weather):

    turnstile_weather_grp_by_hour = turnstile_weather.groupby('day_week').sum()
    turnstile_weather_grp_by_hour = turnstile_weather_grp_by_hour.reset_index()
    turnstile_weather_grp_by_hour.sort('day_week')
    week_day_names = pandas.Series(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    week_day_df = pandas.DataFrame({'days' : week_day_names})
    turnstile_weather_grp_by_hour = turnstile_weather_grp_by_hour.join(week_day_df)

    print(ggplot(turnstile_weather_grp_by_hour,aes(x='days',y='ENTRIESn_hourly')) + \
          geom_bar(stat='identity') + xlab("Day") + ylab("Number of Entries") + \
          ggtitle("Number of Entries per Day"))

if __name__ == '__main__':
    file_path = "../data/turnstile_weather_v2.csv"
    file_pointer = open(file_path)
    turnstile_weather = pandas.read_csv(file_pointer)
    plot_weather_data(turnstile_weather)