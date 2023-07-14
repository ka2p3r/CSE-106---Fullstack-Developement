import matplotlib.pyplot as yah
import pandas as yeet
wd = yeet.read_csv('weather_data.txt')

wd[['actual_max_temp', 'actual_min_temp']].plot(color=['red', 'blue'])

yah.show()

print('---------------------------------------------------------------')


hist = wd['actual_precipitation'].hist()
yah.show()
