import pandas as yeet

#3. Using pandas to analyze a file and find the high percipitation
#consider the fact that data is seperated by commas
#print data from the csv in decreasing order.
wd = yeet.read_csv('weather_data.txt', sep=',')
print(wd.sort_values(['actual_precipitation'], ascending=False))

print('------------------------------------------')

#3b. we want to find the avg max temp with july from
#cvs file consider the
# define the date by creating variable, implement using pandas range
# function and compute mean
wd['date'] = yeet.to_datetime(wd['date'])
s_d = '01-07-2014'
e_d = '31-07-2014'
# calling created variables into pandas function
s_d = yeet.to_datetime(s_d)
e_d = yeet.to_datetime((e_d), infer_datetime_format=True)
# creating a new variable to implement pandas between and mean function
avgmxtemp = wd[wd['date'].between(s_d, e_d)]
print(avgmxtemp['actual_max_temp'].mean())

print('------------------------------------------')

#3c. Find what day is act max temp = rec max temp
print(wd.sort_values(['actual_max_temp', 'record_max_temp'], ascending=False)['date'])

print('------------------------------------------')

#3d.Finding the precipitation in october 2014
wd['date'] = yeet.to_datetime(wd['date'])
day_start = '01-10-2014'
day_end = '31-10-2014'
day_start = yeet.to_datetime(day_start)
day_end = yeet.to_datetime((day_end), infer_datetime_format=True)
oct = wd[wd['date'].between(day_start, day_end)]
print(oct['actual_precipitation'].sum())

print('------------------------------------------')

#3e. WHat day has the temp below 60 and actual max temp
#above 90 degree on the same day

coin = (wd['actual_min_temp'] < 60) & (wd['actual_max_temp'] > 90)
print(wd[coin])

print('------------------------------------------')

